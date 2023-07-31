import sys
from queue import PriorityQueue


def priority_weight(graph):
    active_edge = [False for i in range(len(graph))]
    result = PriorityQueue()

    for i in range(len(graph)):
        for j in range(len(graph)):
            if not active_edge[j] and graph[i][j] != 0:
                result.put((graph[i][j], (i, j)))
        active_edge[i] = True

    return result


def parent_to_array(parent, weight):
    result = [[0 for i in range(len(parent))] for j in range(len(parent))]

    for i in range(len(parent)):
        if parent[i] != -1:
            result[i][parent[i]] = weight[i]
            result[parent[i]][i] = weight[i]

    return result


def parent_cluster_to_array(parent, weight):
    result = [[0 for i in range(len(parent))] for j in range(len(parent))]

    for i in range(len(parent)):
        if parent[i] != -1 and parent[i] != -2:
            result[i][parent[i]] = weight[i]
            result[parent[i]][i] = weight[i]

    return result


def prim_cluster(graph, start_edge, n):

    weight = [sys.maxsize for i in range(len(graph))]
    active_edge = [False for i in range(len(graph))]
    parent = [-1 for i in range(len(graph))]

    weight[start_edge] = 0
    min_vertex = sys.maxsize
    start = start_edge

    while not all(active_edge):
        for i in range(len(graph)):
            if not active_edge[i]:
                min_vertex = weight[i]
                start = i
        for i in range(len(graph)):
            if weight[i] < min_vertex and not active_edge[i]:
                min_vertex = graph[start][i]
                start = i

        active_edge[start] = True

        for i in range(len(graph[start])):
            if graph[start][i] < weight[i] and graph[start][i] != 0 and not active_edge[i]:
                weight[i] = graph[start][i]
                parent[i] = start

        test = 0
        for i in range(len(active_edge)):
            if active_edge[i]:
                test += 1
        if n<len(graph):
            if test == n:
                break
        if n == len(graph):
            if test == n-1:
                break

    if n < len(graph):
        for i in range(len(active_edge)):
            if not active_edge[i]:
                parent[i] = -2
                weight[i] = -1

    return parent, weight
