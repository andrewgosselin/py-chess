import pygame
from chess.constants import * 
from .helpers import *
from pygame import gfxdraw, K_w, K_a, K_d, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_F4, K_p, K_RALT, K_LALT, K_SPACE, MOUSEBUTTONDOWN, QUIT, KEYUP, KEYDOWN, K_TAB, K_v, K_h, K_BACKSPACE, K_q, K_m, K_r
import pygame

class PauseMenu:
    def __init__(self, win):
        self.win = win

    def tick(self):
        self.draw()
        self.input()

    def draw(self):
        pass

    def pause_menu_setup(self, background):
        MENU_TEXT = pygame.font.Font(FONT_LIGHT, int(110 / 1080 * HEIGHT))
        self.win.blit(background, (0, 0))
        background = self.win.copy()
        text_surf, text_rect = text_objects('Pause Menu', MENU_TEXT, colour=WHITE)
        text_rect.center = ((WIDTH // 2), (HEIGHT // 4))
        self.win.blit(text_surf, text_rect)
        pygame.display.update()
        return background


    def pause_menu(self):
        show_mouse()
        paused = True
        background = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
        # background.fill((255, 255, 255, 160))  # for white pause menu
        background.fill((*MATTE_BLACK, 160))     # darken the background
        background = self.pause_menu_setup(background)
        while paused:
            click = False
            pks = pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                alt_f4 = (event.type == KEYDOWN and event.key == K_F4
                        and (pressed_keys[K_LALT] or pressed_keys[K_RALT]))
                if event.type == QUIT or alt_f4: sys.exit()
                elif event.type == KEYDOWN:
                    right_key = event.key == K_RIGHT and not pks[K_d] or event.key == K_d and not pks[K_RIGHT]
                    left_key = event.key == K_LEFT and not pks[K_a] or event.key == K_a and not pks[K_LEFT]
                    if event.key in (pygame.K_ESCAPE, pygame.K_p): paused = False
                    elif event.key == K_m: return 'Main Menu'
                    elif event.key == K_SPACE: return 'Resume'
                    elif event.key == K_q: sys.exit()
                elif event.type == MOUSEBUTTONDOWN: click = True
            if self.button('R E S U M E', button_x_start, HEIGHT * 5 // 13, BUTTON_WIDTH, BUTTON_HEIGHT, click): return 'Resume'
            elif self.button('M A I N  M E N U', button_x_start, HEIGHT * 6 // 13, BUTTON_WIDTH, BUTTON_HEIGHT, click): return 'Main Menu'
            elif self.button('S E T T I N G S', button_x_start, HEIGHT * 7 // 13, BUTTON_WIDTH, BUTTON_HEIGHT, click):
                settings_menu()
                self.pause_menu_setup(background)
            elif self.button('Q U I T  G A M E', button_x_start, HEIGHT * 8 // 13, BUTTON_WIDTH, BUTTON_HEIGHT, click): sys.exit()
        return 'Resume'

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