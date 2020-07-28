from random import randint
import pytest
from epidemic_simulation.simulation import SimulationManager

@pytest.fixture
def test_data():
    test_bodies=[{'position': (748, 634), 'state': 'INFECTIOUS'}, {'position': (1137, 351), 'state': 'SUSCEPTIBLE'}, {'position': (1017, 464), 'state': 'INFECTIOUS'}, {'position': (901, 368), 'state': 'INFECTIOUS'}, {'position': (1227, 549), 'state': 'REMOVED'}, {'position': (1193, 194), 'state': 'REMOVED'}, {'position': (654, 165), 'state': 'SUSCEPTIBLE'}, {'position': (1212, 260), 'state': 'INFECTIOUS'}, {'position': (820, 198), 'state': 'SUSCEPTIBLE'}, {'position': (826, 480), 'state': 'INFECTIOUS'}, {'position': (955, 58), 'state': 'REMOVED'}, {'position': (914, 78), 'state': 'INFECTIOUS'}, {'position': (1239, 86), 'state': 'SUSCEPTIBLE'}, {'position': (1132, 532), 'state': 'SUSCEPTIBLE'}, {'position': (1042, 41), 'state': 'REMOVED'}, {'position': (713, 590), 'state': 'SUSCEPTIBLE'}, {'position': (1169, 572), 'state': 'REMOVED'}, {'position': (778, 70), 'state': 'SUSCEPTIBLE'}, {'position': (906, 554), 'state': 'SUSCEPTIBLE'}, {'position': (797, 598), 'state': 'INFECTIOUS'}]
    test_calc=SimulationManager(test_bodies,{'infection_r':100,'infection_p':1,'sickness_duration':6})
    return test_calc

def test_calculate_subjects_to_change_uniques(test_data):
    test_data.calculate_subjects_to_change()
    set_bodies=set([body['position'] for body in test_data.subjects_to_change])
    assert len(set_bodies)==len(test_data.subjects_to_change)
    
def test_calculate_subjects_to_change_only_susceptible(test_data):
    test_data.calculate_subjects_to_change()
    assert set([body['state'] for body in test_data.subjects_to_change if body['state']])=={'SUSCEPTIBLE'}
    