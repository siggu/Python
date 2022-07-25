import pygame
import random

pygame.init()

black = (0, 0, 0)
gray = (128, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

large_font = pygame.font.SysFont("malgungothic", 72)
small_font = pygame.font.SysFont("malgungothic", 36)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
clock = pygame.time.Clock()

cell_size = 50
x_count = screen_width // cell_size
y_count = screen_height // cell_size

grid = [[{'mine' : False, 'open' : False, 'mine_count_around' : 0, 'flag' : False} for _ in range(x_count)] for _ in range(y_count)]
mine_count = 15

for _ in range(mine_count):
    while True:
        x_index = random.randint(0, x_count - 1)
        y_index = random.randint(0, y_count - 1)
        tile = grid[y_index][x_index]
        if not tile['mine']:
            tile['mine'] = True
            break
        
def in_bound(x_index, y_index):
    if(0 <= x_index < x_count and 0 <= y_index < y_count):
        return True
    else:
        return False

def open_tile(x_index, y_index):
    if not in_bound(x_index, y_index):
        return

    tile = grid[y_index][x_index]
    if not tile['open']:
        tile['open'] = True
    else:
        return

    if tile['mine']:
        return

    mine_count_around = get_mine_count_around(x_index, y_index)
    if mine_count_around > 0:
        tile['mine_count_around'] = mine_count_around
    else:
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            x_index_around, y_index_around = (x_index + x, y_index + y)
            open_tile(x_index_around, y_index_around)


def get_mine_count_around(x_index, y_index):
    count = 0

    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        x_index_around, y_index_around = (x_index + x, y_index + y)
        if in_bound(x_index_around, y_index_around) and grid[y_index_around][x_index_around]['mine']:
            count += 1
    return count

def runGame():
    success = 1
    failure = 2
    game_over = 0
    global done

    while not done:
        clock.tick(10)
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_index = event.pos[0] // cell_size
                y_index = event.pos[1] // cell_size
                if event.button == 1:
                    if in_bound(x_index, y_index):
                        tile = grid[y_index][x_index]
                        if tile['mine']:
                            tile['open'] = True
                            game_over = failure
                        else:
                            open_tile(x_index, y_index)
                elif event.button == 3:
                    if in_bound(x_index, y_index):
                        tile = grid[x_index][y_index]
                        if not tile['flag']:
                            tile['flag'] = True
                        else:
                            tile['flag'] = False

                        success = True
                        for x_index in range(x_count):
                            for y_index in range(y_count):
                                tile = grid[x_index][y_index]
                                if tile['mine'] and not tile['flag']:
                                    success = False
                                    break
                        if success:
                            game_over = success

        for x_index in range(x_count):
            for y_index in range(y_count):
                tile = grid[y_index][x_index]
                if tile['mine_count_around']:
                    mine_count_around_image = small_font.render('{}'.format(tile['mine_count_around']), True, blue)
                    screen.blit(mine_count_around_image, mine_count_around_image.get_rect(centerx=x_index * cell_size + cell_size // 2, centery=y_index * cell_size + cell_size // 2))
                if tile['mine']: 
                    mine_image = small_font.render('x', True, red)
                    screen.blit(mine_image, mine_image.get_rect(centerx=x_index * cell_size + cell_size // 2, centery=y_index * cell_size + cell_size // 2))
                if not tile['open']:
                    pygame.draw.rect(screen, gray, pygame.Rect(x_index * cell_size, y_index * cell_size, cell_size, cell_size))
                if tile['flag']: 
                    v_image = small_font.render('v', True, white)
                    screen.blit(v_image, (x_index * cell_size + 10, y_index * cell_size + 10)) 
                pygame.draw.rect(screen, white, pygame.Rect(x_index * cell_size, y_index * cell_size, cell_size, cell_size), 1)

        if game_over > 0:
            if game_over == success:
                success_image = large_font.render('Success', True, red)
                screen.blit(success_image, success_image.get_rect(centerx=screen_width // 2, centery=screen_height // 2))
            elif game_over == failure:
                failure_image = large_font.render('Failure', True, red)
                screen.blit(failure_image, failure_image.get_rect(centerx=screen_width // 2, centery=screen_height // 2))

        pygame.display.update() 

runGame()
pygame.quit() 
