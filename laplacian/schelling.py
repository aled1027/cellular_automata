import random
from laplacian import Laplacian
from scipy.stats import poisson


class Agent(object):
    def __init__(self, race='black'):
        self.race = race
        self.graph = None
        self.is_happy = False

    def update_happiness(self, nbr_dict=None):
        num_nbrs = 0
        if nbr_dict == None:
            nbrs = self.graph.get_neighbors(self)
            nbr_races = [nbr.race for (edge_weight, nbr) in nbrs for _ in range(edge_weight)]
            nbr_dict = {race: nbr_races.count(race) for race in ['white', 'black']}
            num_nbrs = len(nbrs)
        else:
            num_nbrs = sum(nbr_dict.values())

        if num_nbrs == 0:
            self.is_happy = False
            return
        ratio = float(nbr_dict[self.race]) / num_nbrs
        if ratio > self.graph.pref_alike:
            self.is_happy = True
        else:
            self.is_happy = False

class Graph(list):
    def __init__(self, num_agents=5, moving_mu=0.5, agents=None, \
            laplacian=None, pref_alike=0.7):
        self.pref_alike = 0.5
        self.moving_mu = moving_mu
        self.races = ['white', 'black']
        if agents == None:
            agents = self.generate_agents(num_agents)
        list.__init__(self, agents)
        self.laplacian = Laplacian(size=len(self))
        if laplacian == None:
            self.laplacian = self.generate_laplacian()
        self.unhappy_agents = []
        for agent in self:
            agent.graph = self
            agent.update_happiness()
            if agent.is_happy == False:
                self.unhappy_agents.append(agent)
        self.compute_avg_similarity()


    def generate_agents(self, num_agents):
        """
        generates a list of agents with a random race
        """
        li = []
        for _ in range(num_agents):
            r = random.randint(0,1)
            if r == 0:
                li.append(Agent(race='white'))
            else:
                li.append(Agent(race='black'))
        return li

    def generate_laplacian(self):
        """
        generates a random, symmetric laplacian.
        """
        num_agents = len(self)
        li = []
        for i in range(num_agents):
            sample = poisson(self.moving_mu).rvs(num_agents - i).tolist()
            zeros = ([0]*i)
            zeros.extend(sample)
            li.append(zeros)
        ret_lap = Laplacian(xs=li)
        ret_lap.symmetrize()
        return ret_lap

    def compute_avg_similarity(self):
        # calculates average similarity ratio
        # similarity ratio = # your race / # total nbrs
        similarity = []
        for agent in self:
            nbrs = self.get_neighbors(agent)
            nbr_races = [nbr.race for (edge_weight, nbr) in nbrs for _ in range(edge_weight)]
            nbr_dict = {race: nbr_races.count(race) for race in self.races}
            num_nbrs = sum(nbr_dict.values())
            if num_nbrs  == 0:
                similarity.append(1)
            else:
                ratio = float(nbr_dict[agent.race]) / float(num_nbrs)
                similarity.append(ratio)
        self.avg_similarity = float(sum(similarity)) / float(len(similarity))
        return self.avg_similarity

    @property
    def happiness_ratio(self):
        if len(self) == 0:
            return 0
        return 1 - (float(len(self.unhappy_agents)) / len(self))

    @property
    def num_edges(self):
        return self.laplacian.num_edges

    def get_neighbors(self, agent):
        """
        returns the neighbors of the agents.
        """
        row = self.index(agent)
        return [(entry, self[idx]) for (entry, idx) in self.laplacian.get_neighbor_indices(row=row)]

    def update(self):
        self.move_someone()
        self.unhappy_agents = []
        for agent in self:
            agent.graph = self

            nbrs = self.get_neighbors(agent)
            nbr_races = [nbr.race for (edge_weight, nbr) in nbrs for _ in range(edge_weight)]
            nbr_dict = {race: nbr_races.count(race) for race in self.races}

            agent.update_happiness(nbr_dict=nbr_dict)

            if agent.is_happy == False:
                self.unhappy_agents.append(agent)

            num_nbrs = sum(nbr_dict.values())
            similarity = []
            if num_nbrs  == 0:
                similarity.append(1)
            else:
                ratio = float(nbr_dict[agent.race]) / float(num_nbrs)
                similarity.append(ratio)

            self.avg_similarity = float(sum(similarity)) / float(len(similarity))

    def move_someone(self):
        """
        Picks a random unhappy agent.
        Then, we use a poisson distribution to sample (#agents - 1) values
        By the nature of the poisson distribution, each of these values is independent
        Then we save the sampled values as the weight edges for this agent.
        Since the laplacian is symmetric, we also update other agents' inedges.
        """
        if not self.unhappy_agents:
            return
        agent = random.choice(self.unhappy_agents)
        agent_idx = self.index(agent)
        sample = poisson(self.moving_mu).rvs(len(self)-1).tolist()
        # insert value into diagonal entry
        sample.insert(agent_idx, -1 * sum(sample))
        # update row
        self.laplacian[agent_idx] = sample
        # update column
        self.laplacian[None, agent_idx] = sample

if __name__ == '__main__':
    g = Graph()
    l = g.laplacian


