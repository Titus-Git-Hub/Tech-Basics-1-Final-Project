import pygame
import random
import time

#constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

#functions
def start_screen(screen, font):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("media/music_menu.mp3")
    pygame.mixer.music.play(-1)

    logo = pygame.image.load("media/ascii_art_text_start.png")
    logo = pygame.transform.scale(logo, (800, 160))
    logo_rect = logo.get_rect(center=(SCREEN_WIDTH // 2, 120))

    waiting = True
    while waiting:
        screen.fill(WHITE)
        screen.blit(logo, logo_rect)
        screen.blit(font.render("Welcome! To:", True, BLACK), (10, 10))
        screen.blit(font.render("1: Game controls: ARROW KEYS or WASD", True, BLACK), (115, 350))
        screen.blit(font.render("2: Goal: Catching the ghost 3 times in under 30 seconds!", True, BLACK), (20, 415))
        screen.blit(font.render("=> Press SPACE to start", True, BLACK), (230, 600))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False


def pause_screen(screen, font):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("media/music_menu.mp3")
    pygame.mixer.music.play(-1)

    logo = pygame.image.load("media/ascii_art_text_pause.png")
    logo = pygame.transform.scale(logo, (800, 160))
    logo_rect = logo.get_rect(center=(SCREEN_WIDTH // 2, 150))

    paused = True
    while paused:
        screen.fill(WHITE)
        screen.blit(logo, logo_rect)
        screen.blit(font.render("PAUSE", True, BLACK), (350, 25))
        screen.blit(font.render("=> Press SPACE to continue", True, BLACK), (220, 400))
        screen.blit(font.render("or ESC to finish", True, BLACK), (300, 450))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()


def end_screen(screen, font, won, elapsed_time, best_time):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("media/music_menu.mp3")
    pygame.mixer.music.play(-1)

    waiting = True
    while waiting:
        screen.fill(WHITE)
        if won:
            logo = pygame.image.load("media/ascii_art_text_win.png")
            logo = pygame.transform.scale(logo, (800, 160))
            logo_rect = logo.get_rect(center=(SCREEN_WIDTH // 2, 120))
            screen.blit(logo, logo_rect)

            screen.blit(font.render(f"WIN! Time: {elapsed_time}s", True, (BLACK)), (260, 330))
            screen.blit(font.render(f"Personal Best: {best_time}s", True, (BLACK)), (320, 380))
            screen.blit(font.render("Press SPACE to restart", True, BLACK), (250, 660))
            screen.blit(font.render("or ESC to finish", True, BLACK), (300, 710))
        else:
            logo = pygame.image.load("media/ascii_art_text_defeat.png")
            logo = pygame.transform.scale(logo, (800, 160))
            logo_rect = logo.get_rect(center=(SCREEN_WIDTH // 2, 120))
            screen.blit(logo, logo_rect)

            screen.blit(font.render("GAME OVER!", True, (BLACK)), (310, 400))
            screen.blit(font.render("Press SPACE to restart", True, BLACK), (250, 660))
            screen.blit(font.render("or ESC to finish", True, BLACK), (300, 710))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
    return False


def countdown(screen, font):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("media/music_countdown.mp3")
    pygame.mixer.music.play(-1)

    for text in ["Have Fun!", "", "3", "2", "1", "GO!"]:
        screen.fill(WHITE)
        render = font.render(text, True, (255,0,0))
        rect = render.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        screen.blit(render, rect)
        pygame.display.update()
        pygame.time.wait(1000)


def play_game(screen, font, best_time):
    hunter_img = pygame.transform.scale(pygame.image.load("media/character_hunter.png"), (40, 40))
    ghost_img = pygame.transform.scale(pygame.image.load("media/character_ghost.png"), (40, 40))
    heart_img = pygame.transform.scale(pygame.image.load("media/img_heart.png"), (30, 30))

    hunter = Hunter(hunter_img)
    ghost = Ghost(ghost_img)

    # see sketch drawing -> Tech-Basics-1-Final-Project/media/sketch_drawing_2.png
    obstacles = [
        # Outer Borders ->
        pygame.Rect(25, 75, 25, 700),
        pygame.Rect(750, 75, 25, 700),
        # Upper/Lower Border ->
        pygame.Rect(50, 75, 700, 25),
        pygame.Rect(50, 750, 700, 25),
        # 1 ->
        pygame.Rect(345, 640, 110, 115),
        pygame.Rect(345, 630, 30, 10),
        pygame.Rect(425, 630, 30, 10),
        # 2 ->
        pygame.Rect(345, 480, 110, 90),
        # 3 ->
        pygame.Rect(345, 400, 110, 30),
        pygame.Rect(345, 390, 30, 10),
        pygame.Rect(425, 390, 30, 10),
        # 4 ->
        pygame.Rect(385, 230, 30, 90),
        # 5 ->
        pygame.Rect(340, 230, 120, 30),
        # 6 ->
        pygame.Rect(385, 100, 30, 80),
        # 7 ->
        pygame.Rect(465, 150, 75, 30),
        # 8 ->
        pygame.Rect(590, 150, 100, 30),
        # 9 ->
        pygame.Rect(670, 150, 30, 200),
        # 10 ->
        pygame.Rect(260, 150, 75, 30),
        # 11 ->
        pygame.Rect(100, 150, 110, 30),
        # 12 ->
        pygame.Rect(100, 150, 30, 200),
        # 13 ->
        pygame.Rect(180, 230, 30, 120),
        # 14 ->
        pygame.Rect(590, 230, 30, 120),
        # 15 ->
        pygame.Rect(260, 230, 30, 160),
        # 16 ->
        pygame.Rect(260, 310, 75, 30),
        # 17 ->
        pygame.Rect(465, 310, 75, 30),
        # 18 ->
        pygame.Rect(510, 230, 30, 160),
        # 19 ->
        pygame.Rect(590, 400, 110, 30),
        # 20 ->
        pygame.Rect(670, 410, 30, 220),
        # 21 ->
        pygame.Rect(590, 630, 110, 70),
        # 22 ->
        pygame.Rect(100, 400, 110, 30),
        # 23 ->
        pygame.Rect(100, 430, 30, 200),
        # 24 ->
        pygame.Rect(100, 630, 110, 70),
        # 25 ->
        pygame.Rect(260, 440, 30, 70),
        # 26 ->
        pygame.Rect(180, 480, 80, 30),
        # 27 ->
        pygame.Rect(180, 510, 30, 60),
        # 28 ->
        pygame.Rect(510, 440, 30, 70),
        # 29 ->
        pygame.Rect(540, 480, 80, 30),
        # 30 ->
        pygame.Rect(590, 510, 30, 60),
        # 31 ->
        pygame.Rect(260, 560, 30, 140),
        # 32 ->
        pygame.Rect(510, 560, 30, 140),
    ]

    ghost_lives = 3
    time_limit = 30

    countdown(screen, font)

    pygame.mixer.music.stop()
    pygame.mixer.music.load("media/music_in_game.mp3")
    pygame.mixer.music.play(-1)

    start_time = time.time()

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(GREY)

        # from ChatGPT
        elapsed = int(time.time() - start_time)
        remaining_time = max(0, time_limit - elapsed)
        if remaining_time <= 0:
            restart_game = end_screen(screen, font, False, elapsed, best_time)
            return best_time, restart_game
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 800, 50))
        pygame.draw.rect(screen, WHITE, pygame.Rect(50, 100, 700, 650))

        for obs in obstacles:
            pygame.draw.rect(screen, BLACK, obs)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause_screen(screen, font)

                pygame.mixer.music.stop()
                pygame.mixer.music.load("media/music_in_game.mp3")
                pygame.mixer.music.play(-1)

        keys = pygame.key.get_pressed()
        hunter.move(keys, obstacles, screen.get_rect())

        ghost.move_random(obstacles, screen.get_rect())

        # from ChatGPT
        if hunter.rect.colliderect(ghost.rect):
            ghost_lives -= 1
            if ghost_lives <= 0:
                current_time = elapsed
                if best_time is None or current_time < best_time:
                    best_time = current_time
                restart_game = end_screen(screen, font, True, current_time, best_time)
                return best_time, restart_game
            else:
                ghost.rect = Ghost.respawn_ghost(obstacles)

        # from ChatGPT
        timer_text = font.render(f"Zeit: {remaining_time}", True, BLACK)
        screen.blit(timer_text, (25, 15))
        screen.blit(font.render("BETTER BE FAST...", True, BLACK), (510, 15))
        small_font = pygame.font.SysFont(None, 25)
        screen.blit(small_font.render("Press SPACE to pause", True, BLACK), (310, 780))
        for i in range(ghost_lives):
            screen.blit(heart_img, (150 + i * 35, 12))

        screen.blit(hunter.image, hunter.rect)
        screen.blit(ghost.image, ghost.rect)

        pygame.display.update()
        clock.tick(60)

#classes
class Ghost:
    def __init__(self, image, start_pos=(400, 370), speed=2):
        self.image = image
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = speed
        self.direction = random.choice(["left", "right", "up", "down"])

    def move_random(self, obstacles, bounds):
        old_rect = self.rect.copy()

        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed

        hit_wall = False
        if self.rect.left < bounds.left:
            self.rect.left = bounds.left
            hit_wall = True
        if self.rect.right > bounds.right:
            self.rect.right = bounds.right
            hit_wall = True
        if self.rect.top < bounds.top:
            self.rect.top = bounds.top
            hit_wall = True
        if self.rect.bottom > bounds.bottom:
            self.rect.bottom = bounds.bottom
            hit_wall = True

        for obs in obstacles:
            if self.rect.colliderect(obs):
                self.rect = old_rect
                hit_wall = True

        if hit_wall:
            self.direction = random.choice(["left", "right", "up", "down"])

    # from ChatGPT
    @staticmethod
    def respawn_ghost(obstacles):
        while True:
            x = random.randint(50, SCREEN_WIDTH - 90)
            y = random.randint(100, SCREEN_HEIGHT - 90)
            new_rect = pygame.Rect(x, y, 40, 40)
            if not any(new_rect.colliderect(o) for o in obstacles):
                return new_rect


class Hunter:
    def __init__(self, image, start_pos=(400, 618), speed=3):
        self.image = image
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = speed

    def move(self, keys, obstacles, bounds):
        old_rect = self.rect.copy()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        for obs in obstacles:
            if self.rect.colliderect(obs):
                self.rect = old_rect


