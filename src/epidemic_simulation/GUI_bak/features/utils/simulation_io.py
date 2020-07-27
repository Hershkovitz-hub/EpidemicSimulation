from random import randint, choices
from epidemic_simulation.simulation import SimulationManager

states = ["SUSCEPTIBLE", "INFECTIOUS", "REMOVED"]


class SimulationIO:
    def __init__(
        self,
        screen,
        n_bodies: int,
        size_x: int,
        size_y: int,
        infection_p: float,
        infection_radius: float,
        carriers: int,
        sickness_duration: int,
    ):
        """
        A class to manage all I/O to and from the simulation branch of the epidemic simulation project
        :param screen: [the screen in which the simulation takes place]
        :type screen: [type]
        :param size_x: [Screen's width]
        :type size_x: int
        :param size_y: [Screen's height]
        :type size_y: int
        :param infection_p: [probability of infection as stated by the user]
        :type infection_p: float
        :param infection_radius: [radius of infection]
        :type infection_radius: float
        :param carries: [number of initial carriers]
        :type carries: int
        """
        self.screen = screen
        self.n_bodies = n_bodies
        self.size_x = size_x
        self.size_y = size_y
        self.infection_p = infection_p
        self.infection_radius = infection_radius
        self.carriers = carriers
        self.sickness_duration = sickness_duration

    def generate_bodies(
        self,
        position_x: float = None,
        position_y: float = None,
        counter: int = None,
        is_carrier: bool = None,
    ):
        bodies = []
        for i in range(self.n_bodies):
            body = {
                "position_x": position_x
                if position_x
                else randint(self.size_x / 2 + 20, self.size_x - 30),
                "position_y": position_y
                if position_y
                else randint(10, self.size_y - 20),
                "counter": counter if counter else 0,
            }
            is_carrier = (
                is_carrier
                if is_carrier
                else choices(
                    [False, True], weights=[1 - self.carriers, self.carriers],
                )[0]
            )
            if is_carrier:
                body["state"] = "INFECTIOUS"
                body["counter"] = randint(0, int(self.sickness_duration))
            else:
                body["state"] = "SUSCEPTIBLE"
            bodies.append(body)
        return bodies

    def update_subjects(self, bodies: list, space):
        manager = SimulationManager(
            space,
            bodies,
            self.infection_radius,
            self.infection_p,
            self.sickness_duration,
        )
        manager.update_bodies()
        # manager.find_bodies("infectious")
        return manager.bodies

