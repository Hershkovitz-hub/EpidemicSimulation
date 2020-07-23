from enum import Enum


class SIR(Enum):
    susceptible = (0, 255, 0, 0)
    infectious = (255, 0, 0, 0)
    removed = (0, 0, 255, 0)

