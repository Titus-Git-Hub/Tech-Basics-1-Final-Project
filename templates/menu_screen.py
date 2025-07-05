# To handle this task and my ideas, AI and this week's exercise examples were used as tools for assistance;
# with the requirement for myself to understand the code.

# This week's submission serves as a possible idea for a pause menu for my game in the final submission;
# if this can indeed be well implemented.

import pygame

pygame.init()
display = pygame.display.set_mode((700, 600))
display.fill((0, 0, 0))

mySurface  = pygame.Surface((700,600))

pacman = pygame.image.load("PAC-man.png")
ghost = pygame.image.load("pixel_art.png")

pacman = pygame.transform.scale(pacman, (150, 150))
ghost = pygame.transform.scale(ghost, (200, 130))

rect_1 = pacman.get_rect()
rect_2 = ghost.get_rect()

pygame.draw.rect(display, (0, 0, 0), rect_1)
pygame.draw.rect(display, (0, 0, 0), rect_2)

display.blit(pacman, (0, 0))
display.blit(ghost, (0, 0))

button1 = pygame.Rect(300, 100, 125, 35)
button2 = pygame.Rect(300, 200, 125, 35)
button3 = pygame.Rect(300, 300, 125, 35)
button4 = pygame.Rect(300, 400, 125, 35)

font = pygame.font.SysFont("Arial", 20)

text1 = font.render("PLAY", True, "black")
text2 = font.render("PAUSE", True, "black")
text3 = font.render("REPLAY", True, "black")
text4 = font.render("EXIT", True, "black")

mySurface.blit(text1, (340, 105))
mySurface.blit(text2, (330, 205))
mySurface.blit(text3, (330, 305))
mySurface.blit(text4, (340, 405))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.fill((0, 0, 0))
    mySurface.fill("azure4")

    pos = pygame.mouse.get_pos()

    color1 = "red" if button1.collidepoint(pos) else "white"
    color2 = "red" if button2.collidepoint(pos) else "white"
    color3 = "red" if button3.collidepoint(pos) else "white"
    color4 = "red" if button4.collidepoint(pos) else "white"

    pygame.draw.rect(mySurface, color1, button1, 0, 7)
    pygame.draw.rect(mySurface, color2, button2, 0, 7)
    pygame.draw.rect(mySurface, color3, button3, 0, 7)
    pygame.draw.rect(mySurface, color4, button4, 0, 7)

    mySurface.blit(text1, (340, 105))
    mySurface.blit(text2, (330, 205))
    mySurface.blit(text3, (330, 305))
    mySurface.blit(text4, (340, 405))

    display.blit(mySurface, [0, 0])

    display.blit(pacman, (100, 170))
    display.blit(ghost, (450, 220))

    pygame.display.flip()