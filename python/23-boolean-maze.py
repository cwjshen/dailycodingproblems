# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board. 
# Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

# Given this matrix, a start coordinate, and an end coordinate, 
# return the minimum number of steps required to reach the end coordinate from the start. 
# If there is no possible path, then return null. You can move up, left, down, and right. 
# You cannot move through walls. You cannot wrap around the edges of the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]

# and start = (3, 0) (bottom left) and end = (0, 0) (top left), 
# the minimum number of steps required to reach the end is 7, 
# since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

from queue import *

def min_steps(board, start, end):
    steps = 0
    if start == end:
        return steps

    bfs_queue = Queue()

    for neighbor in get_neighbors(board, start):
        bfs_queue.put((neighbor, steps + 1))

    while not bfs_queue.empty():
        current = bfs_queue.get()
        if current[0] == end:
            return current[1]
        else:
            for neighbor in get_neighbors(board, current[0]):
                if board[neighbor[0]][neighbor[1]] == False:
                   bfs_queue.put((neighbor, current[1] + 1))

def get_neighbors(board, pos):
    neighbors = []

    m_dimension = len(board)
    n_dimension = len(board[0])

    pos_x = pos[0]
    pos_y = pos[1]

    # up-neighbor
    if 0 <= pos_x - 1 < m_dimension:
        up_neighbor = (pos_x - 1, pos_y)
        neighbors.append(up_neighbor)
    # right-neighbor
    if 0 <= pos_y + 1 < n_dimension:
        right_neighbor = (pos_x, pos_y + 1)
        neighbors.append(right_neighbor)
    # down-neighbor
    if 0 <= pos_x + 1 < m_dimension:
        down_neighbor = (pos_x + 1, pos_y)
        neighbors.append(down_neighbor)
    # left-neighbor
    if 0 <= pos_y - 1 < n_dimension:
        left_neighbor = (pos_x, pos_y - 1)
        neighbors.append(left_neighbor)

    return neighbors

f = False
t = True
board = [[f, f, f, f],
        [t, t, f, t],
        [f, f, f, f],
        [f, f, f, f]]

# print(get_neighbors(board, (3,3)))
print(min_steps(board, (3,0), (0,0)))