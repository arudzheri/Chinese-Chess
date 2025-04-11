import pygame

CELL_SIZE = 80

# Chinese piece characters
PIECE_SYMBOLS = {
    "General": {"red": "帥", "black": "將"},
    "Advisor": {"red": "仕", "black": "士"},
    "Elephant": {"red": "相", "black": "象"},
    "Horse": {"red": "傌", "black": "馬"},
    "Chariot": {"red": "俥", "black": "車"},
    "Cannon": {"red": "炮", "black": "砲"},
    "Soldier": {"red": "兵", "black": "卒"}
}

class Piece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color  # 'red' or 'black'
        self.position = position  # (row, col)

    def draw(self, screen):
        row, col = self.position
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        radius = 30

        # Draw piece circle
        pygame.draw.circle(screen, (255, 230, 200), (x, y), radius)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), radius, 2)

        # Draw symbol
        font = pygame.font.SysFont("simhei", 32)
        symbol = PIECE_SYMBOLS[self.name][self.color]
        color = (200, 0, 0) if self.color == "red" else (0, 0, 0)
        text = font.render(symbol, True, color)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

    def valid_moves(self, piece, new_pos):
        valid = piece.valid_moves(self.board)
        return new_pos in valid
        
        moves = []
        row, col = self.position

        if self.name == "Soldier":
            if self.color == "red":
                # Move forward (up)
                if row > 0:
                    moves.append((row - 1, col))
                # After crossing the river (row <= 4)
                if row <= 4:
                    if col > 0:
                        moves.append((row, col - 1))
                    if col < 8:
                        moves.append((row, col + 1))
            else:  # black
                # Move forward (down)
                if row < 9:
                    moves.append((row + 1, col))
                # After crossing the river (row >= 5)
                if row >= 5:
                    if col > 0:
                        moves.append((row, col - 1))
                    if col < 8:
                        moves.append((row, col + 1))

        return moves
