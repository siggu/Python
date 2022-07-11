import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

large_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
clock = pygame.time.Clock()

def runGame():
    done = False

    score = 0
    missed = 0
    SUCCESS = 1
    FAILURE = 2
    game_over = 0
    
    bricks = []
    bricks_x = 8
    bricks_y = 7

    ball = pygame.Rect(screen_width // 2 - 16 // 2, screen_height // 2 - 16, 16, 16)
    ball_dx = 5
    ball_dy = -5

    bar = pygame.Rect(screen_width // 2 - 80 // 2, screen_height - 16, 80, 16)
    bar_dx = 0

    for x_index in range(bricks_x):
        for y_index in range(bricks_y):
            brick = pygame.Rect(x_index * (60 + 10) + 35, y_index * (16 + 5) + 35, 60, 16)
            bricks.append(brick)

    

    while not done:
        clock.tick(60)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    bar_dx = -5
                elif event.key == pygame.K_RIGHT:
                    bar_dx = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    bar_dx = 0
                elif event.key == pygame.K_RIGHT:
                    bar_dx = 0

        bar.left += bar_dx

        ball.left += ball_dx
        ball.top += ball_dy

        if ball.left <= 0:
            ball.left = 0
            ball_dx = -ball_dx
        elif ball.left >= screen_width - ball.width:
            ball.left = screen_width - ball.width
            ball_dx = -ball_dx
        if ball.top < 0:
            ball.top = 0
            ball_dy = -ball_dy
        elif ball.top >= screen_height:
            missed += 1
            ball.left = screen_width // 2 - ball.width // 2
            ball.top = screen_height // 2 - ball.width // 2
            ball_dy = -ball_dy

        if missed >= 3:
            game_over = FAILURE

        if bar.left < 0:
            bar.left = 0
        elif bar.left > screen_width - bar.width:
            bar.left = screen_width - bar.width

        for brick in bricks:
            if ball.colliderect(brick):
                bricks.remove(brick)
                ball_dy = -ball_dy
                score += 1
                break

        if ball.colliderect(bar):
            ball_dy = -ball_dy
            if ball.centerx <= bar.left or ball.centerx > bar.right:
                ball_dx = ball_dx * -1

        if len(bricks) == 0:
            print('success')
            game_over = SUCCESS

        for brick in bricks:
            pygame.draw.rect(screen, green, brick)

        if game_over == 0:
            pygame.draw.circle(screen, black, (ball.centerx, ball.centery), ball.width // 2)

        pygame.draw.rect(screen, (255, 255, 0), bar)

        score_image = small_font.render('Point {}'.format(missed), True, red)
        screen.blit(score_image, (10, 10))

        missed_image = small_font.render('Missed {}'.format(missed), True, red)
        screen.blit(missed_image, missed_image.get_rect(right=screen_width - 10, top = 10))

        if game_over > 0:
            if game_over == SUCCESS:
                success_image = large_font.render('성공', True, blue)
                screen.blit(success_image, success_image.get_rect(centerx = screen_width // 2, centery = screen_height // 2))
            elif game_over == FAILURE:
                failure_image = large_font.render('실패', True, blue)
                screen.blit(failure_image, failure_image.get_rect(centerx = screen_width // 2, centery = screen_height // 2))

        pygame.display.update()
runGame()
pygame.quit()
