import pygame 
import sys

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("stopwatch")
white = pygame.Color(255, 255, 255)
screen.fill(white)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
