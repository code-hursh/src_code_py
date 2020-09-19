import pygame, sys
from pygame.locals import *

pygame.init()
width, height = 1280, 720
playpad = pygame.display.set_mode((width,height))
pygame.display.set_caption('basic block movement')

class Box:
    def __init__(self, width, height, x, y, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win,self.color,self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.y -= self.vel
        if keys[K_s]:
            self.y += self.vel
        if keys[K_a]:
            self.x -= self.vel
        if keys[K_d]:
            self.x += self.vel

        self.rect = (self.x, self.y, self.width, self.height)

def redrawWindow(win, player):
    win.fill((255,255,255))
    player.move()
    player.draw(win)
    pygame.display.update()

def main():
    running = True
    p = Box(100,100,590,310,(255,255,0))
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        redrawWindow(playpad, p)
    pygame.quit()
    sys.exit()

main()
