import pygame

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

size = [500, 500]
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
            

        sky = pygame.image.load('Background.png')
        sky = pygame.transform.scale(sky, (500, 430))
        screen.blit(sky, (0, 0))

        ground = pygame.image.load('Ground.png')
        ground = pygame.transform.scale(ground, (500, 200))
        screen.blit(ground, (0, 400))

        castle = pygame.image.load('castle.png')
        castle = pygame.transform.scale(castle, (300, 250))
        screen.blit(castle, (200, 150))

        heart = pygame.image.load('heart.png')
        heart = pygame.transform.scale(heart, (50, 50))
        screen.blit(heart, (0, 0))

        player = pygame.image.load('Player_Attack_R.png')
        player = pygame.transform.scale(player, (50, 70))
        screen.blit(player, (100, 330))
        
        pygame.display.update()

runGame()
