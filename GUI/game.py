import pygame
import random

from EpidemicSimulation.GUI.features import World, Subject


class Game:
    def __init__(
        self, size_x: int = 1280, size_y: int = 720,
    ):
        """[Class to generate the space ("world") in which the epidemic simulation take place]
        :param size_x: [Window's width], defaults to 1280
        :type size_x: int, optional
        :param size_y: [Window's height], defaults to 720
        :type size_y: int, optional
        """
        self.world = World(size_x=size_x, size_y=size_y)
        self.screen = self.world.screen

