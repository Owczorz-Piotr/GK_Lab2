import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
CZARNY = (0, 0, 0)
ZOLTY = (255, 255, 0)
BIALY = (255,255,255)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(win, BIALY, (0,0,600,600))
    pygame.draw.circle(win, CZARNY, (250, 250), 200, 200)
    pygame.draw.rect(win, ZOLTY , (150, 150, 200, 200))
    


    pygame.display.update()
