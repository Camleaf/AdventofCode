from collections import deque
import sys

from general import data_collect
from grid import CLOCKWISE_DIRS,COUNTERCLOCKWISE_DIRS,Grid

raw = data_collect(2024,16)
grid = Grid(raw)
grid.print()