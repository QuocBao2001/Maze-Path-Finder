import copy
import math


def a_star(matrix, h_matrix, start, end):
    parent = copy.deepcopy(matrix)

    depth = copy.deepcopy(matrix)
    for i in range(len(depth)):
        for j in range(len(depth[0])):
            depth[i][j] = math.inf
    depth[start[0]][start[1]] = 0

    f_matrix = copy.deepcopy(matrix)
    for i in range(len(f_matrix)):
        for j in range(len(f_matrix[0])):
            f_matrix[i][j] = math.inf
    f_matrix[start[0]][start[1]] = h_matrix[start[0]][start[1]]

    priority_queue = [start]
    count = 0
    while len(priority_queue) != 0:
        count += 1
        current = priority_queue.pop(0)

        if current == end:
            break

        neighbors = [[current[0], current[1] + 1],
                     [current[0] + 1, current[1]],
                     [current[0], current[1] - 1],
                     [current[0] - 1, current[1]]]

        for neighbor in neighbors:
            if matrix[neighbor[0]][neighbor[1]] != 'x':
                temp_depth = depth[current[0]][current[1]] + 1
                temp_f = temp_depth + h_matrix[neighbor[0]][neighbor[1]]

                if temp_f < f_matrix[neighbor[0]][neighbor[1]]:
                    depth[neighbor[0]][neighbor[1]] = temp_depth
                    f_matrix[neighbor[0]][neighbor[1]] = temp_f
                    parent[neighbor[0]][neighbor[1]] = current
                    i = 0
                    while i < len(priority_queue):
                        if f_matrix[neighbor[0]][neighbor[1]] < f_matrix[priority_queue[i][0]][priority_queue[i][1]]:
                            break
                        i += 1
                    priority_queue.insert(i, neighbor)


    path = [end]
    current_point = end
    while current_point != start:
        path.insert(0, parent[current_point[0]][current_point[1]])
        current_point = parent[current_point[0]][current_point[1]]

    print('So vong lap A*: ', count)
    return path
