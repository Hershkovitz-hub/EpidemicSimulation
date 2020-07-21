import pymunk
from random import randint


class Subject:
    def __init__(self, position: tuple, radius: int, color: tuple):
        self.body = pymunk.Body()
        self.body.position = position
        impulse = (randint(-50, 50), randint(-50, 50))
        # self.body.apply_impulse_at_local_point(impulse)
        self.radius = radius
        self.color = color

    def set_shape(self):
        shape = pymunk.Circle(self.body, self.radius)
        shape.density = 0.01
        shape.elasticity = 0.99
        shape.friction = 0.5
        shape.color = self.color
        return shape

    @property
    def shape(self):
        return self.set_shape()
