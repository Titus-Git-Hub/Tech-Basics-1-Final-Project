from helper import *

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Spectral Sprint")
    font = pygame.font.SysFont(None, 40)
    best_time = None
    restart = True

    while restart:
        start_screen(screen, font)
        best_time, restart = play_game(screen, font, best_time)

    pygame.quit()


if __name__ == "__main__":
    main()