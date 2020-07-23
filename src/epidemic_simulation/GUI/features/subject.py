import pymunk
from random import randint


class Subject:
    def __init__(self, position: tuple, radius: int, color: tuple):
        self.body = pymunk.Body(mass=1, moment=pymunk.inf)
        self.body.position = position
        impulse = (randint(-1000, 1000), randint(-1000, 1000))
        # impulse = (10, 10)
        self.body.apply_impulse_at_local_point(impulse)
        self.radius = radius
        self.color = color

    def set_shape(self):
        shape = pymunk.Circle(self.body, self.radius)
        shape.density = 0.01
        shape.elasticity = 1
        shape.friction = 0
        shape.color = self.color
        return shape

    @property
    def shape(self):
        return self.set_shape()
