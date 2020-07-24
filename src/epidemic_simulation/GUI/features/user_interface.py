import thorpy
from .utils import Boxes


class UserInteface:
    def __init__(self, screen, size_x: int = 1280, size_y: int = 720):
        """
        A class to produce all user interface part of a project
        :param size_x: [Simulation's window's width]
        :type size_x: int
        :param size_y: [Simulation's window's height]
        :type size_y: int
        """
        self.screen = screen
        boxes = Boxes(size_x, size_y)
        self.coordinates = boxes.set_ui_window_limits()
        self.calculate_shape()

    def calculate_shape(self):
        self.height = self.coordinates[1][1] - self.coordinates[0][1]
        self.width = self.coordinates[2][0] - self.coordinates[0][0]

    def initiate_slider(self, value_range: tuple, title: str):
        slider = thorpy.SliderX(length=100, limvals=value_range, text=title,)
        return slider

    def generate_ui_box(self, elements: list):
        ui_box = thorpy.Box(size=(self.width, self.height), elements=elements)
        return ui_box

    @property
    def quit_button(self):
        button = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
        return button

    @property
    def sliders(self):
        sliders = []
        for value_range, title in zip(
            [(0, 1), (0, 20), (0, 100)],
            [
                "Probability of infection",
                "Infection Radius",
                "Percentge of carriers",
            ],
        ):
            sliders.append(self.initiate_slider(value_range, title))
        return sliders

    @property
    def elements(self):
        elements = self.sliders
        elements.append(self.quit_button)
        return elements

    def run(self):
        slider = self.initiate_slider()
        ui_box = self.generate_ui_box(slider)
        ui_box.set_topleft((100, 100))
        menu = thorpy.Menu(ui_box)
        for element in menu.get_population():
            element.surface = self.screen
        ui_box.blit()
        ui_box.update()


if __name__ == "__main__":
    UserInterface().generate_ui_box()
