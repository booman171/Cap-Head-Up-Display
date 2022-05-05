import pygame

pygame.font.init()

# UI Colors
color_light_blue = pygame.Color(55, 156, 199)
color_dark_blue = pygame.Color(1, 60, 113)
color_darkest = pygame.Color(9, 9, 36)
color_red_dark = pygame.Color(255, 0, 0)
color_red_light = pygame.Color(255, 155, 155)
color_green = pygame.Color(10, 222, 10)
color_red = pygame.Color(255, 0, 0)
color_black = pygame.Color(0, 0, 0)
color_white = pygame.Color(255, 255, 255)
color_yellow = pygame.Color(255, 255, 0)
color_blue = pygame.Color(0, 0, 255)
color_magenta = pygame.Color(255, 0, 255)
color_teal = pygame.Color(0, 128, 128)
color_gray = pygame.Color(128, 128, 128)
color_orange = pygame.Color(255, 140, 0)
color_save =  color_light_blue
color_dark_green = pygame.Color(7, 51, 18)

# Fonts
largeFont = pygame.font.SysFont("roboto", 70, bold=True)
medFont = pygame.font.SysFont("roboto", 35, bold=True)
smallFont = pygame.font.SysFont("roboto", 25)

# Text
cal_text_color = color_green
calc_row1 =  largeFont.render("(         )        <      AC", False, cal_text_color)
calc_row2 =  largeFont.render("7        8        9        /", False, cal_text_color)
calc_row3 =  largeFont.render("4        5        6        x", False, cal_text_color)
calc_row4 =  largeFont.render("1        2        3         -", False, cal_text_color)
calc_row5 =  largeFont.render("0        .         =        +", False, cal_text_color)

row1_pos = (35, 70)
row2_pos = (35, 105)
row3_pos = (35, 140)
row4_pos = (35, 175)
row5_pos = (35, 210)


