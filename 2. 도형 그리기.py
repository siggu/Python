import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
size = [500, 600]
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

        # 1) 사각형
        pygame.draw.rect(screen, green, (50, 200, 40, 20)) # where, color, (start x, start y, width(너비), height(높이))
        pygame.draw.rect(screen, (0, 255, 0), (0, 0, 200, 100), 1) # 테두리만 남김

        # 2) 원
        pygame.draw.circle(screen, red, (300, 100), 30) # where, color, 중심좌표(x, y), radius(반지름)
        pygame.draw.circle(screen, (255, 0, 0), (300, 200),30,1)
        pygame.draw.circle(screen, (255, 0, 0), (360, 200),30,2)
        pygame.draw.circle(screen, (255, 0, 0), (420, 200),30,3) # 테두리 조절

        # 3) 선
        pygame.draw.line(screen, blue, (0,0), (200, 300), 3) # where, color, (start x, start y), (end x, end y), thickness
        pygame.draw.line(screen, blue, (0,0), (200, 0))
        pygame.draw.line(screen, blue, (0, 20), (200, 20), 3)
        pygame.draw.line(screen, blue, (0, 40), (200, 40), 6)
        
        pygame.display.update()
runGame()
pygame.quit()
