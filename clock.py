"""
    feel free to contact me
"""
import pygame
import numpy as np
import datetime
import pygame.font

pygame.init()

WIDTH = 800
HEIGHT = 800
RADIUS = 300
BORDER = 20     # border to the clock circle
CENTER = (WIDTH//2, HEIGHT//2)

pygame.display.set_caption("CLOCK")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("black")

font = pygame.font.Font(None, 72)
textRect = pygame.Rect(290, 20, 300, 100)
running = True

def drawClock():
    pygame.draw.circle(screen,"#980e0d",CENTER, RADIUS + BORDER,)
    pygame.draw.circle(screen,"white",CENTER, RADIUS,)

    # seconds hand
    pygame.draw.line(screen, "black", CENTER, 
                            (CENTER[0]-(RADIUS-500 )* np.sin(np.radians(6 * datetime.datetime.today().second)), 
                             CENTER[1]+(RADIUS-500) * np.cos(np.radians(6 * datetime.datetime.today().second))), 5)
    
    # minute hand
    # adding 6 * datetime.datetime.today().second / 60 to make movement of hand smoother
    # 6 because that is the angle the hand covers in a minute
    pygame.draw.line(screen, "black", CENTER, 
                            (CENTER[0]-(RADIUS-450 )* np.sin(np.radians((6 * datetime.datetime.today().minute + 6 * datetime.datetime.today().second / 60))), 
                             CENTER[1]+(RADIUS-450) * np.cos(np.radians((6 * datetime.datetime.today().minute + 6 * datetime.datetime.today().second / 60)))), 7)
    
    # hour hand
    # adding 30 * datetime.datetime.today().minute / 60 to make movement of hand smoother
    # 30 because that is the angle the hand covers in an hour
    pygame.draw.line(screen, "black", CENTER, 
                            (CENTER[0]-(RADIUS-430 )* np.sin(np.radians((30 * datetime.datetime.today().hour + 30 * datetime.datetime.today().minute / 60))), 
                             CENTER[1]+(RADIUS-430) * np.cos(np.radians((30 * datetime.datetime.today().hour + 30 * datetime.datetime.today().minute / 60)))), 10)
    
    pygame.draw.circle(screen,"black",CENTER, RADIUS // 20,)

    #drawing the hours sticks
    for hour in range(12):
         pygame.draw.line(screen, "black", 
                            (CENTER[0]-(RADIUS-50 )* np.sin(np.radians(30 * hour)), 
                             CENTER[1]-(RADIUS-50) * np.cos(np.radians(30 * hour))),
                            (CENTER[0]-RADIUS * np.sin(np.radians(30 * hour)), 
                             CENTER[1]-RADIUS * np.cos(np.radians(30 * hour))),10)

    #drawing the minnutes && seconds sticks
    for minSec in range(60):
         pygame.draw.line(screen, "black", 
                            (CENTER[0]-(RADIUS-10 )* np.sin(np.radians(6 * minSec)), 
                             CENTER[1]-(RADIUS-10) * np.cos(np.radians(6 * minSec))),
                            (CENTER[0]-RADIUS * np.sin(np.radians(6 * minSec)), 
                             CENTER[1]-RADIUS * np.cos(np.radians(6* minSec))),3)

while running:
     
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()

    screen.fill("black")
    drawClock()

    timetxt = font.render(datetime.datetime.now().strftime("%H : %M : %S"), True, "#00ff00")
    screen.blit(timetxt, textRect)

    pygame.display.update()
pygame.quit()