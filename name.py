import pygame
from math import sin, pi
from itertools import cycle

# Define colors
WHITE = (255 , 255 , 255)
BLACK = (0,0,0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

WIDTH = 800
HEIGHT = 600 

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def bounce(progress):
    return HEIGHT // 2 + 50 * sin(2 * pi * progress)

FPS = 60 
DURATION = 5 
FRAMES = FPS * DURATION

clock = pygame.time.Clock()
frame = 0

font = pygame.font.Font(None, 50)
name = "Bilal Arshad"
letters = [font.render(char, True, color) for char, color in zip(name, cycle(COLORS))]

while frame <= FRAMES:
    screen.fill(BLACK)
    clock.tick(FPS)

    for i, letter in enumerate(letters):
        progress = frame/FRAMES + i / len(letters) / FRAMES 
        pos = (50 * i + WIDTH // 2 - 50 * len(letters) // 2, bounce(progress))
        screen.blit(letter, letter.get_rect(center=pos))

    frame +=1
    pygame.display.flip()