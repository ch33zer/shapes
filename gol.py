#!/usr/bin/env python3

import pprint
from collections import namedtuple

Cell = namedtuple("Cell", ['x', 'y'])
grid = {}

def neighbors(c : Cell):
    # 8 neighbors
    # x +1 x -1, y+1, y-1
    neighbors = set()
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            n = Cell(c.x+x, c.y+y)
            if n != c:
                neighbors.add(n)
    return neighbors


#
#  ox
#  oo

def main():
    c1 = Cell(0, 0)
    grid[c1] = "empty"
   # pprint.pprint(grid)
    pprint.pprint(neighbors(c1))
    assert len(neighbors(c1)) == 8


if __name__ == "__main__":
    main()
