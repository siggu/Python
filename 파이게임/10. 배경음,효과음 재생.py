import pygame
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
clock = pygame.time.Clock()

def runGame():
    global done

    sound_image = pygame.image.load('sound_on.png')
    sound_image = pygame.transform.scale(sound_image, (40, 40))

    sound_rect = pygame.Rect(sound_image.get_rect())
    sound_rect.left = (screen_width - 40) / 2
    sound_rect.top = 10

    sound = pygame.mixer.Sound("gameover.wav")
    is_play = 0

    while not done:
        clock.tick(10)
        screen.fill(white)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos[0], event.pos[1])
                if sound_rect.collidepoint(event.pos) == True:
                    is_play = 1

        screen.blit(sound_image, sound_rect)

        if is_play == 1:
            print("play..")
            is_play = 0
            sound.play()

        pygame.display.update()
runGame()
pygame.quit()
