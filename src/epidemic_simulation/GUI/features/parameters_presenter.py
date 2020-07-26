import pygame
from epidemic_simulation.GUI.features import World, BACKGROUND_COLOR


class ParametersPresenter:
    def __init__(
        self, world: World, presentation_limits: list,
    ):
        self.world = world
        self.corners = presentation_limits
        self.font = pygame.font.Font("freesansbold.ttf", 32)

    def restart_presentation(self):
        x, y = self.world.screen.get_size()
        self.world.screen.fill(BACKGROUND_COLOR, rect=(x / 2, 0, x, y))
        self.world.screen.fill(
            BACKGROUND_COLOR, rect=(0, 0.55 * self.corners[1][1], x, y),
        )

    def place_texts(self, parameters):
        self.restart_presentation()
        y_coordinate = 0.55 * self.corners[1][1]
        for title, value in parameters.items():
            self.add_text(
                title,
                value,
                self.corners[0][0] + 20,
                self.corners[0][1] + y_coordinate,
            )
            y_coordinate += 50

    def add_text(
        self, title: str, value: float, x_coordinate: int, y_coordinate: int
    ):
        text = self.font.render(f"{title} : {value}", True, (255, 255, 255))
        self.world.screen.blit(text, (x_coordinate, y_coordinate))
