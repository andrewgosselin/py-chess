import pygame

FPS = 60

WIDTH, HEIGHT = 680, 900
ROWS, COLS = 8, 8
SQUARE_SIZE = 85
BOARD_PADDING_TOP = 110

WHITE = 255, 255, 255
BLACK = 0, 0, 0
MATTE_BLACK = 20, 20, 20
GREEN = 40, 175, 99
RED = 255, 0, 0
YELLOW = 250, 237, 39
DARKGREEN = 0, 128, 0
LIGHTBLUE = 0, 191, 255
GREY = 204, 204, 204
LIGHTGREY = 220, 220, 220
DARKGREY = 169, 169, 169
BLUE = 33, 150, 243
BACKGROUND = 174, 222, 203
FONT_BOLD = '../assets/fonts/OpenSans-SemiBold.ttf'
FONT_REG = '../assets/fonts/OpenSans-Regular.ttf'
FONT_LIGHT = '../assets/fonts/OpenSans-Light.ttf'

PIECE_SPRITE_DIRECTORY = "../assets/chess/pieces/sprites"



BUTTON_WIDTH = int(WIDTH * 0.625 // 3)  # important
BUTTON_HEIGHT = int(HEIGHT * 5 // 81)
button_x_start = (WIDTH - BUTTON_WIDTH) // 2
button_layout_4 = [(button_x_start, HEIGHT * 5 // 13, BUTTON_WIDTH, BUTTON_HEIGHT),
                    (button_x_start, HEIGHT * 6 // 13, BUTTON_WIDTH, BUTTON_HEIGHT),
                    (button_x_start, HEIGHT * 7 // 13, BUTTON_WIDTH, BUTTON_HEIGHT),
                    (button_x_start, HEIGHT * 8 // 13, BUTTON_WIDTH, BUTTON_HEIGHT)]
# you can create your own custom layouts if you have more than one button e.g. 7 // 17
TOGGLE_WIDTH = int(BUTTON_WIDTH * 0.875)
TOGGLE_ADJ = int(BUTTON_WIDTH * 0.075)
SCORE_ANCHOR = WIDTH - 8, -5
