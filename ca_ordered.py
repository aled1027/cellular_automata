import random
import numpy as np

pref_alike = 0.3

class Agent(object):
    def __init__(self, race='black')
        self.race = race
        self.board = None
        self.is_happy = False

    def update_happiness(self):
        nbrs = self.board.get_neighbors(self)
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

class Board(list):
    def __init__(self, num_agents=15, edge_threshold=0.33, agents=None, laplacian=None):
        if agents == None:
            agents = self.generate_agents(num_agents=num_agents)
        list.__init__(self, agents)

        if laplacian == None:
            self.laplacian = self.generate_laplacian(edge_threshold=edge_threshold)
        self.unhappy_agents = []

        for agent in self:
            agent.board = self
        self.update()

    def generate_agents(num_agents):
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
        self.laplacian = np.matrix(np.zeros(shape=(num_agents, num_agents)))
        for i in range(num_agents):
            for j in range(num_agents):
                if i == j:
                    self.laplacian[i,j] = 0
                else:
                    r = random.random()
                    self.laplacian[i,j] = 1 if r < edge_threshold else 0
    @property
    def happiness_ratio(self):
        if len(self) == 0:
            return 0
        return 1 - (float(len(self.unhappy_agents)) / len(self))

    @property
    def num_edges(self):
        return len(np.transpose(np.nonzero(self.laplacian)))

    def get_neighbors(self, agent):
        """
        returns the neighbors of the agents.
        """
        row_number = self.index(agent)
        _, ys = self.laplacian[row_number].nonzero()

        # take the zeroith element because for some reason the list is nested
        return [self[y] for y in ys.tolist()[0]]

    def update(self):
        # todo add self.move_someone
        # self.move_someone()
        self.unhappy_agents = []
        for agent in self:
            agent.board = self
            agent.update_happiness()
            if agent.is_happy == False:
                self.unhappy_agents.append(agent)

if __name__ == '__main__':

    b = Board(num_agents=15, edge_threshold=0.33)
    print len(b), b.num_edges
    b.update()


