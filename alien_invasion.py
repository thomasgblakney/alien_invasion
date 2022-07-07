import sys
import pygame
from settings import Settings

# make an empty pygame window.


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)  # set the background color

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)  # redraw the screen during each pass through the loop

            # make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # make game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

