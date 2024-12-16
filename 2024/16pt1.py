from collections import deque

from AdventofCode.utils.general import data_collect
from AdventofCode.utils.grid import CLOCKWISE_DIRS,COUNTERCLOCKWISE_DIRS,Grid

raw = data_collect(2024,16)
grid = Grid(raw)
grid.print()