import copy

def BFS(matrix, start, end):
    visited_matrix = copy.deepcopy(matrix)
    parent = copy.deepcopy(matrix)
    visited_matrix[start[0]][start[1]] = '#';
    queue = [start]
    count = 0
    while len(queue) != 0:
        count += 1
        current = queue.pop(0)

        if current == end:
            break;

        neighbors = [[current[0], current[1] + 1],
                    [current[0] + 1, current[1]],
                    [current[0], current[1] - 1],
                    [current[0] - 1, current[1]]]

        for neighbor in neighbors:
            if (visited_matrix[neighbor[0]][neighbor[1]] != '#') and (visited_matrix[neighbor[0]][neighbor[1]] != 'x'):
                visited_matrix[neighbor[0]][neighbor[1]] = '#'
                parent[neighbor[0]][neighbor[1]] = current
                queue.append(neighbor)
    Path = [end]
    currentPoint = end
    while currentPoint != start:
        Path.insert(0, parent[currentPoint[0]][currentPoint[1]])
        currentPoint = parent[currentPoint[0]][currentPoint[1]]

    print('So vong lap BFS: ',count)

    return Path

def BFS_T(matrix, start, end, teleport_points):
    visited_matrix = copy.deepcopy(matrix)
    parent = copy.deepcopy(matrix)
    visited_matrix[start[0]][start[1]] = '#';
    queue = [start]
    count = 0
    while len(queue) != 0:
        count += 1
        current = queue.pop(0)
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
                visited_matrix[neighbor[0]][neighbor[1]] = '#'
                parent[neighbor[0]][neighbor[1]] = current;
                queue.append(neighbor)
    Path = [end]
    currentPoint = end
    while currentPoint != start:
        Path.insert(0, parent[currentPoint[0]][currentPoint[1]])
        currentPoint = parent[currentPoint[0]][currentPoint[1]]

    print('So vong lap BFS: ',count)

    return Path