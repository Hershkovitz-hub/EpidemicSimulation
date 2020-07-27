import random

# from epidemic_simulation.GUI.features.utils import SIR


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
        self.sickness_duration = parameters.get("sickness_duration")

    def sort_subjects_into_groups(self):
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
        :param suscptible_body: [description]
        :type suscptible_body: dict
        :param infected_body: [description]
        :type infected_body: dict
        """
        infectious_x, infectious_y = susceptible_subject.get("position")
        susceptible_x, susceptible_y = infected_subject.get("position")
        x_distance = (infectious_x - susceptible_x) ** 2
        y_distance = (infectious_y - susceptible_y) ** 2
        distance = (y_distance + x_distance) ** 0.5
        if distance <= self.infection_r ** 2:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        return random.choices(
            [False, True],
            weights=[1 - self.infection_p, self.infection_p],
            k=1,
        )[0]

    def calculate_subjects_to_change(self):
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
        for susceptible_subject in self.subjects_to_change:
            for subject in self.subjects:
                if subject is susceptible_subject:
                    subject["state"] = "INFECTIOUS"

    def remove_infected(self):
        for infected_subject in self.infectious:
            for subject in self.subjects:
                if subject == infected_subject:
                    subject["counter"] += 1
                    if subject["counter"] > self.sickness_duration:
                        subject["state"] = "REMOVED"

    def update_subjects(self):
        self.calculate_subjects_to_change()
        self.remove_infected()
        self.infect_susceptibles()
        return self.subjects

