import pygame
import pymunk
from epidemic_simulation.GUI.features import World, BACKGROUND_COLOR
from epidemic_simulation.GUI.features.utils.screen_divider import ScreenDivider
from epidemic_simulation.GUI.features import (
    UserInterface,
    ParametersPresenter,
    SubjectManager,
)
from epidemic_simulation.GUI.features.utils.sliders import Sliders


class Game:
    def __init__(self):
        """
        This is the main Class that governs all simulation-related calsses and method in order to initiate and manage an ongoing simulation
        """
        self.world = World()
        self.running = True
        self.parameters = {}
        self.subjects = []

    def update_game_windows(self):
        """
        Initializing or Resets all windows and UI components (changes upon window size change)
        """
        self.screen_divider = ScreenDivider(self.world)
        self.screen_divider.create_components()
        self.user_interface = UserInterface(
            self.world, self.screen_divider.selection_comp
        )
        self.user_interface.initiate_ui_selections()
        self.parameters_presenter = ParametersPresenter(
            self.world, self.screen_divider.presentation_comp,
        )
        self.parameters_presenter.place_texts(
            self.user_interface.parameters, game.subjects
        )


if __name__ == "__main__":
    game = Game()
    game.update_game_windows()
    subjects_manager = SubjectManager(
        game.world,
        game.user_interface.parameters,
        game.screen_divider.visual_comp,
    )
    subjects_manager.initiate_subjects()
    game.subjects = subjects_manager.subjects
    clock = pygame.time.Clock()
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                break
            if event.type == pygame.VIDEORESIZE:
                new_width, new_height = event.size
                game.world.resize_window(new_width, new_height)
                game.update_game_windows()
                subjects_manager.clear_all_subjects()
                subjects_manager.restart_visualisation()
            game.user_interface.menu.react(event)
        game.parameters_presenter.place_texts(
            game.user_interface.parameters, game.subjects
        )
        subjects_manager.calculate_window_dimension(
            game.screen_divider.visual_comp
        )
        subjects_manager.restart_visualisation()
        game.parameters = game.user_interface.parameters

        subjects_manager.update_subjects(game.parameters)
        if not pygame.time.get_ticks() % 600:
            subjects_manager.integrate_with_simulation()
        game.subjects = subjects_manager.subjects
        game.world.space.debug_draw(game.world.draw_options)
        clock.tick()
        pygame.display.update()
        game.world.space.step(0.001)

