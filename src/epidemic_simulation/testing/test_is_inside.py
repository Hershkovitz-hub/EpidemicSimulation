from simulation_manager import SimulationManager

test_is_inside=SimulationManager([],0.6,0.7,6)

def test_same_position():
    """
    test for when two bodies are in the same position.
    """
    susceptible_body={'position_x':0,'position_y':0}
    infectious_body={'position_x':0,'position_y':0}

    try:
        test_is_inside.is_inside(susceptible_body=susceptible_body, infected_body=infectious_body)
    except ValueError:
        return True
    else: 
        return False

def test_positive_radius():
    """
    The Radius must be greater than 0
    """
    susceptible_body={'position_x':0,'position_y':1}
    infectious_body={'position_x':3,'position_y':2}
    try:
        test_is_inside.infection_r=0
        test_is_inside.is_inside(susceptible_body=susceptible_body, infected_body=infectious_body)
    except ValueError:
        try:
            test_is_inside.infection_r=-1
            test_is_inside.is_inside(susceptible_body=susceptible_body, infected_body=infectious_body)
        except ValueError:
            return True
    return False

print(test_same_position())
print(test_positive_radius())


