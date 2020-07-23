from random import randint

states = ["SUSCEPTIBLE", "INFECTIOUS", "REMOVED"]


def generate_bodies_example(n_bodies: int) -> list:
    bodies = []
    for i in range(n_bodies):
        bodies.append(
            {
                "position_x": randint(650, 1270),
                "position_y": randint(10, 690),
                "state": states[randint(0, 2)],
            }
        )
    return bodies
