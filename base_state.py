class GameState:
    def __init__(self, game):
        self.game = game # Reference to the router to call change_state()

    def handle_event(self, event):
        pass

    def draw(self, surface):
        pass