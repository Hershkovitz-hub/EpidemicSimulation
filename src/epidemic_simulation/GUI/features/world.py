import pygame
import pymunk
import pymunk.pygame_util
import thorpy

BACKGROUND_COLOR = (0, 0, 0)


class World:
    def __init__(self, size_x: int = 1280, size_y: int = 720):
        pygame.init()
        self.space = pymunk.Space()
        self.space.gravity = 0, 0
        self.screen = pygame.display.set_mode(
            (size_x, size_y), pygame.RESIZABLE
        )
        pygame.display.set_caption("Epidemic Simulation")
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.screen.fill(BACKGROUND_COLOR)

    def resize_window(self, size_x: int, size_y: int):
        """
        Update the screen to change when users change screen size
        :param size_x: [Screen's new width]
        :type size_x: int
        :param size_y: [Screen's new height]
        :type size_y: int
        """
        self.screen = pygame.display.set_mode(
            (size_x, size_y), pygame.RESIZABLE
        )
        self.screen.fill(BACKGROUND_COLOR)
        segments = [
            shape
            for shape in self.space._get_shapes()
            if isinstance(shape, pymunk.shapes.Segment)
        ]
        self.space.remove(segments)


if __name__ == "__main__":
    World()
