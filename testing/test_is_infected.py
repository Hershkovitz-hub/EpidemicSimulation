from epidemic_simulation.simulation import SimulationManager
import pytest

@pytest.fixture
def test_data():
    test_calc=SimulationManager([],{'infection_r':100,'infection_p':0.99,'sickness_duration':6})
    return test_calc

def test_infection_prob_between_0_1(test_data):
    """
    infection_prob must be between 0 and 1
    """
    try:
        test_data.infection_prob=-0.5
        test_data.is_infected()
    except ValueError:
        try:
           test_data.infection_prob=1.5
           test_data.is_infected()
        except ValueError:
            return True
    return False