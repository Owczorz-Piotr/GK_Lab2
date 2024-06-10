
import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 1")
CZARNY = (0, 0, 0)
FIOLETOWY = (128, 0, 128)

def pentagon(center,shift):
    r = 150
    c = center

    points = []
    for i in range(5):
        angle_deg = 72 * i
        angle_rad = math.radians(angle_deg)
        x = c[0] + r * math.cos(angle_rad)
        y = c[1] + r * math.sin(angle_rad)
        if i > 3:
            x += shift
        points.append((x, y))
    pygame.draw.polygon(win, FIOLETOWY, points)

pentagon((300,300),0)
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_1:
                    win = pygame.display.set_mode((600, 600))
                    pentagon((300,300),0)
                    penta = pygame.transform.scale_by(win, (0.6,0.6))
                    rect = penta.get_rect(center=(300, 300))
                    win.blit(penta, rect)
                    pygame.display.update()
                case pygame.K_2:
                    win = pygame.display.set_mode((600, 600))
                    pentagon((300,300),0)
                    penta = pygame.transform.rotate(win, 45)
                    rect = penta.get_rect(center=(300, 300))
                    win.blit(penta, rect)
                    pygame.display.update()
                case pygame.K_3:
                    win = pygame.display.set_mode((600, 600))
                    pentagon((300,300),0)
                    penta = pygame.transform.scale_by(win, (0.6,1))
                    penta = pygame.transform.flip(penta, False, True)
                    rect = penta.get_rect(center=(300, 300))
                    win.blit(penta, rect)
                    pygame.display.update()
                case pygame.K_4:
                    win = pygame.display.set_mode((600, 600))
                    pentagon((300,300),70)
                    rect = win.get_rect(center=(300, 300))
                    win.blit(win, rect)
                    pygame.display.update()
                case pygame.K_5:
                    win = pygame.display.set_mode((600, 600))
                    pentagon((300,300),0)
                    penta = pygame.transform.scale_by(win, (1,1/3))
                    rect = penta.get_rect(center=(300, 50))
                    pygame.draw.rect(win,CZARNY,(0,101,600,499))
                    win.blit(penta, rect)
                    pygame.display.update()
                case pygame.K_6:
                     win = pygame.display.set_mode((600, 600))
                     pentagon((300,300),70)
                     penta = pygame.transform.rotate(win, 90)
                     rect = penta.get_rect(center=(300, 300))
                     win.blit(penta, rect)
                     pygame.display.update()
                case pygame.K_7:
                    win = pygame.display.set_mode((600, 600))
                    pentagon((300,300),0)
                    penta = pygame.transform.scale_by(win, (0.6,1))
                    penta = pygame.transform.rotate(win, 180)
                    rect = penta.get_rect(center=(300, 300))
                    win.blit(penta, rect)
                    pygame.display.flip()
                case pygame.K_8:
                    win = pygame.display.set_mode((600, 600))
                    pentagon((300,300),0)
                    penta = pygame.transform.scale_by(win, (1,1/3))
                    penta = pygame.transform.rotate(penta, 120)
                    rect = penta.get_rect(center=(200, 400))
                    pygame.draw.rect(win,CZARNY,(250,250,250,100))
                    win.blit(penta, rect)
                    pygame.display.flip()
                case pygame.K_9:
                     win = pygame.display.set_mode((600, 600))
                     pentagon((300,300),70)
                     penta = pygame.transform.rotate(win, 180)
                     rect = penta.get_rect(center=(490, 300))
                     pygame.draw.rect(win,CZARNY,(0,150,320,400))
                     win.blit(penta, rect)
                     pygame.display.update()