import pygame
from time import sleep
from math import sin
from math import cos
from math import pi


pygame.init()
screen = pygame.display.set_mode((500, 600))
GREY = (120, 120, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
running = True
start = False
font = pygame.font.SysFont('sans', 50)
text_1 = font.render('+', True, BLACK)
text_2 = font.render('-', True, BLACK)
text_3 = font.render('+', True, BLACK)
text_4 = font.render('-', True, BLACK)
text_5 = font.render('Start', True, BLACK)
text_6 = font.render('Reset', True, BLACK)
total_secs = 0
total = 0


sound = pygame.mixer.Sound('alarm.mp3')


while running:
    screen.fill(GREY)
    mouse_x, mouse_y = pygame.mouse.get_pos()


    pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))
    pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
    pygame.draw.rect(screen, WHITE, (300, 150, 150, 50))


    screen.blit(text_1, (100, 50))
    screen.blit(text_2, (100, 200))
    screen.blit(text_3, (200, 50))
    screen.blit(text_4, (200, 200))
    screen.blit(text_5, (300, 50))
    screen.blit(text_6, (300, 150))


    pygame.draw.rect(screen, BLACK, (50, 520, 400, 50))
    pygame.draw.rect(screen, WHITE, (60, 530, 380, 30))


    pygame.draw.circle(screen, BLACK, (250, 400), 100)
    pygame.draw.circle(screen, WHITE, (250, 400), 95)
    pygame.draw.circle(screen, BLACK, (250, 400), 5)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.pause()
                if 100 < mouse_x < 150 and 50 < mouse_y < 100:
                    total_secs += 60
                    total = total_secs
                if 100 < mouse_x < 150 and 200 < mouse_y < 250:
                    total_secs -= 60
                    total = total_secs
                if 200 < mouse_x < 250 and 50 < mouse_y < 100:
                    total_secs += 1
                    total = total_secs
                if 200 < mouse_x < 250 and 200 < mouse_y < 250:
                    total_secs -= 1
                    total = total_secs
                if 300 < mouse_x < 450 and 50 < mouse_y < 100:
                    start = True
                    total = total_secs
                if 300 < mouse_x < 450 and 150 < mouse_y < 200:
                    total_secs = 0


    if start:
        total_secs -= 1
        if total_secs == 0:
            start = False
            pygame.mixer.Sound.play(sound)
        sleep(1)


    if total_secs < 0:
        start = False
        total_secs = 0


    mins = int(total_secs / 60)
    secs = total_secs - mins * 60
    time_now = str(mins) + "  :  " + str(secs)


    text_time = font.render(time_now, True, BLACK)
    screen.blit(text_time, (120, 120))


    x_sec = 250 + 90* sin(6* secs * pi/180)
    y_sec = 400 - 90* cos(6* secs * pi/180)
    pygame.draw.line(screen, BLACK, (250, 400), (int(x_sec), int(y_sec)))


    x_min = 250 + 40* sin(6* mins * pi/180)
    y_min = 400 - 40* cos(6* mins * pi/180)
    pygame.draw.line(screen, RED, (250, 400), (int(x_min), int(y_min)))


    if total != 0:
        pygame.draw.rect(screen, RED, (60, 530, int(380 * (total_secs/ total)), 30))







    pygame.display.flip()
pygame.quit()