import pygame
import random

pygame.init()



WHITE = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        ############################
        # 여기에 도형을 그리세요
        ############################
        
        
        pygame.display.update()

runGame()
