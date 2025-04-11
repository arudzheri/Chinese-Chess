import pygame
from pieces import Piece
from board import draw_board

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = [[None for _ in range(9)] for _ in range(10)]
        self.pieces = []
        self.selected_piece = None
        self.turn = "red"  # "red" or "black"
        self.setup_pieces()

        # Setup pieces here
        self.setup_pieces()

    def setup_pieces(self):
        self.pieces = [
            Piece("General", "red", (9, 4)),
            Piece("Chariot", "red", (9, 0)), Piece("Chariot", "red", (9, 8)),
            Piece("Cannon", "red", (7, 1)), Piece("Cannon", "red", (7, 7)),
            *[Piece("Soldier", "red", (6, i)) for i in range(0, 9, 2)],

            Piece("General", "black", (0, 4)),
            Piece("Chariot", "black", (0, 0)), Piece("Chariot", "black", (0, 8)),
            Piece("Cannon", "black", (2, 1)), Piece("Cannon", "black", (2, 7)),
            *[Piece("Soldier", "black", (3, i)) for i in range(0, 9, 2)]
        ]

    def draw(self):
        draw_board(self.screen)
        for piece in self.pieces:
            piece.draw(self.screen)
            
        # Highlight selected piece
        if self.selected_piece:
            row, col = self.selected_piece.position
            x = col * 80 + 40
            y = row * 80 + 40
            pygame.draw.circle(self.screen, (0, 255, 0), (x, y), 35, 3)

    def handle_click(self, pos):
        row, col = pos[1] // 80, pos[0] // 80
        clicked_piece = self.get_piece_at((row, col))

        if self.selected_piece:
            if clicked_piece and clicked_piece.color == self.selected_piece.color:
                # Select a different piece from same team
                self.selected_piece = clicked_piece
            else:
                # Move or capture
                if self.valid_move(self.selected_piece, (row, col)):
                    self.move_piece(self.selected_piece, (row, col))
                    self.selected_piece = None
                    self.switch_turn()
        else:
            if clicked_piece and clicked_piece.color == self.turn:
                self.selected_piece = clicked_piece

    def get_piece_at(self, pos):
        for piece in self.pieces:
            if piece.position == pos:
                return piece
        return None

    def move_piece(self, piece, new_pos):
        # Remove enemy piece if present
        enemy = self.get_piece_at(new_pos)
        if enemy:
            self.pieces.remove(enemy)

        piece.position = new_pos

    def valid_move(self, piece, new_pos):
        # Placeholder — we allow any move for now
        return True

    def switch_turn(self):
        self.turn = "black" if self.turn == "red" else "red"
