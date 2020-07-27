import pymunk
import pygame
from epidemic_simulation.GUI.features.world import World


class ScreenDivider:
    def __init__(self, world):
        """
        A class aimed at managing the division of the simulation's main screen into 3 components: Visualisation, parameters selection, and parameter presentation
        :param world: [description]
        :type world: World
        """
        self.space = world.space
        # self.width, self.height = world.screen.get_size()
        self.width, self.height = pygame.display.get_surface().get_size()
        self.half_width = self.width / 2
        self.set_components_limits()

    def set_components_limits(self):
        """
        Sets the coordinates of the different components in relevance to screen's size
        """
        self.visual_comp = [
            (self.width - 10, 10),
            (self.width - 10, self.height - 10),
            (self.half_width + 5, self.height - 10),
            (self.half_width + 5, 10),
        ]
        self.selection_comp = [
            (10, self.height * 0.66),
            (10, self.height - 10),
            (self.half_width - 5, self.height - 10),
            (self.half_width - 5, self.height * 0.66),
        ]
        self.presentation_comp = [
            (10, 10),
            (10, self.height * 0.65),
            (self.half_width - 5, self.height * 0.65),
            (self.half_width - 5, 10),
        ]

    def add_component(self, boundaries: list):
        """
        Adds a component to the screen by it's boundaries' coordinates
        :param boundaries: [List of 4 tuples indicating component's boundaries' coordinates]
        :type boundaries: list
        """
        for coord_index in range(len(boundaries)):
            seg = pymunk.Segment(
                self.space.static_body,
                boundaries[coord_index],
                boundaries[(coord_index + 1) % 4],
                2,
            )
            seg.elasticity = 0.999
            seg.color = (255, 255, 255, 0)
            self.space.add(seg)

    def create_components(self):
        """
        Iterates over components' boundaries and add them to simulation's screen
        """
        for boundaries in [
            self.visual_comp,
            self.presentation_comp,
            self.selection_comp,
        ]:
            self.add_component(boundaries)
