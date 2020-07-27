from random import randint
from src.epidemic_simulation.simulation.simulation_manager import SimulationManager


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

def test_calc_len():
    bodies=generate_bodies_example(20)
    test=SimulationManager(bodies,12,0.2,6)
    test.calculate_bodies_to_change()
    assert len(test.bodies_to_change) == len(set(test.bodies_to_change))

def test_calc_status():
    bodies=generate_bodies_example(20)
    test=SimulationManager(bodies,12,0.2,6)
    test.calculate_bodies_to_change()
    assert set([body['state'] for body in test.bodies_to_change if body['state']])=='INFECTIOUS'