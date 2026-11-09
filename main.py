import pygame
from config import *
from persbody import *

pygame.init()

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Labirint game")

# iz qoladigan ekran
trail = pygame.Surface((window_width, window_height), pygame.SRCALPHA)


clock = pygame.time.Clock()


personaj = Persbody(50, 50, perx, pery, percolor)


running = True
FPS = 60


# oyinni tugatadi
game_over = False

# harakat timeri
move_timer = 0
move_delay = 120

# qadamini sanash
step_count = 0


# qayta boshlash funksiyasi
def reset_game():
    
    global personaj, game_over

    personaj = Persbody(50, 50, perx, pery, percolor)
    game_over = False
    move_timer = 0
    trail.fill(0, 0, 0, 0)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.KEYDOWN:

            # oyinni qayta boshlash
            if game_over:
                if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
                    reset_game()

            else:
                if event.key == pygame.K_d:
                    personaj.change_direction("RIGHT")

                elif event.key == pygame.K_a:
                    personaj.change_direction("LEFT")

                elif event.key == pygame.K_w:
                    personaj.change_direction("UP")

                elif event.key == pygame.K_s:
                    personaj.change_direction("DOWN")


    # chekalarni devor bilan tosish
    if personaj.rect.x >= window_width:
        game_over = True
    elif personaj.rect.x < 0:
        game_over = True

    if personaj.rect.y >= window_height:
        game_over = True
    elif personaj.rect.y < 0:
        game_over = True



    # harakat qildiradigan qismi

    if not game_over:
        move_timer += clock.get_time()

        if move_timer >= move_delay:
            personaj.move()






            move_timer = 0


    # ekran chizish qismi
    screen.fill(menu_bg_color)

    # eski izlarni sekin o'chirish
    trail.fill((0, 0, 0, 5), special_flags=pygame.BLEND_RGBA_SUB)

    # yangi iz qoldirish
    pygame.draw.rect(trail, (*pygame.Color("#797979")[:3], 255),
                     personaj.rect, border_radius=4)

    screen.blit(trail, (0, 0))

    # personajni chizish
    personaj.draw(screen)

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()