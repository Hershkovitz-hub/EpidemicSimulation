import thorpy
from .utils.boxes import Boxes


class UserInteface:
    def __init__(self, size_x: int, size_y: int):
        """
        A class to produce all user interface part of a project
        :param size_x: [Simulation's window's width]
        :type size_x: int
        :param size_y: [Simulation's window's height]
        :type size_y: int
        """
        boxes = Boxes(size_x, size_y)
        self.coordinates = boxes.set_ui_window_limits()
