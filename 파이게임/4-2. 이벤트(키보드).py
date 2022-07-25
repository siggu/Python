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
    draw_circle = False
    x = 250
    y = 250
    while not done:
        clock.tick(10)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_DOWN:        # y 좌표는 위에서 아래로 커지기 때문에 키 다운을 하면 + 를 해줘야 한다.
                y += 10
            elif event.key == pygame.K_UP:             # y 좌표는 위에서 아래로 커지기 때문에 키 업을 하면 - 를 해줘야 한다.
                y -= 10

        pygame.draw.circle(screen, blue, (x, y), 5)
        
        pygame.display.update()

runGame()
