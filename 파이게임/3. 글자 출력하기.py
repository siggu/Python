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

        # 영어로 작성
        sysfont = pygame.font.SysFont(None, 30)
        text = sysfont.render("Hello world!", True, (0, 0, 255)) # BLUE = (0, 0, 255) 
        screen.blit(text, (0,0))

        # 한글로 작성(글자가 깨진다면 "malgungothic" 옵션 추가)
        sysfont = pygame.font.SysFont("malgungothic", 26)
        text = sysfont.render("안녕", True, (0, 0, 0))
        screen.blit(text, (100, 100))
        
        pygame.display.update()

runGame()
