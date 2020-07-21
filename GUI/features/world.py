import pygame
import pymunk
import pymunk.pygame_util

GRAY = (0, 0, 0)
space = pymunk.Space()
space.gravity = 0, -900
b0 = space.static_body


class World:
    def __init__(
        self,
        size_x: int = 1280,
        size_y: int = 720,
        title: str = "Epidemic Simulation",
    ):
        """[Class to generate the space ("world") in which the epidemic simulation take place]
        :param size_x: [Window's width], defaults to 1280
        :type size_x: int, optional
        :param size_y: [Window's height], defaults to 720
        :type size_y: int, optional
        :param title: [World's window's title], defaults to "Epidemic Simulation"
        :type title: str, optional
        """
        self.size_x = size_x
        self.size_y = size_y
        pygame.init()
        self.screen = pygame.display.set_mode((size_x, size_y))
        pygame.display.set_caption(title)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill(GRAY)
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.01)
        pygame.quit()


if __name__ == "__main__":
    world = World()
    world.run()

