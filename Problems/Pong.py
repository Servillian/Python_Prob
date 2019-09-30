import pygame
from pygame.locals import *


class App:
    def __init__(self):
        self._run = True
        self._display_surf = None
        self.ball = None
        self.paddle = None

    def on_init(self):
        pygame.init()

        self._display_surf = pygame.display.set_mode((1024, 768), pygame.HWSURFACE)
        self._run = True
        self.ball = Ball()
        self.paddle = Paddle()
        self._display_surf.fill((0, 0, 0))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.ball.updatePosition(0, 20)
            if event.key == pygame.K_UP:
                self.ball.updatePosition(0, -20)



class Paddle:
    def __init__(self):
        self.position = [420, 360]
        self.image_surf = pygame.image.load("paddle.png").convert()
    def updatePosition(self, x, y):
        self.position = [self.position[0] + x, self.position[1] + y]
    def draw(self, _display_surf):
        _display_surf.blit(self._image_surf, self.position)


class Ball:
    def __init__(self):
        self.position = [0,0]
        self.velocity = [0,0]
        self._image_surf = pygame.image.load("ball.png").convert()
    def updatePosition(self, x, y):
        self.position = [self.position[0]+x, self.position[1]+y]
    def draw(self, _display_surf):
        _display_surf.blit(self._image_surf, self.position)


