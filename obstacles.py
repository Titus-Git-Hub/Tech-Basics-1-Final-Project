import pygame

GREY = (170, 170, 170)
RED = (200, 50, 50)

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Obstacles")

obstacles = [
    #Außen Begrenzung
    pygame.Rect(25, 75, 25, 700),
    pygame.Rect(750, 75, 25, 700),
    #Oben/Unten Begrenzung
    pygame.Rect(50, 75, 700, 25),
    pygame.Rect(50, 750, 700, 25),

    #HORIZONTAL
    #pygame.Rect(60, 400, 680, 25),
    #VERTIKAL
    #pygame.Rect(400, 110, 25, 630),
    #ALLES FULL
    #pygame.Rect(50, 100, 700, 650),

    pygame.Rect(360, 400, 100, 25),
    pygame.Rect(360, 350, 25, 50),
    pygame.Rect(435, 350, 25, 50),

    pygame.Rect(400, 225, 25, 90),
    pygame.Rect(340, 225, 140, 25),

    pygame.Rect(230, 225, 25, 140),
    pygame.Rect(555, 225, 25, 140),
    pygame.Rect(255, 280, 100, 25),
    pygame.Rect(460, 280, 100, 25),

    pygame.Rect(400, 100, 25, 80),

    pygame.Rect(360, 625, 100, 125),

    pygame.Rect(400, 475, 25, 90),

    pygame.Rect(320, 475, 25, 90),
    pygame.Rect(270, 540, 50, 25),
    pygame.Rect(270, 565, 25, 60),

    pygame.Rect(230, 410, 25, 60),
    pygame.Rect(190, 445, 40, 25),

    pygame.Rect(130, 360, 60, 25),
    pygame.Rect(130, 410, 25, 60),


    pygame.Rect(480, 475, 25, 90),
    pygame.Rect(500, 540, 50, 25),
    pygame.Rect(525, 565, 25, 60),

    pygame.Rect(555, 410, 25, 60),
    pygame.Rect(580, 445, 40, 25),

    pygame.Rect(620, 360, 60, 25),
    pygame.Rect(655, 410, 25, 60),
]

running = True
while running:
    screen.fill(GREY)

    for obs in obstacles:
        pygame.draw.rect(screen, RED, obs)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
