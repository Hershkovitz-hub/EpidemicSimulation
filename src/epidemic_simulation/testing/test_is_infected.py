from simulation_manager import SimulationManager

test_is_infected=SimulationManager([],0.6,0.7,6)

def test_infection_prob_between_0_1():
    """
    infection_prob must be between 0 and 1
    """
    try:
        test_is_infected.infection_prob=-0.5
        test_is_infected.is_infected()
    except ValueError:
        try:
           test_is_infected.infection_prob=1.5
           test_is_infected.is_infected()
        except ValueError:
            return True
    return False


print((test_infection_prob_between_0_1()))