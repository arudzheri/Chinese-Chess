import pygame
import sys
from game import Game

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chinese Chess")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main game loop
def main():
    clock = pygame.time.Clock()
    game = Game(SCREEN)
    running = True

    while running:
        SCREEN.fill(WHITE)
        game.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                game.handle_click(pos)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
