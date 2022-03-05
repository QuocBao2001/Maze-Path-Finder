import os
from visualize_maze import visualize_maze
from read_file import read_file
from DFS import DFS, DFS_T
from BFS import BFS, BFS_T
from heuristic_function import euclidean_distance
from heuristic_function import manhattan_distance
from greedy_best_first_search import GBFS
from a_star import a_star
from maze_have_bonus import eat_points

def find_path(file_name, search_function = "DFS", heuristic = "manhattan_distances"):
    bonus_points, matrix = read_file(file_name)

    teleport_points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'T':
                teleport_points.append([i, j])

            if matrix[i][j] == 'S':
                start = [i, j]

            elif matrix[i][j] == ' ':
                if (i == 0) or (i == len(matrix) - 1) or (j == 0) or (j == len(matrix[0]) - 1):
                    end = [i, j]

    if heuristic == "manhattan_distances":
        h_matrix = manhattan_distance(matrix, end)
    else:
        h_matrix = euclidean_distance(matrix, end)

    if search_function == "DFS":
        route = DFS(matrix, start, end)
        print("Cost: ", len(route))
    if search_function == "BFS":
        route = BFS(matrix, start, end)
        print("Cost: ", len(route))
    if search_function == "GBFS":
        route = GBFS(matrix, h_matrix, start, end)
        print("Cost: ", len(route))
    if search_function == "A*":
        route = a_star(matrix, h_matrix, start, end)
        print("Cost: ", len(route))
    if search_function == "eat_points":
        route = eat_points(matrix,start,end,bonus_points)
    if search_function == "DFS_T":
        route = DFS_T(matrix,start,end,teleport_points)
    if search_function == "BFS_T":
        route = BFS_T(matrix, start, end, teleport_points)

    visualize_maze(matrix, bonus_points, start, end, route, teleport_points)