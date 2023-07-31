import asyncio
import sys
import time


def prim(graph):
    start_time = time.perf_counter()

    p, w = asyncio.run(prim_algorithm(graph,0))
    check_arr = []

    for i in range(len(p)):
        _, w_check = asyncio.run(prim_algorithm(graph, i))
        check_arr.append(sum(w_check))

    min_value = min(check_arr)
    index_value = check_arr.index(min_value)

    parent, weight = asyncio.run(prim_algorithm(graph,index_value))

    end_time = time.perf_counter()
    execution_time = (end_time - start_time)*1000

    print("Execution Time Prim: {:.6f} milliseconds".format(execution_time))
    return parent, weight


async def prim_algorithm(graph, start_edge):
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
        if test == len(graph) - 1:
            break

    return parent, weight