import pygame

pygame.init()

white = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)
  
done = False
clock = pygame.time.Clock()

airplane_img = pygame.image.load('plane.png')
airplane = pygame.transform.scale(airplane_img, (60, 40))

def runGame():
    global done
    global airplane
    x = 20
    y = 40

    while not done:
        clock.tick(10)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 10
                elif event.key == pygame.K_DOWN:
                    y += 10
                elif event.key == pygame.K_LEFT:
                    x -= 10
                elif event.key == pygame.K_RIGHT:
                    x += 10

            if x < 0:
                x = 0
            elif x > 400 - 60:
                x = 400 - 60

            if y < 0:
                y = 0
            elif y > 400 - 40:
                y = 400 - 40

        screen.blit(airplane, (x, y))
        pygame.display.update()
        
runGame()
pygame.quit()
