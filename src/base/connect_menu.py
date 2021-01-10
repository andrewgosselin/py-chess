import pygame
from chess.constants import * 
from .helpers import *
import os
import platform
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'
from pygame import gfxdraw, K_w, K_a, K_d, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_F4, K_p, K_RALT, K_LALT, K_SPACE, MOUSEBUTTONDOWN, QUIT, KEYUP, KEYDOWN, K_TAB, K_v, K_h, K_BACKSPACE, K_q, K_m, K_r
import pygame
from chess.game import Game
from base.pause_menu import PauseMenu
from ui.inputbox import InputBox
from ui.button import Button

from networking.client import Network

class ConnectMenu:
    def __init__(self, win, main_menu):
        self.win = win
        self.active = True
        self.main_menu = main_menu
        self.network = None
        self.input_boxes = [
            InputBox(self.win, (WIDTH / 2) - 100, 450, 140, 32, "192.168.1.6"),
            InputBox(self.win, (WIDTH / 2) - 100, 525, 140, 32, "5555")
        ]
        self.buttons = [
            Button(self.win, 'Connect', (WIDTH - BUTTON_WIDTH) // 2, 600, BUTTON_WIDTH, BUTTON_HEIGHT, False, self.click_connect, "")
        ]

    def tick(self):
        if self.active == True:
            self.draw()
            for button in self.buttons:
                button.tick()
            for inputbox in self.input_boxes:
                inputbox.tick()
        pygame.display.update()


    def draw(self):
        MENU_TEXT = pygame.font.Font(FONT_LIGHT, int(110 / 1080 * HEIGHT))
        LARGE_TEXT = pygame.font.Font(FONT_REG, int(40 / 1080 * HEIGHT))
        MEDIUM_TEXT = pygame.font.Font(FONT_LIGHT, int(35 / 1440 * HEIGHT))
        SMALL_TEXT = pygame.font.Font(FONT_BOLD, int(25 / 1440 * HEIGHT))
        HUD_TEXT = pygame.font.Font(FONT_REG, int(40 / 1440 * HEIGHT))
        show_mouse()
        self.win.fill(WHITE)
        pygame.draw.rect(self.win, LIGHTGREY, ((WIDTH / 2) - 200, 300, 400, 400))
        text_surf, text_rect = text_objects('Chess', MENU_TEXT)
        text_rect.center = (int(WIDTH / 2), int(HEIGHT / 4))
        self.win.blit(text_surf, text_rect)
        text_surf1, text_rect1 = text_objects('Online', pygame.font.Font(FONT_LIGHT, 36))
        text_rect1.center = (int(WIDTH / 2), int(HEIGHT / 2) - 75)
        self.win.blit(text_surf1, text_rect1)
        text_surf, text_rect = text_objects(f'v{1.0}', SMALL_TEXT)
        text_rect.center = (int(WIDTH * 0.98), int(HEIGHT * 0.98))
        self.win.blit(text_surf, text_rect)
        # text_surf, text_rect = text_objects('Created by AUTHOR', LARGE_TEXT)
        text_rect.center = (int(WIDTH / 2), int(HEIGHT * 0.84))
        # self.win.blit(text_surf, text_rect)

        text_surf2, text_rect2 = text_objects('IP', pygame.font.Font(FONT_LIGHT, 18))
        text_rect2.center = (int(WIDTH / 2), 435)
        self.win.blit(text_surf2, text_rect2)

        
        text_surf2, text_rect2 = text_objects('Port', pygame.font.Font(FONT_LIGHT, 18))
        text_rect2.center = (int(WIDTH / 2), 505)
        self.win.blit(text_surf2, text_rect2)

    def input(self):
        pass

    def click_connect(self):
        self.network = Network()
        self.main_menu.start_game(True, self.network)
        
