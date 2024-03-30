from collections import namedtuple
from enum import Enum

class Direction(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4

Point = namedtuple("Point", "x, y")