import random
#from epidemic_simulation.GUI.features.utils import SIR


class SimulationManager:
    def __init__(
        self,
        #space,
        bodies: list,
        infection_r: float,
        infection_prob: float,
        sickness_duration: int,
    ):
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
        #self.space = space
        self.bodies = bodies
        self.infection_r = infection_r
        self.infection_prob = infection_prob
        self.bodies_to_change = []
        self.sickness_duration = sickness_duration

    def extract_position(self, body):
        x_coord = body["position_x"]
        y_coord = body["position_y"]
        return x_coord, y_coord

    def is_inside(self, susceptible_body, infected_body):
        """
        Method to determine whether susceptible subjects are in close proximity to infectious ones
        :param suscptible_body: [description]
        :type suscptible_body: dict
        :param infected_body: [description]
        :type infected_body: dict
        """
        infectious_x, infectious_y = susceptible_body.position
        susceptible_x, susceptible_y = infected_body.position
        if infectious_x==susceptible_x and infectious_y==susceptible_y:
            raise ValueError('Both bodies are in the same position')
        if self.infection_r<=0:
            raise ValueError('The Radius must be grater than 0')
        if (infectious_x - susceptible_x) * (infectious_x - susceptible_x) + (
            infectious_y - susceptible_y
        ) * (infectious_y - susceptible_y) <= self.infection_r ** 2:
            return True
        else:
            return False

    def is_infected(self):
        if self.infection_prob<0 or self.infection_prob>1:
            raise ValueError('Infection probability must be a number between o and 1')
        return random.choices(
            [False, True],
            weights=[1 - self.infection_prob, self.infection_prob],
            k=1,
        )[0]

    def calculate_bodies_to_change(self):
        self.suscpetible_bodies = self.find_bodies("susceptible")
        self.infected_bodies = self.find_bodies("infectious")
        for susceptible_body in self.suscpetible_bodies:
            # print(susceptible_body)
            for infected_body in self.infected_bodies:
                proximate = self.is_inside(susceptible_body, infected_body)
                # print(proximate)
                if proximate:
                    to_infect = self.is_infected()
                    if to_infect:
                        self.bodies_to_change.append(susceptible_body)
                        break

    def infect_susceptibles(self):
        for susceptible_body in self.bodies_to_change:
            for body in self.bodies:
                if body is susceptible_body:
                    body["state"] = "INFECTIOUS"

    def remove_infected(self):
        for infected_body in self.infected_bodies:
            for body in self.bodies:
                if body == infected_body:
                    body["counter"] += 1
                    if body["counter"] > self.sickness_duration:
                        body["state"] = "REMOVED"

    def find_bodies(self, target: str):
        target_bodies = []
        for body in self.space._get_bodies():
            body_x, body_y = body.position
            for shape in body.shapes:
                if shape.color == SIR[target.lower()].value:
                    target_bodies.append(body)
        return target_bodies
        # shape = body.shapes[0]
        # print(shape)
    
    def update_bodies(self):
        self.calculate_bodies_to_change()
        self.remove_infected()
        self.infect_susceptibles()

