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
    # 이전 좌표를 저장하기 위해 리스트에 저장
    mousepos = []
    while not done:
        clock.tick(10)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                draw_circle = True
                mousepos.append(event.pos)
                print(mousepos)

        if draw_circle == True:
            for pos in mousepos:
                pygame.draw.circle(screen, (0, 255, 0), (pos[0], pos[1]), 4)

        pygame.display.update()

runGame()
