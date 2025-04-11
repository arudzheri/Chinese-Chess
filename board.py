import pygame

ROWS, COLS = 10, 9
CELL_SIZE = 80

def draw_board(screen):
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            pygame.draw.rect(screen, (0, 0, 0), (x, y, CELL_SIZE, CELL_SIZE), 1)

    # Draw river
    font = pygame.font.SysFont("simhei", 40)
    text = font.render("楚河    汉界", True, (0, 0, 0))
    screen.blit(text, (CELL_SIZE * 2.5, CELL_SIZE * 4.3))
