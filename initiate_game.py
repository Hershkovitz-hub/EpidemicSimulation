import pygame
import random
import pymunk
import thorpy
from random import randint
from epidemic_simulation.GUI.features import Subject
from epidemic_simulation.GUI.features import Subject
from epidemic_simulation.GUI.features.world import World, space
from epidemic_simulation.GUI.features.world import space
from epidemic_simulation.simulation import SimulationManager
from epidemic_simulation.GUI.features.utils import (
    SIR,
    COLORS,
    generate_bodies_example,
    Boxes,
    SimulationIO,
)


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
        self.subjects = []
        self.bodies = []

    def pass_variables(self):
        print(self.world.carriers)

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
            subject = Subject(
                position=position, radius=10, color=color, properties=bodies[i]
            )
            self.subjects.append(subject)
            space.add(subject.body, subject.shape)

    def remove_bodies(self):
        space.remove(space._get_shapes())
        space.remove(space._get_bodies())
        self.subjects = []

    def update_parameters(self):
        self.world.infectious = 0
        self.world.susceptible = 0
        self.world.removed = 0
        for subject in self.subjects:
            color = subject.shape.color
            if color[0] == 255:
                self.world.infectious += 1
            elif color[1] == 255:
                self.world.susceptible += 1
            elif color[2] == 255:
                self.world.removed += 1

    def get_balls(self):
        print(t)


if __name__ == "__main__":
    game = Game()
    simulation_io = SimulationIO(
        game.world.screen,
        100,
        game.world.size_x,
        game.world.size_y,
        game.world.infection_p,
        game.world.infection_radius,
        game.world.carriers / 100,
        game.world.sickness_duration,
    )
    manager = SimulationManager(
        space,
        [subject.properties for subject in game.subjects],
        game.world.infection_radius,
        game.world.infection_p,
        game.world.sickness_duration,
    )
    while game.world.running:
        if simulation_io.carriers != game.world.carriers:
            game.remove_bodies()
            simulation_io = SimulationIO(
                game.world.screen,
                100,
                game.world.size_x,
                game.world.size_y,
                game.world.infection_p,
                game.world.infection_radius,
                game.world.carriers,
                game.world.sickness_duration,
            )
            bodies = simulation_io.generate_bodies()
            game.add_bodies(bodies)
            game.update_parameters()
        if (
            (manager.infection_r != game.world.infection_radius)
            or (manager.infection_prob != game.world.infection_p)
            or (manager.sickness_duration != game.world.sickness_duration)
        ):
            bodies = simulation_io.update_subjects(
                [subject.properties for subject in game.subjects], space
            )
            game.remove_bodies()
            game.add_bodies(bodies)
            game.update_parameters()
        game.world.run()
    pygame.quit()
