import pygame
from states import MenuState, PlayingState

class Game:
    MENU_WIDTH = 800
    MENU_HEIGHT = 600
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        # Keep the global dimensions from your test script
        self.screen = pygame.display.set_mode((self.MENU_WIDTH, self.MENU_HEIGHT)) 
        pygame.display.set_caption("Pac-Man Engine Test")
        self.running = True
        
        # Register your pages
        self.states = {
            "MENU": MenuState(self),
            "PLAYING": PlayingState(self)
        }
        self.current_state = self.states["MENU"]

    def change_state(self, state_name):
        self.current_state = self.states[state_name]

        if state_name == "PLAYING":
            self.screen = pygame.display.set_mode((self.width * 40, self.height * 40))
        elif state_name == "MENU":
            self.screen = pygame.display.set_mode((self.MENU_WIDTH, self.MENU_HEIGHT))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # Pass the event down to the active page
                self.current_state.handle_event(event)

            self.screen.fill((0, 0, 0))
            self.current_state.draw(self.screen)
            pygame.display.flip()

        pygame.quit()