import pygame

pygame.init() 

WHITE = (255,255,255)
BLACK = (0, 0, 0)
size = [400, 300]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    global done

    screen_width = size[0]
    screen_height = size[1]

    bar_width = 9
    bar_height = 50

    bar_x = bar_start_x = 0
    bar_y = bar_start_y = (screen_height - bar_height) / 2

    circle_radius = 9
    circle_diameter = circle_radius * 2

    circle_x = circle_start_x =  screen_width - circle_diameter
    circle_y = circle_start_y =  (screen_width - circle_diameter) / 2

    bar_move = 0
    speed_x, speed_y, speed_bar = -screen_width / 1.28, screen_height / 1.92, screen_height * 1.2

    while not done:
        time_passed = clock.tick(30)
        time_sec = time_passed / 1000.0
        screen.fill(BLACK)

        circle_x += speed_x * time_sec
        circle_y += speed_y * time_sec
        ai_speed = speed_bar * time_sec 
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                done = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bar_move = -ai_speed
                elif event.key == pygame.K_DOWN:
                    bar_move = ai_speed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    bar_move = 0
                elif event.key == pygame.K_DOWN:
                    bar_move = 0

        bar_y += bar_move
    
        if bar_y + bar_height > screen_height:
            bar_y = screen_height - bar_height
        elif bar_y <= 0:
            bar_y = 0

        if circle_x < bar_width: 
            if circle_y >= bar_y - circle_radius and circle_y <= bar_y + bar_height + circle_radius:
                circle_x = bar_width
                speed_x = -speed_x
        if circle_x < -circle_radius:
            circle_x, circle_y = circle_start_x, circle_start_y
            bar_x, bar_y = bar_start_x, bar_start_y
        elif circle_x > screen_width - circle_diameter: 
            speed_x = -speed_x
        if circle_y <= 0: 
            speed_y = -speed_y
            circle_y = 0
        elif circle_y >= screen_height - circle_diameter: 
            speed_y = -speed_y
            circle_y = screen_height - circle_diameter

        pygame.draw.rect(screen, 
                         WHITE, 
                        (bar_x, bar_y, int(bar_width), int(bar_height)))

        pygame.draw.circle(screen, 
                            WHITE, 
                            (int(circle_x), int(circle_y)), 
                            int(circle_radius))
    
        pygame.display.update()

runGame()
pygame.quit()
