"""Random maze generator"""

from random import shuffle, choice
from operator import add
import matplotlib.pyplot as plt
from numpy import zeros as npz


def build():
    """Generate a maze with rooms on intersections, corners, and dead-ends"""

    rules = [
        [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0],
        [1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1],
        [1, 1, 1, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0],
        [0, 1, 0, 1]
    ]
    moves = [
        [(0, 2), (0, 1)], [(0, -2), (0, -1)],
        [(-2, 0), (-1, 0)], [(2, 0), (1, 0)]
    ]

    x = choice([10, 12, 14, 18])
    y = 148//x
    maze = npz((x+1, y+1), dtype=int)
    grid = [(i, j) for i in range(1, x+1, 2) for j in range(1, y+1, 2)]
    path = [choice(grid)]
    rooms = []
    k = path[0]
    grid.remove(k)

    while grid:
        n = len(path)
        nsew = []
        for i in range(4):
            probe = tuple(map(add, moves[i][0], k))
            link = tuple(map(add, moves[i][1], k))
            nsew.append([probe, link])
        shuffle(nsew)
        for prb_lnk in nsew:
            probe, link = prb_lnk
            if probe in grid:
                maze[probe], maze[link] = 1, 1
                grid.remove(probe)
                path.extend(prb_lnk)
                break
        if n == len(path):
            k = path[max(path.index(k)-1, 1)]
        else:
            k = path[-1]
    
    for coord in path:
        i, j = coord
        neighbors = [
            maze[i-1, j],
            maze[i+1, j],
            maze[i, j-1],
            maze[i, j+1]
        ]
        if neighbors in rules:
            rooms.append(coord)
            maze[coord] = 2
    
    return maze, rooms


if __name__ == "__main__":
    for i in range(100000):
        build()
        if i%1000 == 0:
            print(f"success {i}")
