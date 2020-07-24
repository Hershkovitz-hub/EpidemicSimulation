from random import randint, choices

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

    def generate_bodies(self):
        bodies = []
        for i in range(self.n_bodies):
            body = {
                "position_x": randint(self.size_x / 2 + 20, self.size_x - 30),
                "position_y": randint(10, self.size_y - 20),
            }
            is_carrier = choices(
                [False, True], weights=[1 - self.carriers, self.carriers],
            )[0]
            if is_carrier:
                body["state"] = "Infectious"
            else:
                body["state"] = "Susceptible"
            bodies.append(body)
        return bodies

