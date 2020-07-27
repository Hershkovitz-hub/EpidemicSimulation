import pymunk
import pygame
from pymunk.vec2d import Vec2d
from epidemic_simulation.GUI.features import World, BACKGROUND_COLOR
from epidemic_simulation.GUI.features.utils.sir_to_color import SIR
from random import randint, choices


class SubjectManager:
    def __init__(self, world: World, parameters: dict):
        """
        A class to create, update and manage all subjects-related matters of the simulation
        :param world: [Simulation World instance, conatining all window-related properties]
        :type world: World
        :param parameters: [Dictionary containing all world-related parameters]
        :type parameters: dict
        """
        self.world = world
        self.width, self.height = self.world.screen.get_size()
        self.parameters = parameters
        self.space = self.world.space
        self.extract_initial_parameters()

    def extract_initial_parameters(self):
        """
        Extracts parameter relevant for initiating world's subjects
        """
        self.subjects_n = self.parameters.get("subjects_n")
        self.initial_carriers_p = self.parameters.get("initial_carriers_p")

    def restart_visualisation(self):
        """
        "Cleans" visualisation-designated area before updating subjects
        """
        self.world.screen.fill(
            BACKGROUND_COLOR, rect=(self.width / 2, 0, self.width, self.height)
        )

    def initiate_subjects(self):
        """
        initiate subjects according to world's parameters
        """
        self.subjects = []
        for subject in range(self.subjects_n):
            position = Vec2d(
                randint(self.width / 2 + 20, self.width - 20),
                randint(20, self.height - 20),
            )
            counter = 0
            is_carrier = choices(
                [False, True],
                weights=[1 - self.initial_carriers_p, self.initial_carriers_p],
            )[0]
            subject_dict = {
                "position": position,
                "state": "SUSCEPTIBLE",
                "counter": 0,
            }
            if is_carrier:
                subject_dict["state"] = "INFECTIOUS"
            subject_dict["body"] = self.add_body_to_subject(subject_dict)
            subject_dict["shape"] = self.add_shape_to_body(subject_dict)
            self.subjects.append(subject_dict)
        self.add_subjects_to_space()

    def add_body_to_subject(self, subject_dict: dict) -> pymunk.Body:
        """
        Generate pymunk.Body according to parameters presented in subject_dict
        :param subject_dict: [Dictionary describing the subject]
        :type subject_dict: dict
        :return: [pymunk.Body instance to be added to simulation's space]
        :rtype: pymunk.Body
        """
        body = pymunk.Body(mass=1, moment=pymunk.inf)
        body.position = subject_dict.get("position")
        impulse = (randint(-1000, 1000), randint(-1000, 1000))
        body.apply_impulse_at_local_point(impulse)
        return body

    def add_shape_to_body(self, subject_dict: dict) -> pymunk.Circle:
        """
        Adds shape (circle) to pymunk.Body instance, color is defined by subject's state declared in subject_dict
        :param subject_dict: [Dictionary describing the subject]
        :type subject_dict: dict
        :return: [pymunk.Circle instance to be attached to a pymunk.Body instance]
        :rtype: pymunk.Circle
        """
        shape = pymunk.Circle(body=subject_dict.get("body"), radius=5)
        shape.density = 0.01
        shape.elasticity = 1
        shape.friction = 0
        shape.color = SIR[subject_dict.get("state").lower()].value
        return shape

    def add_subjects_to_space(self):
        """
        Adds subjects to simulation's space according to generated dictionary
        """
        self.restart_visualisation()
        for subject_dict in self.subjects:
            self.world.space.add(
                subject_dict.get("body"), subject_dict.get("shape")
            )

    def clear_all_subjects(self):
        """
        Clears all subjects upon chnage of certain parameters
        """
        for body in self.world.space._get_bodies():
            self.world.space.remove(body, body.shapes)

    def update_subjects(self, parameters: dict):
        """
        Main method, aimed at updating subjects' parameters at each iteration of the simulation
        :param parameters: ["New" (although possibly the same) simulation's parameters dictionary]
        :type parameters: dict
        """
        if (
            parameters.get("subjects_n") != self.subjects_n
            or parameters.get("initial_carriers_p") != self.initial_carriers_p
        ):
            self.clear_all_subjects()
            self.parameters = parameters
            self.extract_initial_parameters()
            self.initiate_subjects()
        for body in self.world.space._get_bodies():
            for subject_dict in self.subjects:
                if body == subject_dict.get("body"):
                    subject_dict["position"] = body._get_position()
