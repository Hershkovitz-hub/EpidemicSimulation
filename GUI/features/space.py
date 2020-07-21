import pygame

pygame.init()


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
        self.screen = pygame.display.set_mode((size_x, size_y))
        pygame.display.set_caption(title)

    def run(self):
        clock = pygame.time.Clock()
        done = True
        pygame.draw.circle(self.screen, (0, 0, 255), (150, 50), 15, 1)
        while done:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


if __name__ == "__main__":
    world = World()
    world.run()

