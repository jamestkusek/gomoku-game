import pygame

GRID_SIZE = 15
CELL_SIZE = 50
Y_OFFSET = 20
X_OFFSET = 10
LINE_THICKNESS = 2
PIECE_RADIUS = 20
X_MARGIN = 20
Y_MARGIN = 50
BOARD_COLOR = (235,200,138)
BOARD_COLOR_TRANSLUCENT = (235,200,138,100)
LINE_COLOR = (255,255,255)

width = GRID_SIZE * CELL_SIZE
height = GRID_SIZE * CELL_SIZE

cells = [[(0,0,0)] * GRID_SIZE for x in range(GRID_SIZE)]

index = 0
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        cells[x][y] = ((y * (CELL_SIZE) + X_OFFSET),(x * (CELL_SIZE) + Y_OFFSET), index)
        index += 1

pygame.init()
screen = pygame.display.set_mode((width + X_MARGIN, height + Y_MARGIN))


def draw_game_board():
    screen.fill(BOARD_COLOR)
    for x in range(GRID_SIZE + 1):
        pygame.draw.rect(screen,LINE_COLOR,(X_OFFSET, x * CELL_SIZE + Y_OFFSET, width + LINE_THICKNESS, LINE_THICKNESS)) #horizontal grid lines
        pygame.draw.rect(screen, LINE_COLOR,(x * CELL_SIZE + X_OFFSET, Y_OFFSET, LINE_THICKNESS, width + LINE_THICKNESS))  # vertical grid lines
    pygame.display.update()


def mouse_in_grid(pos):
    if pos[0] in range(X_OFFSET, X_OFFSET + width) and pos[1] in range (Y_OFFSET, Y_OFFSET + height):
        return True
    else:
        return False


def find_cell(pos):
    cell_found = False
    for row in cells:
        for node in row:
            x = node[0]
            y = node[1]

            if pos[0] in range(x, x + CELL_SIZE) and pos[1] in range(y, y + CELL_SIZE):
                cell_found = True
                cell_id = node[2]
                return cell_id
        if cell_found:
            break
    

def update_cell(player, cell_id):
    column = (cell_id % (GRID_SIZE))
    row = cell_id // GRID_SIZE
    colour = (50,50,50)
    if player == 2:
        colour =  (255,255,255)
    x_center = cells[row][column][0] + ((CELL_SIZE + LINE_THICKNESS) // 2)
    y_center = cells[row][column][1] + ((CELL_SIZE + LINE_THICKNESS) // 2)
    pygame.draw.circle(screen,colour,(x_center,y_center),PIECE_RADIUS)
    pygame.display.update()

def end_game_menu():
    screen.fill(BOARD_COLOR_TRANSLUCENT)
    pygame.display.update()




