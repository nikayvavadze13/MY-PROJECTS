import pygame

pygame.init()

WINDOW = pygame.display.set_mode((900,500))




def draw_window():
    WINDOW.blit(0, 0)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()


    draw_window()

main()