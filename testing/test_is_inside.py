from epidemic_simulation.simulation import SimulationManager
import pytest


@pytest.fixture
def test_data():
    test_calc=SimulationManager([],{'infection_r':100,'infection_p':0.99,'sickness_duration':6})
    return test_calc


def test_not_in_same_position(test_data):
    """
    test for when two bodies are in the same position.
    """
    susceptible_subject={'position':(0,0)}
    infectious_subject={'position':(0,0)}

    try:
        test_data.is_inside(susceptible_subject=susceptible_subject, infected_subject=infectious_subject)
    except ValueError:
        return True
    else: 
        return False

def test_positive_radius(test_data):
    """
    The Radius must be greater than 0
    """
    susceptible_subject={'position':(0,1)}
    infectious_subject={'position':(3,2)}
    try:
        test_data.infection_r=0
        test_data.is_inside(susceptible_subject=susceptible_subject, infected_subject=infectious_subject)
    except ValueError:
        try:
            test_data.infection_r=-1
            test_data.is_inside(susceptible_subject=susceptible_subject, infected_subject=infectious_subject)
        except ValueError:
            return True
    return False




