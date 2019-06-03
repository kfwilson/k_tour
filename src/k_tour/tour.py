from heapq import heappush, heappop
from typing import List, Tuple
import numpy as np
from random import shuffle
import time

# | | | | | | | | |
# | | | | | | | | |
# | | |8| |1| | | |
# | |7| | | |2| | |
# | | | |K| | | | |
# | |6| | | |3| | |
# | | |5| |4| | | |
# | | | | | | | | |

OPTIONS = [(2, 1),    # 1
           (1, 2),    # 2
           (-1, 2),   # 3
           (-2, 1),   # 4
           (-2, -1),  # 5
           (-1, -2),  # 6
           (1, -2),   # 7
           (2, -1)]   # 8


class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.neighbors = self._build_neighbors()

    def rc(self, board_index: int) -> Tuple[int, int]:
        return board_index // self.board_size, board_index % self.board_size

    def board_index(self, position: Tuple[int, int]) -> int:
        return position[0] * self.board_size + position[1]

    def is_valid(self, position: Tuple[int, int]):
        return 0 <= position[0] < self.board_size and 0 <= position[1] < self.board_size

    def _build_neighbors(self) -> List[List]:
        neighbors = []
        for i in range(self.board_size ** 2):
            position = self.rc(i)
            possible_positions = [tuple(np.add(o, position)) for o in OPTIONS]
            position_neighbors = [self.board_index(n) for n in possible_positions if self.is_valid(n)]
            neighbors.append(position_neighbors)
        return neighbors

    def naive_tour(self, randomize=False):
        start = self.board_index((0, 0))

        route = [start]
        n_complete = self.board_size ** 2
        neighbors = self.neighbors.copy()
        visited = [0] * self.board_size ** 2
        visited[start] = 1

        if randomize:
            for n in neighbors:
                shuffle(n)

        def _naive_tour(board_index):
            if len(route) == n_complete:  # tour complete
                return True

            possible = [n for n in neighbors[board_index] if not visited[n]]
            for p in possible:
                route.append(p)
                visited[p] = 1
                if _naive_tour(p):
                    return True
                route.pop()
                visited[p] = 0

            return False

        _naive_tour(start)
        return route

    def smart_tour(self):
        start = self.board_index((0, 0))

        current = start
        n_complete = self.board_size ** 2
        visited = [0] * self.board_size ** 2
        route = []

        for i in range(n_complete):
            route.append(current)
            visited[current] = 1
            pq = []  # priority queue of neighbors

            for n in self.neighbors[current]:
                if not visited[n]:
                    n_neighbors = 0
                    for n_neighbor in self.neighbors[n]:
                        if not visited[n_neighbor]:
                            n_neighbors += 1
                    heappush(pq, (n_neighbors, n))

            if pq:
                count, current = heappop(pq)
            else:
                break

        return route

    def tour(self, tour_type):
        start = time.time()
        if tour_type == 'smart':
            route = self.smart_tour()
        elif tour_type == 'random':
            route = self.naive_tour(randomize=True)
        else:
            route = self.naive_tour(randomize=False)
        end = time.time()
        if len(route) < self.board_size ** 2:
            result = 'was unsuccessful.'
        else:
            result = f'resulted in the following route: {route}.'
        print(f'{tour_type.capitalize()} tour over board of size {self.board_size} took {end - start} seconds and {result}')
        return route

