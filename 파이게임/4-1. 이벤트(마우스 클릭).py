import pygame

pygame.init()

white = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    global done
    draw_circle = False
    while not done:
        clock.tick(10)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # 마우스의 클릭 위치에 점 찍기
            if event.type == pygame.MOUSEBUTTONDOWN:
                draw_circle = True
                mousepos = event.pos
                print(mousepos)
                
        if draw_circle == True:
            pos = mousepos
            pygame.draw.circle(screen, (0, 255, 0), (pos[0], pos[1]), 3)
            
        pygame.display.update()
runGame()
