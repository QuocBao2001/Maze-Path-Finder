import copy
import math


def GBFS(matrix, h_matrix, start, end):
    visited_matrix = copy.deepcopy(matrix)
    parent = copy.deepcopy(matrix)
    visited_matrix[start[0]][start[1]] = '#';
    priority_queue = [start]
    count = 0
    while len(priority_queue) != 0:
        count += 1
        current = priority_queue.pop(0)
        visited_matrix[current[0]][current[1]] = '#'

        if current == end:
            break;

        neighbors = [[current[0], current[1] + 1],
                     [current[0] + 1, current[1]],
                     [current[0], current[1] - 1],
                     [current[0] - 1, current[1]]]

        for neighbor in neighbors:
            if (visited_matrix[neighbor[0]][neighbor[1]] != 'x') and (visited_matrix[neighbor[0]][neighbor[1]] != '#'):
                parent[neighbor[0]][neighbor[1]] = current;
                i = 0
                while i < len(priority_queue):
                    if h_matrix[neighbor[0]][neighbor[1]] < h_matrix[priority_queue[i][0]][priority_queue[i][1]]:
                        break
                    i += 1
                priority_queue.insert(i, neighbor)

    Path = [end]
    currentPoint = end
    while currentPoint != start:
        Path.insert(0, parent[currentPoint[0]][currentPoint[1]])
        currentPoint = parent[currentPoint[0]][currentPoint[1]]

    print('So vong lap GBFS: ', count)
    return Path
