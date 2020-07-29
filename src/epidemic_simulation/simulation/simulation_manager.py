import random


class SimulationManager:
    def __init__(self, subjects: list, parameters: dict):
        """
        A class to manage all simulation and calculation regarding the epidemic.
        :param bodies: [description]
        :type bodies: list
        :param infection_r: [description]
        :type infection_r: float
        :param infection_prob: [description]
        :type infection_prob: float
        :param day: [description]
        :type day: int
        """
        self.subjects = subjects
        self.sort_subjects_into_groups()
        self.infection_r = parameters.get("infection_r")
        self.infection_p = parameters.get("infection_p")
        self.subjects_to_change = []
        self.sickness_duration = parameters.get("sickness_duration") + 1000

    def sort_subjects_into_groups(self):
        """
        Divides subjects into SIR (susceptible, infectious, removed) groups
        """
        self.infectious = [
            subject
            for subject in self.subjects
            if subject.get("state").lower() == "infectious"
        ]
        self.susceptibles = [
            subject
            for subject in self.subjects
            if subject.get("state").lower() == "susceptible"
        ]
        self.removed = [
            subject
            for subject in self.subjects
            if subject.get("state").lower() == "removed"
        ]

    def is_inside(
        self, susceptible_subject: dict, infected_subject: dict
    ) -> bool:
        """
        Method to determine whether susceptible subjects are in close proximity to infectious ones
        :param suscptible_subject: [A dictionary containing susceptible subject's parameters]
        :type suscptible_subject: dict
        :param infected_subject: [A dictionary containing infectious subject's parameters]
        :type infected_subject: dict
        :raises ValueError: [Upon two subjects located at the same coordinated]
        :raises ValueError: [Upon world's infectious radius parameter being negative]
        :return: [whether subjects are in proximity to one another]
        :rtype: bool
        """
        infectious_x, infectious_y = susceptible_subject.get("position")
        susceptible_x, susceptible_y = infected_subject.get("position")
        if infectious_x == susceptible_x and infectious_y == susceptible_y:
            raise ValueError("Both bodies are in the same position")
        if self.infection_r <= 0:
            raise ValueError("The Radius must be grater than 0")
        x_distance = (infectious_x - susceptible_x) ** 2
        y_distance = (infectious_y - susceptible_y) ** 2
        distance = (y_distance + x_distance) ** 0.5
        if distance <= self.infection_r ** 2:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """

        :raises ValueError: [Upon world's infection probability parameter being negative]
        :return: [wheter the subject is to be infected]
        :rtype: bool
        """
        if self.infection_p < 0 or self.infection_p > 1:
            raise ValueError(
                "Infection probability must be a number between o and 1"
            )
        return random.choices(
            [False, True],
            weights=[1 - self.infection_p, self.infection_p],
            k=1,
        )[0]

    def calculate_subjects_to_change(self):
        """
        Use world's and subjects' parameter to determine which of the current subjects is to be infected
        """
        for susceptible_subject in self.susceptibles:
            for infected_subject in self.infectious:
                proximate = self.is_inside(
                    susceptible_subject, infected_subject
                )
                if proximate:
                    to_infect = self.is_infected()
                    if to_infect:
                        self.subjects_to_change.append(susceptible_subject)
                        break

    def infect_susceptibles(self):
        """
        Change subjects' state from "susceptible" to "infectious"
        """
        for susceptible_subject in self.subjects_to_change:
            for subject in self.subjects:
                if subject is susceptible_subject:
                    subject["state"] = "INFECTIOUS"

    def remove_infected(self):
        """
        Change subjects' state from "infectious" to "removed"
        """
        for infected_subject in self.infectious:
            for subject in self.subjects:
                if subject == infected_subject:
                    subject["counter"] += 1
                    if subject["counter"] > self.sickness_duration:
                        subject["state"] = "REMOVED"

    def update_subjects(self) -> list:
        """
        Uses class's methods to update subjects' states
        :return: [Updated subjects list]
        :rtype: [list]
        """
        self.calculate_subjects_to_change()
        self.remove_infected()
        self.infect_susceptibles()
        return self.subjects

