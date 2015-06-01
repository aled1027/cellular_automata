import pygame

class Agent(object):
    def __init__(self, pos=(0,0), col=(0,0,0), board_width=8):
        assert(board_width > 0)
        self.pos = pos
        self.radius = 400 // board_width
        self.col = col

    def draw(self, surface):
        rect = (self.pos[0] * self.radius, self.pos[1] * self.radius, self.radius, self.radius)
        pygame.draw.rect(surface, self.col, rect)

# need to switch to an ordered dict
class Board(dict):
    def __init__(self, width, height, state):
        dict.__init__(self, state)
        self.width = width
        self.height = height
        self.empty_color = (255,255,255)
        self.radius = 400 // self.width

    def draw(self, surface):
        for coord, agent in zip(self.keys(), self.values()):
            if agent is None:
                rect = (coord[0] * self.radius, coord[1] * self.radius, self.radius, self.radius)
                pygame.draw.rect(surface, self.empty_color, rect)
            else:
                agent.draw(surface)

