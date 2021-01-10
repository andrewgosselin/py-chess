import pygame
from chess.constants import * 
import os
import platform
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'
from pygame import gfxdraw, K_w, K_a, K_d, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_F4, K_p, K_RALT, K_LALT, K_SPACE, MOUSEBUTTONDOWN, QUIT, KEYUP, KEYDOWN, K_TAB, K_v, K_h, K_BACKSPACE, K_q, K_m, K_r
import pygame


class Button:
    def __init__(self, win, text, x, y, w, h, click, click_function, click_argument, inactive_colour=BLUE, active_colour=LIGHTBLUE, text_colour=WHITE):
        self.win = win
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.click = click
        self.click_function = click_function
        self.click_argument = click_argument
        self.inactive_colour = inactive_colour
        self.active_colour = active_colour
        self.text_colour = text_colour
        self.clicked = False

    def tick(self):
        self.draw()
        self.input()
        if self.clicked:
            self.click_function()

    def draw(self):
        MENU_TEXT = pygame.font.Font(FONT_LIGHT, int(110 / 1080 * HEIGHT))
        LARGE_TEXT = pygame.font.Font(FONT_REG, int(40 / 1080 * HEIGHT))
        MEDIUM_TEXT = pygame.font.Font(FONT_LIGHT, int(35 / 1440 * HEIGHT))
        SMALL_TEXT = pygame.font.Font(FONT_BOLD, int(25 / 1440 * HEIGHT))
        HUD_TEXT = pygame.font.Font(FONT_REG, int(40 / 1440 * HEIGHT))
        mouse = pygame.mouse.get_pos()
        self.clicked = False
        if self.x < mouse[0] < self.x + self.w and self.y < mouse[1] < self.y + self.h:  # if mouse is hovering the button
            pygame.draw.rect(self.win, self.active_colour, (self.x, self.y, self.w, self.h))
        else: pygame.draw.rect(self.win, self.inactive_colour, (self.x, self.y, self.w, self.h))
        text_surf, text_rect = text_objects(self.text, SMALL_TEXT, colour=self.text_colour)
        text_rect.center = (int(self.x + self.w / 2), int(self.y + self.h / 2))
        self.win.blit(text_surf, text_rect)
        

    def input(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN: self.clicked = True