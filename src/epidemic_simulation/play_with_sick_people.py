import pygame
import pymunk
from epidemic_simulation.GUI.features import World, BACKGROUND_COLOR
from epidemic_simulation.GUI.features.utils.screen_divider import ScreenDivider
from epidemic_simulation.GUI.features import UserInterface
from epidemic_simulation.GUI.features.utils.sliders import Sliders


class Game:
    def __init__(self):
        self.world = World()
        self.running = True
        self.set_initial_parameters()

    def set_initial_parameters(self):
        self.parameters = {}
        for parameter in Sliders:
            self.parameters[parameter.name] = parameter.value["initial_value"]

    def update_game_windows(self):
        """
        Initializing or Resets all windows and UI components (changes upon window size change)
        """
        screen_divider = ScreenDivider(self.world)
        screen_divider.create_components()
        self.user_interface = UserInterface(
            self.world, screen_divider.selection_comp
        )
        self.user_interface.initiate_ui_selections()


if __name__ == "__main__":
    game = Game()
    game.update_game_windows()
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                break
            if event.type == pygame.VIDEORESIZE:
                new_width, new_height = event.size
                game.world.resize_window(new_width, new_height)
                game.update_game_windows()
            game.user_interface.menu.react(event)
        game.world.space.debug_draw(game.world.draw_options)
        pygame.display.update()
        game.world.space.step(0.001)

