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
    test_body=position[0]
    x,y=test.extract_position(test_body)
    assert isinstance(x,float) 
    assert isinstance(y,float) 

def test_calc_len():
    bodies=generate_bodies_example(20)
    test=SimulationManager(bodies,12,0.2,6)
    test.calculate_bodies_to_change()
    assert len(test.bodies_to_change) == len(set(test.bodies_to_change))

def test_calc_status():
    bodies=generate_bodies_example(20)
    test=SimulationManager(bodies,12,0.2,6)
    test.calculate_bodies_to_change()
    
    assert SUS==test.bodies_to_change

def test_infect_susceptibles():
    bodies=generate_bodies_example(20)
    test=SimulationManager(bodies,12,0.2,6)
    test.calculate_bodies_to_change()
    SUS_bodies = [body for body in test.bodies if body['state']=='SUSCEPTIBLE']
    to_change_bodies = test.bodies_to_change
    test.infect_susceptibles()
    SUS_bodies_post_function = [body for body in test.bodies if body['state']=='SUSCEPTIBLE']
    assert len(SUS_bodies)-len(to_change_bodies)==len(SUS_bodies_post_function)
    

bodies=generate_bodies_example(20)
test=SimulationManager(bodies,12,0.2,6)
test_body={'position_x':5,'position_y':9}
print([body['state'] for body in bodies if body['state']=='INFECTIOUS'])



