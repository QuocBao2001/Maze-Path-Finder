import copy


def DFS(matrix, start, end):
    visited_matrix = copy.deepcopy(matrix)
    parent = copy.deepcopy(matrix)
    stack = [start]
    count = 0
    while len(stack) != 0:
        count += 1
        current = stack.pop()
        visited_matrix[current[0]][current[1]] = '#'

        if current == end:
            break;

        neighbors = [[current[0], current[1] + 1],
                    [current[0] + 1, current[1]],
                    [current[0], current[1] - 1],
                    [current[0] - 1, current[1]]]

        for neighbor in neighbors:
            if (visited_matrix[neighbor[0]][neighbor[1]] != '#') and (matrix[neighbor[0]][neighbor[1]] != 'x'):
                parent[neighbor[0]][neighbor[1]] = current
                stack.append(neighbor)
    Path = [end]
    currentPoint = end
    while currentPoint != start:
        Path.insert(0, parent[currentPoint[0]][currentPoint[1]])
        currentPoint = parent[currentPoint[0]][currentPoint[1]]

    print('So vong lap DFS: ',count)
    return Path

def DFS_T(matrix, start, end, teleport_points):
    visited_matrix = copy.deepcopy(matrix)
    parent = copy.deepcopy(matrix)
    stack = [start]
    while len(stack) != 0:
        current = stack.pop()
        visited_matrix[current[0]][current[1]] = '#'

        if current == end:
            break;

        neighbors = [[current[0], current[1] + 1],
                    [current[0] + 1, current[1]],
                    [current[0], current[1] - 1],
                    [current[0] - 1, current[1]]]

        if current in teleport_points:
            for point in teleport_points:
                if point != current:
                    neighbors.append(point)

        for neighbor in neighbors:
            if (visited_matrix[neighbor[0]][neighbor[1]] != '#') and (visited_matrix[neighbor[0]][neighbor[1]] != 'x'):
                parent[neighbor[0]][neighbor[1]] = current
                stack.append(neighbor)
    Path = [end]
    currentPoint = end
    while currentPoint != start:
        Path.insert(0, parent[currentPoint[0]][currentPoint[1]])
        currentPoint = parent[currentPoint[0]][currentPoint[1]]

    return Path
