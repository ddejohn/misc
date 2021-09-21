"""Random maze generator"""

import random
import numpy as np


class Maze:
    def __init__(self, x: int, y: int, rooms=False) -> None:
        self.shape = (x + 1, y + 1)
        self.maze = np.zeros(self.shape, dtype="uint8")
        self.grid = [(i, j) for i in range(1, x+1, 2) for j in range(1, y+1, 2)]
        self.path = [random.choice(self.grid)]
        self.position = self.path[0]
        self.grid.remove(self.position)
        self.history = []

        while self.grid:
            for probe_link in self.moves:
                probe, link = probe_link
                if probe in self.grid:
                    self.maze[tuple(zip(probe, link))] = 1
                    self.grid.remove(probe)
                    self.path.extend(probe_link)
                    self.position = probe
                    self.history.append(self.maze.copy())
                    break
            else:
                last_position = self.path.index(self.position)
                self.position = self.path[max(last_position - 1, 1)]
        self.history.extend([self.history[-1]]*50)

    @property
    def moves(self):
        x, y = self.position
        nsew = [[(x + 2, y), (x + 1, y)],
                [(x, y + 2), (x, y + 1)],
                [(x - 2, y), (x - 1, y)],
                [(x, y - 2), (x, y - 1)]]
        return random.sample(nsew, k=4)


# def build_maze():
#     """Generate a maze with rooms on intersections, corners, and dead-ends"""


#     x = random.choice((10, 12, 14, 18))
#     y = 148 // x
#     maze = np.zeros((x + 1, y + 1), dtype="uint8")
#     grid = [(i, j) for i in range(1, x + 1, 2) for j in range(1, y + 1, 2)]
#     path = [random.choice(grid)]
#     k = path[0]
#     grid.remove(k)

#     while grid:
#         n = len(path)
#         nsew = []

#         for i in range(4):
#             probe = tuple(map(add, moves[i][0], k))
#             link = tuple(map(add, moves[i][1], k))
#             nsew.append([probe, link])

#         random.shuffle(nsew)
#         for prb_lnk in nsew:
#             probe, link = prb_lnk
#             if probe in grid:
#                 maze[probe], maze[link] = 1, 1
#                 grid.remove(probe)
#                 path.extend(prb_lnk)
#                 break

#         if n == len(path):
#             k = path[max(path.index(k)-1, 1)]
#         else:
#             k = path[-1]


# def highlight_rooms(maze):
#     rooms = []
#     for coord in maze.path:
#         i, j = coord
#         neighbors = [
#             maze[i-1, j],
#             maze[i+1, j],
#             maze[i, j-1],
#             maze[i, j+1]
#         ]

#         if neighbors in NEIGHBOR_RULES:
#             rooms.append(coord)
#             maze[coord] = 2

#     return maze, rooms
