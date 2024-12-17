from collections import deque
import sys

from AdventofCode.utilities.general import data_collect
from AdventofCode.utilities.grid import CLOCKWISE_DIRS,COUNTERCLOCKWISE_DIRS,Grid

raw = data_collect(2024,16)
grid = Grid(raw)
grid.print()