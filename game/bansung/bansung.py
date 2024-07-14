from __future__ import division
import pygame
import random
from os import path

## thư mục tài nguyên
img_dir = path.join(path.dirname(__file__), 'assets')
sound_folder = path.join(path.dirname(__file__),'sounds')

## đặt trong constant.py sau này
WIDTH =480  # chiều rộng của sổ
HEIGHT = 600 #chiều cao
FPS= 60 #tốc độ khung hình/s
POWER_TIME = 5000 #tg hiển thị power up
BAR_LENGTH =100  #độ dài thanh bảo vệ
BAR_HEIGHT =10  #chiều cao thanh bv

# màu

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
YELLOW=(255,255,0)
BLUE= (0,0,255)

def draw_text(surf, text, size,x,y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x , y)
    surf.blit(text_surface, text_rect)

pygame.init()
pygame.mixer.init()  #sound
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game bắn nhau =))")
clock=pygame.time.Clock()  #đồng bộ fps


font_name = pygame.font.match_font('arial')


def main_menu():
    global screen

    menu_song= pygame.mixer.music.load(path.join(sound_folder, "menu.ogg"))
    pygame.mixer.music.play(-1)

    title= pygame.image.load(path.join(img_dir, "main.png")).convert()
    title= pygame.transform.scale(title, (WIDTH,HEIGHT), screen)

    screen.blit(title, (0,0))
    pygame.display.update()
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.type == pygame.K_q:
                pygame.quit()
                quit()
            else:
                draw_text(screen,"Nhấn enter để chơi",30,WIDTH/2,HEIGHT/2)
                draw_text(screen,"Q để thoát",30,WIDTH/2, (HEIGHT/2)+40)
                pygame.display.update()

    ready= pygame.mixer.Sound(path.join(sound_folder,'getready.ogg'))
    ready.play()
    screen.fill(BLACK)
    draw_text(screen, "Chuẩn bị",40,WIDTH/2,HEIGHT/2)
    pygame.display.update()

    