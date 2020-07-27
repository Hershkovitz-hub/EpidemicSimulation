import pygame
from epidemic_simulation.GUI.features import World, BACKGROUND_COLOR


class ParametersPresenter:
    def __init__(
        self, world: World, presentation_limits: list,
    ):
        """
        A class aimed at presenting and updating all simulation-related parameters
        :param world: [Simulation's World instance, conatining all window-related properties]
        :type world: World
        :param presentation_limits: [List of 4 tuples, indicating presentation part of the window]
        :type presentation_limits: list
        """
        self.world = world
        self.corners = presentation_limits
        self.font = pygame.font.Font("freesansbold.ttf", 32)

    def restart_presentation(self):
        """
        "Cleans" presentation-designated area before updating parameters
        """
        x, y = self.world.screen.get_size()
        self.world.screen.fill(BACKGROUND_COLOR, rect=(x / 2, 0, x, y))
        self.world.screen.fill(
            BACKGROUND_COLOR, rect=(0, 0.55 * self.corners[1][1], x, y),
        )

    def sort_subjects_into_presentation(self, subjects: list) -> dict:
        """
        Generate a presentable dictionary by counting subjects' states and divi
        :param subjects: [List of dictionaries discribing simulations' subjects]
        :type subjects: list
        :return: [Dictionary describing all subjects divided into "susceptibles","infectious" and "removed"]
        :rtype: dict
        """
        subjects_dict = {"Susceptibles": 0, "Infectious": 0, "Removed": 0}
        subjects_dict["Susceptibles"] = len(
            [
                subject
                for subject in subjects
                if subject.get("state").lower() == "susceptible"
            ]
        )
        subjects_dict["Infectious"] = len(
            [
                subject
                for subject in subjects
                if subject.get("state").lower() == "infectious"
            ]
        )
        subjects_dict["Removed"] = len(
            [
                subject
                for subject in subjects
                if subject.get("state").lower() == "removed"
            ]
        )
        return subjects_dict

    def place_texts(self, parameters: dict, subjects: list):
        """
        Place the parameters present in given dictionary at the top left part of the designated window
        :param parameters: [Dictionary with parameters' title as keys and their values al values]
        :type parameters: [dict]
        """
        self.restart_presentation()
        y_coordinate = 0.55 * self.corners[1][1]
        subjects_dict = self.sort_subjects_into_presentation(subjects)
        for key, value in subjects_dict.items():
            parameters[key] = value
        for title, value in parameters.items():
            self.add_text(
                title,
                value,
                self.corners[0][0] + 20,
                self.corners[0][1] + y_coordinate,
            )
            y_coordinate += 50

    def add_text(
        self, title: str, value: float, x_coordinate: int, y_coordinate: int
    ):
        """A method aimed at generating a text render instance to locate at specific coordinates at the simulation's window
        :param title: [parameter's title]
        :type title: str
        :param value: [parameter's value]
        :type value: float
        :param x_coordinate: [coordinate on X axis]
        :type x_coordinate: int
        :param y_coordinate: [coordinate on Y axis]
        :type y_coordinate: int
        
        :reference pygame.font: https://www.pygame.org/docs/ref/font.html
        """
        text = self.font.render(f"{title} : {value}", True, (255, 255, 255))
        self.world.screen.blit(text, (x_coordinate, y_coordinate))
