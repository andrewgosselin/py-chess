from chess.constants import * 

def text_objects(text, font, colour=BLACK):
    text_surface = font.render(text, True, colour)
    return text_surface, text_surface.get_rect()

def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)


def toggle_btn(text, x, y, w, h, click, text_colour=BLACK, enabled=True, draw_toggle=True, blit_text=True,
               enabled_color=LIGHTBLUE, disabled_color=GREY):
    mouse = pygame.mouse.get_pos()
    # draw_toggle and blit_text are used to reduce redundant drawing and blitting (improves quality)
    rect_height = h // 2
    if rect_height % 2 == 0: rect_height += 1
    if enabled and draw_toggle:
        pygame.draw.rect(SCREEN, WHITE, (x + TOGGLE_WIDTH - h // 4, y, TOGGLE_ADJ + h, rect_height))
        pygame.draw.rect(SCREEN, enabled_color, (x + TOGGLE_WIDTH, y, TOGGLE_ADJ, rect_height))
        draw_circle(SCREEN, int(x + TOGGLE_WIDTH), y + h // 4, h // 4, enabled_color)
        draw_circle(SCREEN, int(x + TOGGLE_WIDTH + TOGGLE_ADJ), y + h // 4, h // 4, enabled_color)
        draw_circle(SCREEN, int(x + TOGGLE_WIDTH + TOGGLE_ADJ), y + h // 4, h // 5, WHITE)  # small inner circle
    elif draw_toggle:
        pygame.draw.rect(SCREEN, WHITE, (x + TOGGLE_WIDTH - h // 4, y, TOGGLE_ADJ + h, rect_height))
        pygame.draw.rect(SCREEN, disabled_color, (x + TOGGLE_WIDTH, y, TOGGLE_ADJ, rect_height))
        draw_circle(SCREEN, int(x + TOGGLE_WIDTH), y + h // 4, h // 4, disabled_color)
        draw_circle(SCREEN, int(x + TOGGLE_WIDTH + TOGGLE_ADJ), y + h // 4, h // 4, disabled_color)
        draw_circle(SCREEN, int(x + TOGGLE_WIDTH), y + h // 4, h // 5, WHITE)  # small inner circle
    if blit_text:
        text_surf, text_rect = text_objects(text, MEDIUM_TEXT, colour=text_colour)
        text_rect.topleft = (x, y)
        SCREEN.blit(text_surf, text_rect)
    return x < mouse[0] < x + w and y < mouse[1] < y + h and click and pygame.time.get_ticks() > 100

def show_mouse():
    pass