import pygame
import pymunk
import pymunk.pygame_util
import thorpy
from .utils import Boxes
from . import UserInteface, ParametersPresenter

BACKGROUND = (0, 0, 0)
space = pymunk.Space()
space.gravity = 0, 0
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
        self.r = 0
        self.infection_radius = 0
        self.carriers = 0
        self.size_x = size_x
        self.size_y = size_y
        pygame.init()
        self.screen = pygame.display.set_mode(
            (size_x, size_y), pygame.RESIZABLE
        )
        pygame.display.set_caption(title)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)

        self.screen.fill(BACKGROUND)
        self.running = True
        self.set_ui()

    def set_ui(self):
        """
        Uses UserInterface class to generate and maintain user interface part of the simulation
        """
        ui_manager = UserInteface(self.screen, self.size_x, self.size_y)
        self.elements = ui_manager.elements
        ui_box = ui_manager.generate_ui_box(self.elements)
        self.background = thorpy.Background(elements=self.elements)
        self.menu = thorpy.Menu(ui_box)
        for element in self.menu.get_population():
            element.surface = self.screen
        ui_box.set_topleft((10, 10))
        ui_box.blit()
        ui_box.update()

    @property
    def reaction(self):
        return thorpy.Reaction(
            reacts_to=pygame.USEREVENT,
            reac_func=self.sliders_reaction,
            event_args={"id": thorpy.constants.EVENT_SLIDE},
            params={
                "r": self.elements[0],
                "infection_radius": self.elements[1],
                "carriers": self.elements[2],
            },
        )

    def run(self):
        self.background.add_reaction(self.reaction)
        self.menu = thorpy.Menu(self.background)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                # elif event.type == pygame.USEREVENT:

                self.menu.react(event)
            x, y = self.screen.get_width(), self.screen.get_height()
            self.size_x, self.size_y = pygame.display.get_surface().get_size()
            Boxes(self.size_x, self.size_y, space=space).create()
            self.screen.fill(
                BACKGROUND, rect=(x / 2, 0, x, y),
            )
            self.screen.fill(
                BACKGROUND, rect=(0, 150, x, y),
            )
            ParametersPresenter(
                self.screen,
                self.size_x,
                self.size_y,
                self.r,
                self.infection_radius,
                self.carriers,
            ).place_texts()
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.01)
        pygame.quit()

    def sliders_reaction(self, event, r, infection_radius, carriers):
        if event.el == r:
            self.r = r.get_value()
        if event.el == infection_radius:
            self.infection_radius = infection_radius.get_value()
        if event.el == carriers:
            self.carriers = carriers.get_value()


if __name__ == "__main__":
    world = World()
    world.run()

