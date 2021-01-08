import pygame
from chess.constants import * 
from .helpers import *
import os
import platform
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'
from pygame import gfxdraw, K_w, K_a, K_d, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_F4, K_p, K_RALT, K_LALT, K_SPACE, MOUSEBUTTONDOWN, QUIT, KEYUP, KEYDOWN, K_TAB, K_v, K_h, K_BACKSPACE, K_q, K_m, K_r
import pygame
from chess.game import Game

class MainMenu:
    def __init__(self, win):
        self.win = win
        self.input_enabled = False
        self.game_started = False
        self.game = None

    def tick(self):
        if not self.game_started:
            self.draw()
            self.input()
        pygame.display.update()
        

    def draw(self):
        MENU_TEXT = pygame.font.Font(FONT_LIGHT, int(110 / 1080 * HEIGHT))
        LARGE_TEXT = pygame.font.Font(FONT_REG, int(40 / 1080 * HEIGHT))
        MEDIUM_TEXT = pygame.font.Font(FONT_LIGHT, int(35 / 1440 * HEIGHT))
        SMALL_TEXT = pygame.font.Font(FONT_BOLD, int(25 / 1440 * HEIGHT))
        HUD_TEXT = pygame.font.Font(FONT_REG, int(40 / 1440 * HEIGHT))
        show_mouse()
        MENU_TEXT = pygame.font.Font(FONT_LIGHT, int(110 / 1080 * HEIGHT))
        self.win.fill(WHITE)
        text_surf, text_rect = text_objects('Chess', MENU_TEXT)
        text_rect.center = (int(WIDTH / 2), int(HEIGHT / 4))
        self.win.blit(text_surf, text_rect)
        text_surf, text_rect = text_objects(f'v{1.0}', SMALL_TEXT)
        text_rect.center = (int(WIDTH * 0.98), int(HEIGHT * 0.98))
        self.win.blit(text_surf, text_rect)
        # text_surf, text_rect = text_objects('Created by AUTHOR', LARGE_TEXT)
        text_rect.center = (int(WIDTH / 2), int(HEIGHT * 0.84))
        # self.win.blit(text_surf, text_rect)

    

    def toggle_input(toggle):
        self.input_enabled = toggle

    def input(self):
        click = False
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            alt_f4 = (event.type == KEYDOWN and (event.key == K_F4
                      and (pressed_keys[K_LALT] or pressed_keys[K_RALT])
                      or event.key == K_q or event.key == K_ESCAPE))
            if event.type == QUIT or alt_f4: sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE: pass
            elif event.type == KEYDOWN and (event.key == K_v or event.key == K_h): pass
            elif event.type == MOUSEBUTTONDOWN: click = True

        if self.button('O N L I N E', (WIDTH - BUTTON_WIDTH) // 2, HEIGHT * 5 // 13, BUTTON_WIDTH, BUTTON_HEIGHT, click): pass
        elif self.button('O F F L I N E', (WIDTH - BUTTON_WIDTH) // 2, HEIGHT * 6 // 13, BUTTON_WIDTH, BUTTON_HEIGHT, click):
            self.start_game()
        elif self.button('S E T T I N G S', (WIDTH - BUTTON_WIDTH) // 2, HEIGHT * 7 // 13, BUTTON_WIDTH, BUTTON_HEIGHT, click): pass
        elif self.button('Q U I T  G A M E', (WIDTH - BUTTON_WIDTH) // 2, HEIGHT * 8 // 13, BUTTON_WIDTH, BUTTON_HEIGHT, click): pass

    def start_game(self):
        self.game_started = True
        self.game = Game(self.win)

    def button(self, text, x, y, w, h, click, inactive_colour=BLUE, active_colour=LIGHTBLUE, text_colour=WHITE):
        MENU_TEXT = pygame.font.Font(FONT_LIGHT, int(110 / 1080 * HEIGHT))
        LARGE_TEXT = pygame.font.Font(FONT_REG, int(40 / 1080 * HEIGHT))
        MEDIUM_TEXT = pygame.font.Font(FONT_LIGHT, int(35 / 1440 * HEIGHT))
        SMALL_TEXT = pygame.font.Font(FONT_BOLD, int(25 / 1440 * HEIGHT))
        HUD_TEXT = pygame.font.Font(FONT_REG, int(40 / 1440 * HEIGHT))
        mouse = pygame.mouse.get_pos()
        return_value = False
        if x < mouse[0] < x + w and y < mouse[1] < y + h:  # if mouse is hovering the button
            pygame.draw.rect(self.win, active_colour, (x, y, w, h))
            if click and pygame.time.get_ticks() > 100: return_value = True
        else: pygame.draw.rect(self.win, inactive_colour, (x, y, w, h))

        text_surf, text_rect = text_objects(text, SMALL_TEXT, colour=text_colour)
        text_rect.center = (int(x + w / 2), int(y + h / 2))
        self.win.blit(text_surf, text_rect)
        return return_value