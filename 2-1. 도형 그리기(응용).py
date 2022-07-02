import pygame
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

size = [700, 700]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # 4x4 격자무늬 그리기
        pygame.draw.line(screen, red, (0, 0), (80, 0), 3)
        pygame.draw.line(screen, red, (0, 20), (80, 20), 3)
        pygame.draw.line(screen, red, (0, 40), (80, 40), 3)
        pygame.draw.line(screen, red, (0, 60), (80, 60), 3)
        pygame.draw.line(screen, red, (0, 80), (80, 80), 3)
        
        pygame.draw.line(screen, red, (0, 0), (0, 80), 3)
        pygame.draw.line(screen, red, (20, 0), (20, 80), 3)
        pygame.draw.line(screen, red, (40, 0), (40, 80), 3)
        pygame.draw.line(screen, red, (60, 0), (60, 80), 3)
        pygame.draw.line(screen, red, (80, 0), (80, 80), 3)

        # 신호등 만들기
        pygame.draw.line(screen, (0, 0, 0), (100, 100), (250, 100), 1)
        pygame.draw.line(screen, (0, 0, 0), (100, 100), (100, 400), 1)
        pygame.draw.line(screen, (0, 0, 0), (250, 100), (250, 400), 1)
        pygame.draw.line(screen, (0, 0, 0), (100, 400), (250, 400), 1)
        pygame.draw.line(screen, (0, 0, 0), (175, 400), (175, 500), 1)

        pygame.draw.circle(screen, (255, 0, 0), (175, 170), 40)
        pygame.draw.circle(screen, (255, 255, 0), (175, 250), 40)
        pygame.draw.circle(screen, (0, 255, 0), (175, 330), 40)
        
        pygame.display.update()

runGame()
