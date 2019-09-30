import pygame
pygame.init()

window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)

class Player1:
    def __init__(self, x, y, up, down):
        self.x = x
        self.y = y
        self.up = up
        self.down = down
        self.rect = pygame.Rect(self.x, self.y, 40, 100)


    def draw(self):
        # self.rect.dr
        pygame.draw.rect(window, (255, 255, 255), self.rect)
        pygame.display.update()

    def move(self, velo):
        keys = pygame.key.get_pressed()
        if keys[self.up]:
            self.y -= velo
        if keys[self.down]:
            self.y += velo
        self.rect =  pygame.Rect(self.x, self.y, 40, 100)


class Ball:
    def __init__(self, x, y, xvel, yvel):
        self.position = [x,y]
        self.velocity = [xvel, yvel]


    def draw(self):
        pygame.draw.rect(window, (255, 255, 255), (self.position[0], self.position[1], 20, 20))
        pygame.display.update()

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]



p1 = Player1(100, 360, pygame.K_w, pygame.K_s)
p2 = Player1(1180, 360, pygame.K_UP, pygame.K_DOWN)
ball = Ball(640,360,20,20)
run = True
while run:
    window.fill((0, 0, 0))
    pygame.time.delay(35)
    p1.draw()
    p1.move(20)
    p2.draw()
    p2.move(20)
    ball.draw()
    ball.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()


# import pygame
# pygame.init()
#
# window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
# # onscreen = pygame.Rect(0, 0, 1280, 720)
#
# class Player1:
#     def __init__(self, x, y, up, down):
#         self.x = x
#         self.y = y
#         self.up = up
#         self.down = down
#         self.rect = pygame.Rect(self.x, self.y, 40, 100)
#
#     def draw(self):
#         pygame.draw.rect(window, (255, 255, 255), self.rect)
#         pygame.display.update()
#
#     def move(self, velo):
#         keys = pygame.key.get_pressed()
#         if keys[self.up]:
#             self.y -= velo
#         if keys[self.down]:
#             self.y += velo
#
#
# class Ball:
#     def __init__(self, x, y, xvel, yvel):
#         self.position = [x,y]
#         self.velocity = [xvel, yvel]
#
#
#     def draw(self):
#         pygame.draw.rect(window, (255, 255, 255), (self.position[0], self.position[1], 20, 20))
#         pygame.display.update()
#
#     def move(self):
#         self.position[0] += self.velocity[0]
#         self.position[1] += self.velocity[1]
#
#
#
# p1 = Player1(100, 360, pygame.K_w, pygame.K_s)
# p2 = Player1(1180, 360, pygame.K_UP, pygame.K_DOWN)
# ball = Ball(640,360,20,20)
# run = True
# while run:
#     window.fill((0, 0, 0))
#     pygame.time.delay(35)
#     p1.draw()
#     p1.move(20)
#     p2.draw()
#     p2.move(20)
#     # ball.draw()
#     # ball.move()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#
#             run = False
#
# pygame.quit()
#





