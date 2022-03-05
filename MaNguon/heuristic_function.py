import copy
import math


def euclidean_distance(matrix, end):
    result = copy.deepcopy(matrix)
    for i in range(len(result)):
        for j in range(len(result[0])):
            if result[i][j] != '*':
                result[i][j] = math.sqrt(pow((end[0] - i), 2) + pow((end[1] - j), 2))
    return result


def manhattan_distance(matrix, end):
    result = copy.deepcopy(matrix)
    for i in range(len(result)):
        for j in range(len(result[0])):
            if result[i][j] != '*':
                result[i][j] = abs(end[0] - i) + abs(end[1] - j)
    return result
