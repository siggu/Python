import pygame

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

sky_img = pygame.image.load('Background.png')
sky = pygame.transform.scale(sky_img, (400, 300))

ground_img = pygame.image.load('Ground.png')
ground = pygame.transform.scale(ground_img, (400, 150))

castle_img = pygame.image.load('castle.png')
castle = pygame.transform.scale(castle_img, (200, 150))

heart_img = pygame.image.load('heart.png')
heart = pygame.transform.scale(heart_img, (50, 50))

player_images = ['Player_Attack_R.png', 'Player_Attack_L.png']
player_img = pygame.image.load(player_images[0])

def runGame():
    global done
    global player_img
    bounce = False

    player_x = 100
    player_y = 250
    to_x = 5
    to_y = -18
    
    while not done:
        clock.tick(10)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x -= 10
                    to_x = -5
                    player_img = pygame.image.load(player_images[1])
                elif event.key == pygame.K_RIGHT:
                    player_x += 10
                    to_x = 5
                    player_img = pygame.image.load(player_images[0])
                elif event.key == pygame.K_SPACE and bounce == False:
                    bounce = True
                    bounce_count = 0

        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))
        screen.blit(castle, (200, 150))
        screen.blit(heart, (0, 0))

        if bounce == True:
            player_x += to_x
            player_y += (to_y + 0.5)
            if player_y <= 200 or player_y > 250:
                if player_y >= 250:
                    player_y = 250
                to_y = to_y * (-1)
                bounce_count += 1
            if player_x <= 0 or player_x >= size[0]:
                to_x = to_x * (-1)
            if bounce_count >=2:
                bounce = False
                
        player = pygame.transform.scale(player_img, (50, 50))
        screen.blit(player, (player_x, player_y))
        
        pygame.display.update()

runGame()
