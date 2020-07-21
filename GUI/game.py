import pygame
import random
import pymunk
from random import randint
from features import World, Subject
from features.world import space
from features.utils import SIR, generate_bodies_example


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
        self.size_x = size_x
        self.size_y = size_y
        self.world = World(size_x=size_x, size_y=size_y)

    def create_box(self):
        """
        Create a box splitting the "world" in 2 - visualisation (right) and UI (left)
        """
        box_x_boundary = self.size_x / 2
        box_points = [
            (self.size_x - 10, 10),
            (self.size_x - 10, self.size_y - 10),
            (box_x_boundary + 5, self.size_y - 10),
            (box_x_boundary + 5, 10),
        ]
        for i in range(4):  # Define bounderies and connect them
            seg = pymunk.Segment(
                space.static_body, box_points[i], box_points[(i + 1) % 4], 2,
            )
            seg.elasticity = 0.999
            space.add(seg)

    def add_bodies(self, bodies: list):
        """
        Adds bodies with shapes of circles to the simulation.
        :param bodies: [list of dictionaries with fields {"position_x","position_y","state"} describing bodies (subjects) to simulate.]
        :type bodies: list
        """
        space.gravity = 0, 0
        for i in range(len(bodies)):
            position = (
                bodies[i].get("position_x"),
                bodies[i].get("position_y"),
            )
            color = SIR[bodies[i].get("state").lower()].value
            subject = Subject(position=position, radius=10, color=color)
            space.add(subject.body, subject.shape)


if __name__ == "__main__":
    Game().create_box()
    bodies = generate_bodies_example(40)
    Game().add_bodies(bodies)
    World().run()
