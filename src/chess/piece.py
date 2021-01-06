from .constants import *
class Piece:
    def __init__(self, row, col, color, type):
        self.row = row
        self.col = col
        self.color = color
        self.type = type

        self.x = 0
        self.y = 0

        self.calculatePosition()

    def calculatePosition(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        piece_sprite = pygame.image.load("myimage.bmp")
        pygame.draw.circle()

    def getPossibleMoves(self):
        pass