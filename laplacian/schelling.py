import random
from laplacian import Laplacian
from scipy.stats import poisson

pref_alike = 0.5

class Agent(object):
    def __init__(self, race='black'):
        self.race = race
        self.graph = None
        self.is_happy = False

    def update_happiness(self):
        nbrs = self.graph.get_neighbors(self)
        if len(nbrs) == 0:
            self.is_happy = False
            return

        nbr_races = [nbr.race for nbr in nbrs]
        nbr_dict = {race: nbr_races.count(race) for race in ['white', 'black']}
        ratio = float(nbr_dict[self.race]) / len(nbrs)

        if ratio > pref_alike:
            self.is_happy = True
        else:
            self.is_happy = False

class Graph(list):
    def __init__(self, num_agents=15, edge_threshold=0.33, moving_mu=0.5, agents=None, laplacian=None):
        self.moving_mu = moving_mu
        if agents == None:
            agents = self.generate_agents(num_agents)
        list.__init__(self, agents)

        if laplacian == None:
            self.laplacian = self.generate_laplacian(edge_threshold)

        self.unhappy_agents = []

        for agent in self:
            agent.graph = self

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

    def generate_laplacian(self, edge_threshold):
        """
        generates a random laplacian.
        """
        num_agents = len(self)
        ret_lap = Laplacian(size=num_agents)
        for i in range(num_agents):
            sample = poisson(self.moving_mu).rvs(len(self)-1).tolist()
            # insert value into diagonal entry
            sample.insert(i, -1 * sum(sample))
            ret_lap[i] = sample
        return ret_lap

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
        return [self[i] for i in self.laplacian.get_neighbor_indices(row=row)]

    def update(self):
        self.move_someone()
        self.unhappy_agents = []
        for agent in self:
            agent.graph = self
            agent.update_happiness()
            if agent.is_happy == False:
                self.unhappy_agents.append(agent)

    def move_someone(self):
        """
        TODO document
        """
        # determine the agent to move:
        if not self.unhappy_agents:
            return
        agent = random.choice(self.unhappy_agents)
        agent_idx = self.index(agent)
        sample = poisson(self.moving_mu).rvs(len(self)-1).tolist()
        # insert value into diagonal entry
        sample.insert(agent_idx, -1 * sum(sample))
        self.laplacian[agent_idx] = sample





