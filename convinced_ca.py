import sys
import pygame
from pygame.locals import *
import random
from ca_ordered import Agent, Board

import numpy as np

colors = {'orange': (255, 102, 0),
          'teal': (0, 128, 128),
          'white': (255, 255, 255),
          'light_gray': (220, 220, 220),
          'green': (0, 220, 0),
          }

class ConvincedAgent(Agent):
    def __init__(self, pos=(0,0), board_width=8, convinced=0.0):
        Agent.__init__(self,pos=pos, board_width=board_width)
        self.convinced = convinced
        self.board = None
        self.col = (0,0,0)

    def update_convinced(self):
        nbr_coords = self.board.get_neighbor_coords(self.pos)
        nbr_convinced = sum([self.board[nbr].convinced for nbr in nbr_coords])
        num_nbrs = len([1 for nbr in nbr_coords if nbr in self.board])
        if num_nbrs > 0:
            # todo maybe fix up this function.
            # perhaps the core of the model
            average_convinced = float(nbr_convinced) / num_nbrs
            delta = (average_convinced - self.convinced) / 4.0
            self.convinced += delta

    def draw_convinced(self, surface):
        c = float(self.convinced / self.board.highest_convinced) * 255.0
        self.col = (c,c,c)
        super(ConvincedAgent, self).draw(surface)

class ConvincedBoard(Board):
    def __init__(self, width, height, state):
        edge_threshold = 0.3

        Board.__init__(self, width, height, state)
        self.cell_radius = 400 / self.width
        self.empty_color = colors['green']
        num_agents = len(self)

        self.laplacian = np.matrix(np.zeros(shape=(num_agents, num_agents)))
        for i in range(num_agents):
            for j in range(num_agents):
                if i == j:
                    self.laplacian[i,j] = 0
                r = random.random()
                self.laplacian[i,j] = 1 if r < edge_threshold else 0

        for agent in self.values():
            agent.board = self

        self.update()

    @property
    def num_edges(self):
        return len(np.transpose(np.nonzero(self.laplacian)))

    @property
    def convinced(self):
        tot_convinced = 0.0
        for agent in self.values():
            if agent:
                tot_convinced += agent.convinced
        return tot_convinced

    @property
    def highest_convinced(self):
        return max([agent.convinced for agent in self.values() if agent])

    def get_neighbor_coords(self, pos):
        if pos[0] < 0:
            raise RuntimeError("Width %d less than number of cells. " % pos[0])
        elif pos[0] >= self.width:
            raise RuntimeError("Width %d greater than number of cells. " % pos[0])
        elif pos[1] < 0:
            raise RuntimeError("Height %d less than number of cells. " % pos[1])
        elif pos[1] >= self.height:
            raise RuntimeError("Height %d greater than number of cells. " % pos[1])

        def is_good_coord(pos):
            b1 = (0 <= pos[0] < self.width) and (0 <= pos[1] < self.height)
            b2 = pos in self
            return b1 and b2 and self[pos[0], pos[1]] is not None

        deltas = [(a,b) for a in range(-1,2) for b in range(-1,2) if (a,b) != (0,0)]
        return [(pos[0] + a, pos[1] + b) for (a,b) in deltas if is_good_coord((pos[0] + a, pos[1] + b))]

    def draw_convinced(self, surface):
        for coord, agent in zip(self.keys(), self.values()):
            if agent is None:
                # we should never be here.
                # todo, change this if statement to an assert / exception thing
                rect = (coord[0] * self.radius, coord[1] * self.radius, self.radius, self.radius)
                pygame.draw.rect(surface, self.empty_color, rect)
            else:
                agent.draw_convinced(surface)

    def update(self):
        for agent in self.values():
            agent.board = self
        # self.move_someone()
        self.update_convinced()

    def update_convinced(self):
        for agent in self.values():
            agent.update_convinced()


if __name__ == '__main__':
    n = 4
    empty_board = {}
    for i in range(n):
        for j in range(n):
            r1 = random.randint(0,100)
            if r1 < 60:
                r2 = (random.random() * 4)
                empty_board[i,j] = ConvincedAgent((i,j), board_width=n, convinced=r2)

    b = ConvincedBoard(n,n,empty_board)
    # print len(b), b.num_edges


#    pygame.init()
#    screen = pygame.display.set_mode((800, 800))
#    pygame.display.set_caption('Cellular Automata')
#
#    # Fill background
#    con_background = pygame.Surface(screen.get_size())
#    con_background = con_background.convert()
#    con_background.fill(colors['green'])
#
#    # blit to screen
#    screen.blit(con_background, (0, 0))
#    pygame.display.flip()
#
#    UPDATE_BOARD = USEREVENT + 1
#    pygame.time.set_timer(UPDATE_BOARD, 10)
#
#    cycle = 0
#    while True:
#        for event in pygame.event.get():
#            if event.type == QUIT:
#                sys.exit()
#                # return
#            elif event.type == pygame.KEYUP:
#                if event.key == 32:
#                    # continue
#                    for _ in range(5):
#                        cycle = cycle + 1
#                        print ("Cycle: %d" % (cycle))
#                        b.update()
#            elif event.type == UPDATE_BOARD:
#                continue
#                cycle = cycle + 1
#                print ("Cycle: %d" % (cycle))
#                b.update()
#
#        con_background.fill(colors['green'])
#
#        b.draw_convinced(con_background)
#        screen.blit(con_background, (0, 0))
#        pygame.display.flip()
#
#
