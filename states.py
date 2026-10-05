import pygame
from base_state import GameState
from mazegenerator import MazeGenerator

class Cell:
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8

    def __init__(self, x: int, y: int, val: int):
        self.x = x
        self.y = y
        self.val = val
        # True means the path is open, False means there is a wall
        self.can_go_north = not bool(val & self.NORTH)
        self.can_go_east = not bool(val & self.EAST)
        self.can_go_south = not bool(val & self.SOUTH)
        self.can_go_west = not bool(val & self.WEST)


class PlayingState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.tile_size = 40
        maze_gen = MazeGenerator((self.game.width, self.game.height), seed=42, perfect=False)
        self.cells = []
        for j, row in enumerate(maze_gen.maze):
            row_cells = []
            for i, value in enumerate(row):
                row_cells.append(Cell(i, j, value))
            self.cells.append(row_cells)

    def handle_event(self, event):
        # Press ESC to browse back to the menu
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.change_state("MENU")

    def draw(self, surface):
        for row in self.cells:
            for cell in row:
                px_x = cell.x * self.tile_size
                px_y = cell.y * self.tile_size
                
                if not cell.can_go_north:
                    pygame.draw.line(surface, (0, 0, 255), (px_x, px_y), (px_x + self.tile_size, px_y), 2)
                if not cell.can_go_south:
                    pygame.draw.line(surface, (0, 0, 255), (px_x, px_y + self.tile_size), (px_x + self.tile_size, px_y + self.tile_size), 2)
                if not cell.can_go_west:
                    pygame.draw.line(surface, (0, 0, 255), (px_x, px_y), (px_x, px_y + self.tile_size), 2)
                if not cell.can_go_east:
                    pygame.draw.line(surface, (0, 0, 255), (px_x + self.tile_size, px_y), (px_x + self.tile_size, px_y + self.tile_size), 2)


class button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)


class MenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        center_x = self.game.MENU_WIDTH // 2
        center_y = self.game.MENU_HEIGHT // 2
        
        self.button_start = button(center_x - 50, center_y - 40, 100, 50, "Start")
        self.button_quit = button(center_x - 50, center_y + 20, 100, 50, "Quit")
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button_start.is_clicked(event):
                self.game.change_state("PLAYING")
            elif self.button_quit.is_clicked(event):
                self.game.running = False

    def draw(self, surface):
        self.button_start.draw(surface)
        self.button_quit.draw(surface)