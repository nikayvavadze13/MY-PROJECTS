import pygame
import os
pygame.font.init()
pygame.mixer.init()

FPS = 60
WIDTH = 900
HEIGHT = 500
VEL = 5
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)



YELLLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
BULLET_VEL = 7



WHITE = (255,255,255)


SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

WINDOW = pygame.display.set_mode((900, 500))
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("python projects","pyGame", "spaceship 1v1",'Assets', 'space.png')), (WIDTH, HEIGHT))
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("python projects","pyGame", "spaceship 1v1","Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("python projects","pyGame", "spaceship 1v1",'Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WINDOW.blit(SPACE, (0,0))
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y ))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    WINDOW.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WINDOW.blit(yellow_health_text, (10, 10))

    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)

    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)

    pygame.draw.rect(WINDOW, (0, 0, 0), BORDER)
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > BORDER.x + 20:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < WIDTH:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_j] and red.x - VEL > 0:
        red.x -= VEL
    if keys_pressed[pygame.K_l] and red.x - VEL < BORDER.x - 60:
        red.x += VEL
    if keys_pressed[pygame.K_k] and red.y + VEL + red.height < HEIGHT - 15:
        red.y += VEL
    if keys_pressed[pygame.K_i] and red.y - VEL > 0:
        red.y -= VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x += BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WINDOW.blit(draw_text, (WIDTH/2 - draw_text.get_width() /2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
    





def main():
    red = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    bullets = pygame.Rect(yellow.x - yellow.width, yellow.y + 23, 10, 5)
                    yellow_bullets.append(bullets)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    bullets = pygame.Rect(red.x +  red.width, red.y + 23, 10, 5)
                    red_bullets.append(bullets)




            if event.type == RED_HIT:
                yellow_health -= 1
            if event.type == YELLLOW_HIT:
                red_health -= 1

            winner_text = ""

            if red_health <= 0:
                winner_text = "yellow win!"
            if yellow_health <= 0:
                winner_text = "red win!"
            if winner_text != "":
                draw_winner(winner_text)
                break

                
        keys_pressed = pygame.key.get_pressed()

        draw_window(red, yellow, yellow_bullets, red_bullets,red_health, yellow_health)
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)



main()

