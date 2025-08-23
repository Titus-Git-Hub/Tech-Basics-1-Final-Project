import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
    #pygame.Rect(60, 395, 680, 300),
    #VERTIKAL
    #pygame.Rect(385, 110, 30, 630),
    #ALLES FULL
    #pygame.Rect(50, 100, 700, 650),


    # 1,2,3,4,5
    pygame.Rect(345, 400, 110, 30),
    pygame.Rect(345, 390, 30, 10),
    pygame.Rect(425, 390, 30, 10),
    #pygame.Rect(300, 350, 60, 30),
    #pygame.Rect(435, 350, 80, 30),

    # 6,7
    pygame.Rect(385, 230, 30, 90),
    pygame.Rect(340, 230, 120, 30),

    # 8,9,10,11
    pygame.Rect(260, 230, 30, 160),
    pygame.Rect(510, 230, 30, 160),
    pygame.Rect(260, 310, 80, 30),
    pygame.Rect(465, 310, 75, 30),

    # 12
    pygame.Rect(385, 100, 30, 80),

    # 13
    pygame.Rect(345, 640, 110, 115),

    # 14
    pygame.Rect(345, 480, 110, 90),

    # 15,16,17
    #.Rect(260, 475, 25, 90),
    #pygame.Rect(210, 540, 50, 25),
    #pygame.Rect(210, 565, 25, 60),

    # 18,19
    pygame.Rect(260, 450, 30, 60),
    pygame.Rect(180, 480, 80, 30),

    # 20,21
    pygame.Rect(100, 400, 110, 30),
    pygame.Rect(100, 430, 30, 200),

    # 22,23,24
    #pygame.Rect(480, 475, 25, 90),
    #pygame.Rect(500, 540, 50, 25),
    #pygame.Rect(525, 565, 25, 60),

    # 25,26
    pygame.Rect(510, 450, 30, 60),
    pygame.Rect(540, 480, 80, 30),

    # 27,28
    pygame.Rect(590, 400, 110, 30),
    pygame.Rect(670, 410, 30, 220),

    # 29,30
    pygame.Rect(100, 630, 120, 70),
    pygame.Rect(600, 630, 100, 70),

    # 31,32
    pygame.Rect(260, 150, 75, 30),
    pygame.Rect(465, 150, 75, 30),

    # 33,34
    pygame.Rect(100, 150, 110, 30),
    pygame.Rect(590, 150, 100, 30),

    # 35,36
    pygame.Rect(100, 150, 30, 200),
    pygame.Rect(670, 150, 30, 200),

    # 37,38
    pygame.Rect(180, 230, 30, 120),
    pygame.Rect(590, 230, 30, 120),

    # 39,40
    pygame.Rect(180, 510, 30, 60),
    pygame.Rect(590, 510, 30, 60),

    # 41,42
    #pygame.Rect(100, 590, 80, 110),
    #pygame.Rect(640, 590, 60, 110),

    # 43,44
    pygame.Rect(270, 560, 30, 140),
    pygame.Rect(505, 560, 30, 140),

    pygame.Rect(345, 630, 30, 10),
    pygame.Rect(425, 630, 30, 10),
]

running = True
while running:
    screen.fill(WHITE)

    for obs in obstacles:
        pygame.draw.rect(screen, BLACK, obs)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
