import sys
import pygame
from pygame.locals import *
import random
from ca import Agent, Board

colors = {'orange': (255, 102, 0),
          'teal': (0, 128, 128),
          'white': (255, 255, 255),
          'light_gray': (220, 220, 220),
          'green': (0, 220, 0),
          }


class PowerAgent(Agent):
    def __init__(self, pos=(0,0), board_width=8, power=0.0, desired_power=0.0):
        Agent.__init__(self,pos=pos, board_width=board_width)
        self.power = power
        self.desired_power = desired_power
        self.is_happy = False

    def update_happiness(self, board):
        # nbrs should be a list of nbr agents
        nbr_coords = board.get_neighbor_coords(self.pos)
        nbr_power = sum([board[nbr].power for nbr in nbr_coords])
        cur_ratio = nbr_power / self.power

        # TODO REFINE THIS
        if cur_ratio <= self.desired_power:
            self.is_happy = True
        else:
            self.is_happy = False

    def draw(self, surface):
        self.col = colors['orange'] if self.is_happy else colors['teal']
        super(PowerAgent, self).draw(surface)

class PowerBoard(Board):
    def __init__(self, width, height, state):
        Board.__init__(self, width, height, state)
        self.cell_radius = 400 / self.width
        self.unhappy_agents = []
        self.empty_color = colors['green']
        self.update_happiness()

    @property
    def power(self):
        tot_power = 0.0
        for agent in self.values():
            if agent:
                tot_power += agent.power
        return tot_power

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


    def draw(self, surface):
        super(PowerBoard, self).draw(surface)

    def update(self):
        self.move_someone()
        self.update_happiness()

    def update_happiness(self):
        # move an unhappy agent and update all agents happinesses
        self.unhappy_agents = []
        for agent in self.values():
            if agent:
                agent.update_happiness(self)
                if agent.is_happy == False:
                    self.unhappy_agents.append(agent)

    def move_someone(self):
        # TODO SHOULD CLEAN THIS UP
        if self.unhappy_agents:
            agent = random.choice(self.unhappy_agents)
            old_pos = agent.pos
            del self[old_pos]
            did_move, counter = False, 0

            while counter < (self.width*self.height) // 3:
                counter += 1
                new_pos = (random.randint(0, self.width-1), random.randint(0, self.height-1))
                if new_pos not in self or self[new_pos] is None:
                    agent.pos = new_pos
                    agent.update(self)
                    if agent.is_happy:
                        self[new_pos] = agent
                        did_move = True
                        break
            if did_move == False:
                agent.pos = old_pos
                agent.update(self)
                self[old_pos] = agent

n = 13
empty_board = {}
for i in range(n):
    for j in range(n):
        r1 = random.randint(0,2)
        if r1 == 0:
            r2 = (random.random() * 4)
            r3 = (random.random() * 4)
            # empty_board[i,j] = PowertAgent((i,j), n, r2, r3)

b = PowerBoard(n, n, empty_board)
print (len(b))

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Cellular Automata')

# Fill background
hap_background = pygame.Surface(screen.get_size())
hap_background = hap_background.convert()
hap_background.fill(colors['green'])

power_background = pygame.Surface(screen.get_size())
power_background = power_background.convert()
power_background.fill(colors['green'])

# blit to screen
screen.blit(hap_background, (0, 0))
pygame.display.flip()

UPDATE_BOARD = USEREVENT + 1
pygame.time.set_timer(UPDATE_BOARD, 100)

cycle = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            # return
        elif event.type == pygame.KEYUP:
            if event.key == 32:
                continue
                cycle = cycle + 1
                print ("Cycle: %d" % cycle)
                b.update()
        elif event.type == UPDATE_BOARD:
            # continue
            cycle = cycle + 1
            print ("Cycle: %d, %f" % (cycle, b.power))
            b.update()

    b.draw(hap_background)
    screen.blit(hap_background, (0, 0))
    pygame.display.flip()
