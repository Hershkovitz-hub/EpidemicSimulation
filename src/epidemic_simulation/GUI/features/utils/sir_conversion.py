from enum import Enum


class SIR(Enum):
    susceptible = (0, 255, 0, 0)
    infectious = (255, 0, 0, 0)
    removed = (0, 0, 255, 0)


class COLORS(Enum):
    a = "a"
    # (0,255,0,0) = "green"
    # (255, 0, 0, 0) = "red"
    # (0, 0, 255, 0) = "blue"

