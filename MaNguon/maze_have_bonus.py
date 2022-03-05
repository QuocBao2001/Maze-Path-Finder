import copy
import math
from heuristic_function import manhattan_distance
from visualize_maze import visualize_maze

def a_star(input_matrix, h_matrix, start, end, endpoint):
    matrix = copy.deepcopy(input_matrix)
    if end != endpoint:
        matrix[endpoint[0]][endpoint[1]] = 'x'
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
    while len(priority_queue) != 0:
        current = priority_queue.pop(0)

        if current == end:
            break;

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


    Path = [end]
    currentPoint = end
    while currentPoint != start:
        Path.insert(0, parent[currentPoint[0]][currentPoint[1]])
        currentPoint = parent[currentPoint[0]][currentPoint[1]]

    return Path

flags = []
list_nodes = []

shorted_path = []
best_score = math.inf

def init(nodes):
    global flags
    global list_nodes
    global shorted_path
    global best_score

    flags = []
    list_nodes = []

    shorted_path = []
    best_score = math.inf

    for i in range(len(nodes)):
        flags.append(0)
    flags[0] = 1
    list_nodes.append(0)

def cost(list_nodes, edges, points):
    total = 0
    for i in range(len(list_nodes) - 2):
        total += edges[list_nodes[i]][list_nodes[i+1]] + points[list_nodes[i+1]][2]
    total += edges[list_nodes[-1]][list_nodes[-2]]
    return total


def find_shorted_path(nodes, points, edges, len_list):
    global flags
    global list_nodes
    global best_score
    global shorted_path
    if list_nodes[len_list - 1] == nodes - 1:
        current_cost = cost(list_nodes, edges, points)
        if current_cost < best_score:
            shorted_path = list_nodes[:]
            best_score = current_cost

    else:
        for i in range(nodes):
            if (flags[i] == 0):
                list_nodes.append(i)
                flags[i] = 1
                find_shorted_path(nodes, points, edges, len_list + 1)
                flags[i] = 0
                list_nodes.pop()




def eat_points(matrix, start, end, bonus_points):
    points = copy.deepcopy(bonus_points)
    points.insert(0,(start[0], start[1], 0))
    points.append((end[0], end[1], 0))

    Paths = []
    Scores = []
    for i in range(len(points)):
        Paths_from_i = []
        Scores_from_i = []
        for j in range(len(points)):
            Paths_from_i.append(None)
            Scores_from_i.append(None)
        Paths.append(Paths_from_i)
        Scores.append(Scores_from_i)

    for i in range(len(points)):
        Scores[i][i] = math.inf

    for i in range(len(points)):
        point_1 = [points[i][0], points[i][1]]
        for j in range(i+1,len(points)):
            point_2 = [points[j][0], points[j][1]]
            heu = manhattan_distance(matrix, end)
            Paths[i][j] = a_star(matrix, heu, point_1, point_2, end)
            if (j != len(points) - 1) and (j != 0):
                Paths[j][i] = a_star(matrix, heu, point_2, point_1, end)
            else:
                Paths[j][i] = Paths[i][j]
            Scores[i][j] = Scores[j][i] = len(Paths[j][i])

    init(points)
    find_shorted_path(len(points), points, Scores, 1)

    print("Cost: ", best_score)
    official_path = Paths[0][shorted_path[1]]
    for i in range(2,len(shorted_path)):
        official_path += Paths[shorted_path[i-1]][shorted_path[i]]

    return official_path
