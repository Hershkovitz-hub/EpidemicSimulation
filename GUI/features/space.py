import pyglet
import pymunk
import time
from pymunk.pyglet_util import DrawOptions
from EpidemicSimulation.GUI.features import initiate_window


class World:
    def __init__(
        self, size_x: int = 1280, size_y: int = 720, title: str = "Epidemic Simulation"
    ):
        """[Class to generate the space ("world") in which the epidemic simulation take place]
        :param size_x: [Window's width], defaults to 1280
        :type size_x: int, optional
        :param size_y: [Window's height], defaults to 720
        :type size_y: int, optional
        :param title: [World's window's title], defaults to "Epidemic Simulation"
        :type title: str, optional
        """
        self.title = title
        self.size_x = size_x
        self.size_y = size_y

