from epidemic_simulation.simulation import SimulationManager

test_is_inside=SimulationManager([],{'infection_r':0.6,'infection_p':0.7,'sickness_duration':6})

def test_same_position():
    """
    test for when two bodies are in the same position.
    """
    susceptible_subject={'position':(0,0)}
    infectious_subject={'position':(0,0)}

    try:
        test_is_inside.is_inside(susceptible_subject=susceptible_subject, infected_subject=infectious_subject)
    except ValueError:
        return True
    else: 
        return False

def test_positive_radius():
    """
    The Radius must be greater than 0
    """
    susceptible_subject={'position':(0,1)}
    infectious_subject={'position':(3,2)}
    try:
        test_is_inside.infection_r=0
        test_is_inside.is_inside(susceptible_subject=susceptible_subject, infected_subject=infectious_subject)
    except ValueError:
        try:
            test_is_inside.infection_r=-1
            test_is_inside.is_inside(susceptible_subject=susceptible_subject, infected_subject=infectious_subject)
        except ValueError:
            return True
    return False

print(test_same_position())
print(test_positive_radius())


