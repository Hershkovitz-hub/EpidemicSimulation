from random import randint
from simulation_manager import SimulationManager

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

def test_extract_position(test_body):
    position=(55., 9.)
    x,y=test.extract_position(position)
    assert isinstance(x,float) 
    assert isinstance(y,float) 


