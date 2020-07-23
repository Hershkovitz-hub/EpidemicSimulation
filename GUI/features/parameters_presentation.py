import pygame
from .utils import Boxes


class ParametersPresenter:
    def __init__(
        self,
        screen,
        size_x: int,
        size_y: int,
        p_infection: float,
        infection_radius: float,
        carriers: int,
        r: float = 0,
        susceptible: int = 10,
        infectious: int = 10,
        removed: float = 10,
    ):
        self.screen = screen
        self.size_x = size_x
        self.size_y = size_y
        self.p_infection = p_infection
        self.infection_radius = infection_radius
        self.carriers = carriers
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.get_window_corners()
        self.r = r
        self.susceptible = susceptible
        self.infectious = infectious
        self.removed = removed

    def get_window_corners(self):
        self.corners = Boxes(
            self.size_x, self.size_y
        ).set_param_window_limits()

    def place_texts(self):
        for title, value, y_coordinate in zip(
            [
                "Probability of infection",
                "Infection radius",
                "Number of initial carriers",
                "R",
                "Susceptible",
                "Infectious",
                "Removed",
            ],
            [
                self.p_infection,
                self.infection_radius,
                self.carriers,
                self.r,
                self.susceptible,
                self.infectious,
                self.removed,
            ],
            [150, 200, 250, 300, 350, 400],
        ):
            y_coordinate = self.corners[0][1] + y_coordinate
            self.show_text(title, value, self.corners[0][0] + 20, y_coordinate)

    def show_text(
        self, title: str, value: str, x_coordinate: int, y_coordinate: int,
    ):
        text = self.font.render(f"{title} : {value}", True, (255, 255, 255))
        self.screen.blit(text, (x_coordinate, y_coordinate))

