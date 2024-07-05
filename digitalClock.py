import pygame
import datetime
import pygame.font

running = True
WIDTH = 500
HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Watch")
screen.fill("black")

timeRect = pygame.Rect(0.25 * WIDTH, 0.125 * HEIGHT, 0.75 * WIDTH, 0.45 * HEIGHT)
dateRect = pygame.Rect(0.25 * WIDTH, 0.575 * HEIGHT, 0.75 * WIDTH, 0.323 * HEIGHT)
font = pygame.font.Font(None, 72)
fontd = pygame.font.Font(None, 42)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    timeNow = font.render(datetime.datetime.now().strftime("%H : %M : %S"), True, "#00ff00")
    dateToday = fontd.render(datetime.date.today().strftime(" %a  %b %d , %Y"), True, "white")

    screen.fill("black")
    screen.blit(timeNow, timeRect)
    screen.blit(dateToday, dateRect)

    pygame.display.update()
pygame.quit()