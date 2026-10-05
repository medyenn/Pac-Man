# from time import sleep

# from mazegenerator import MazeGenerator
# import pygame


# WIDTH = 20
# HEIGHT = 20

# maze = MazeGenerator((WIDTH, HEIGHT), seed=42, perfect=False)

# class Cell:
#     NORTH = 1
#     EAST = 2
#     SOUTH = 4
#     WEST = 8

#     def __init__(self, x: int, y: int, val: int):
#         self.x = x
#         self.y = y
#         self.val = val
#         # True means the path is open, False means there is a wall
#         self.can_go_north = not bool(val & self.NORTH)
#         self.can_go_east = not bool(val & self.EAST)
#         self.can_go_south = not bool(val & self.SOUTH)
#         self.can_go_west = not bool(val & self.WEST)



# Cells = []
# for j, row in enumerate(maze.maze):
#     row_cells = []
#     for i, value in enumerate(row):
#         row_cells += [Cell(i, j, value)]
#     Cells += [row_cells]




# # 2. Pygame Setup
# pygame.init()
# TILE_SIZE = 40 # what is this ? # The size of each tile in pixels
# WIDTH = WIDTH * TILE_SIZE
# HEIGHT = HEIGHT * TILE_SIZE

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("A-Maze-ing Render")

# # 3. Main Loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((0, 0, 0)) # Black background

#     # 4. Draw the Maze
#     for row in Cells:
#         for cell in row:
#             px_x = cell.x * TILE_SIZE
#             px_y = cell.y * TILE_SIZE
            
#             # Draw a blue line if the path is blocked
#             if not cell.can_go_north:
#                 pygame.draw.line(screen, (0, 0, 255), (px_x, px_y), (px_x + TILE_SIZE, px_y), 2)
#             if not cell.can_go_south:
#                 pygame.draw.line(screen, (0, 0, 255), (px_x, px_y + TILE_SIZE), (px_x + TILE_SIZE, px_y + TILE_SIZE), 2)
#             if not cell.can_go_west:
#                 pygame.draw.line(screen, (0, 0, 255), (px_x, px_y), (px_x, px_y + TILE_SIZE), 2)
#             if not cell.can_go_east:
#                 pygame.draw.line(screen, (0, 0, 255), (px_x + TILE_SIZE, px_y), (px_x + TILE_SIZE, px_y + TILE_SIZE), 2)

#     pygame.display.flip()

# pygame.quit()












##########################################################################################


                
# class GameState:
#     def __init__(self, game):
#         self.game = game

#     def handle_event(self, event):
#         pass

#     def draw(self):
#         pass


# class MENU(GameState):
#     def __init__(self, game):
#         self.game = game
#         self.font = pygame.font.SysFont(None, 48)

#     def handle_event(self, event):
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
#             self.game.change_state("PlayingState")
            

#     def draw(self):
#         text = self.font.render("Press ENTER to Start", True, (255, 255, 255))
#         # if I want this to appear in the middle of the screen, I need to calculate the position based on the screen size and text size
#         text_rect = text.get_rect(center=(self.game.width * self.game.TILE_SIZE // 2, self.game.height * self.game.TILE_SIZE // 2))
#         self.game.screen.blit(text, text_rect)







# class PlayingState(GameState):
#     def __init__(self, game):
#         self.game = game
#         self.maze = MazeGenerator((game.width, game.height), seed=42, perfect=False)
#         self.Cells = []
#         for j, row in enumerate(self.maze.maze):
#             row_cells = []
#             for i, value in enumerate(row):
#                 row_cells += [Cell(i, j, value)]
#             self.Cells += [row_cells]

#     def handle_event(self, event):
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#             self.game.change_state("MENU")

#     def draw(self):
#         for row in self.Cells:
#             for cell in row:
#                 px_x = cell.x * self.game.TILE_SIZE
#                 px_y = cell.y * self.game.TILE_SIZE
                
#                 # Draw a blue line if the path is blocked
#                 if not cell.can_go_north:
#                     pygame.draw.line(self.game.screen, (0, 0, 255), (px_x, px_y), (px_x + self.game.TILE_SIZE, px_y), 2)
#                 if not cell.can_go_south:
#                     pygame.draw.line(self.game.screen, (0, 0, 255), (px_x, px_y + self.game.TILE_SIZE), (px_x + self.game.TILE_SIZE, px_y + self.game.TILE_SIZE), 2)
#                 if not cell.can_go_west:
#                     pygame.draw.line(self.game.screen, (0, 0, 255), (px_x, px_y), (px_x, px_y + self.game.TILE_SIZE), 2)
#                 if not cell.can_go_east:
#                     pygame.draw.line(self.game.screen, (0, 0, 255), (px_x + self.game.TILE_SIZE, px_y), (px_x + self.game.TILE_SIZE, px_y + self.game.TILE_SIZE), 2)
    


# class Games:
#     TILE_SIZE = 40
#     def __init__(self, width, height):
#         pygame.init()
#         self.width = width
#         self.height = height
#         self.screen = pygame.display.set_mode((self.width* self.TILE_SIZE, self.height* self.TILE_SIZE))
#         pygame.display.set_caption("PAC-MAC")
#         self.states = {
#             "MENU": MENU(game=self),
#             "PlayingState": PlayingState(game=self)
#         }
#         self.current_state = self.states["MENU"]


#     def change_state(self, state):
#         self.current_state = self.states[state]

#     def run(self):
#         running = True
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 self.current_state.handle_event(event)
#             self.screen.fill((0, 0, 0))
#             self.current_state.draw()

#             pygame.display.flip()

#         pygame.quit()




# games = Games(20, 20)
# games.run()


    
    


