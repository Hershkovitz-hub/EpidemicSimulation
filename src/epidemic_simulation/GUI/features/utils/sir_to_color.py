from enum import Enum


class SIR(Enum):
    """
    An Enum aimed at simplify the conversion of SIR state to simulation's color
    """

    susceptible = (0, 255, 0, 0)
    infectious = (255, 0, 0, 0)
    removed = (0, 0, 255, 0)
