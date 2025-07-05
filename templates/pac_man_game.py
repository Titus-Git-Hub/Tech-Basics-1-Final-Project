# To handle this task and my ideas, AI and the last week's assignment were used as tools for assistance;
# with the requirement for myself to understand the code.

# libraries for the game
import pygame
import random

# adjustment of the background with these constants (colour, width and height)
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
BACKGROUND_COLOR = (255, 255, 255)

# to activate the pygame library
pygame.init()

# to create the display surface object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# for the pygame window name
pygame.display.set_caption('Pacman vs Ghosts')

# PacMan class
class PacMan:
    def __init__(self, image_path):
        self.pacman_image = pygame.image.load(image_path).convert_alpha()
        self.pacman_image = pygame.transform.scale(self.pacman_image, (170, 170))
        self.image = self.pacman_image
        self.x = 100
        self.y = 100
        self.speed = 7
        self.direction = 'right'

    def handle_keys(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            if self.direction != 'left':
                self.direction = 'left'
                self.image = pygame.transform.flip(self.pacman_image, True, False)
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            if self.direction != 'right':
                self.direction = 'right'
                self.image = self.pacman_image
        elif keys[pygame.K_UP]:
            self.y -= self.speed
            if self.direction != 'up':
                self.direction = 'up'
                self.image = pygame.transform.rotate(self.pacman_image, 90)
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
            if self.direction != 'down':
                self.direction = 'down'
                self.image = pygame.transform.rotate(self.pacman_image, -90)

        # screen boundaries
        self.x = max(0, min(self.x, SCREEN_WIDTH - 170))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - 170))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def get_rect(self): # collision detection (CHAT-GPT)
        return self.image.get_rect(topleft=(self.x, self.y))

# Main base Ghost class
class Ghost1:
    def __init__(self, image_path):
        self._speed = 6
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (190, 120))
        self.respawn()

    def get_speed(self):
        return self._speed

    def set_speed(self, value):
        self._speed = max(1, value)

    def respawn(self):
        self.direction = random.choice(['left', 'right', 'top', 'bottom'])

        if self.direction == 'left':
            self.x = -80
            self.y = random.randint(0, SCREEN_HEIGHT - 120)
            self.dx = self._speed
            self.dy = 0
        elif self.direction == 'right':
            self.x = SCREEN_WIDTH
            self.y = random.randint(0, SCREEN_HEIGHT - 120)
            self.dx = -self._speed
            self.dy = 0
        elif self.direction == 'top':
            self.x = random.randint(0, SCREEN_WIDTH - 120)
            self.y = -80
            self.dx = 0
            self.dy = self._speed
        elif self.direction == 'bottom':
            self.x = random.randint(0, SCREEN_WIDTH - 120)
            self.y = SCREEN_HEIGHT
            self.dx = 0
            self.dy = -self._speed

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if (self.direction == 'left' and self.x > SCREEN_WIDTH) or \
           (self.direction == 'right' and self.x < -120) or \
           (self.direction == 'top' and self.y > SCREEN_HEIGHT) or \
           (self.direction == 'bottom' and self.y < -120):
            self.respawn()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def get_rect(self): # collision detection (CHAT-GPT)
        return self.image.get_rect(topleft=(self.x, self.y))

# Sub Ghost class (smaller, slower)
class Ghost2(Ghost1):
    def __init__(self, image_path):
        super().__init__(image_path)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 80))
        self.set_speed(4)
        self.respawn()

pacman = PacMan("PacMan.png")
ghost1 = Ghost1("ghost.png")
ghost2 = Ghost2("ghost.png")

# Init the clock
clock = pygame.time.Clock()

flag = True
while flag:
    # ticking the clock
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    keys = pygame.key.get_pressed()
    pacman.handle_keys(keys)

    # collision detection (CHAT-GPT)
    if pacman.get_rect().colliderect(ghost1.get_rect()):
        ghost1.respawn()
    if pacman.get_rect().colliderect(ghost2.get_rect()):
        ghost2.respawn()

    ghost1.move()
    ghost2.move()

    screen.fill(BACKGROUND_COLOR)
    pacman.draw(screen)
    ghost1.draw(screen)
    ghost2.draw(screen)

    pygame.display.flip()

pygame.quit()


# THE GOAL IS TO CATCH AS MANY GHOSTS AS POSSIBLE. AS LONG AS YOU WANT TO (:
# YOU CAN MOVE BY PRESSING THE ARROW KEY TO THE LEFT/RIGHT/UP/DOWN.
# HAVE FUN AND ENJOY!