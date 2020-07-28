from enum import Enum


class Sliders(Enum):
    """
    An Enum to more efficiently call the different sliders that are part of the GUI of the simulation
    """

    subjects_n = {
        "title": "Number of People to simulate",
        "values_range": (10, 1000),
        "initial_value": 100,
        "type": int,
    }
    infection_p = {
        "title": "Probability Of Infection",
        "values_range": (0, 1),
        "initial_value": 0.1,
        "type": float,
    }
    infection_r = {
        "title": "Infection Radius",
        "values_range": (0, 20),
        "initial_value": 4,
        "type": float,
    }
    initial_carriers_p = {
        "title": "Proportion of Initial Carriers",
        "values_range": (0, 1),
        "initial_value": 0.1,
        "type": float,
    }
    sickness_duration = {
        "title": "Sickness Duration",
        "values_range": (1, 1000),
        "initial_value": 15,
        "type": int,
    }

