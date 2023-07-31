import time

from utils import utils


def kruskal(graph):
    start_time = time.perf_counter()
    parent = [-1 for i in range(len(graph))]
    rank = [0 for i in range(len(graph))]
    weight = [0 for i in range(len(graph))]
    queue = utils.priority_weight(graph)

    count = 0
    while count < len(graph) and not queue.empty():
        w, (l, r) = queue.get()

        absolute_parent_r = r
        absolute_parent_l = l
        while parent[absolute_parent_r] != -1:
            absolute_parent_r = parent[absolute_parent_r]
        while parent[absolute_parent_l] != -1:
            absolute_parent_l = parent[absolute_parent_l]

        if absolute_parent_l != absolute_parent_r:
            if rank[absolute_parent_r] == rank[absolute_parent_l]:
                rank[absolute_parent_r] += 1
                parent[l] = r
                weight[l] = w
            if rank[absolute_parent_r] > rank[absolute_parent_l]:
                parent[l] = r
                weight[l] = w
            if rank[absolute_parent_r] < rank[absolute_parent_l]:
                parent[r] = l
                weight[r] = w
            count += 1

    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000


    print("Execution Time Kruskal: {:.6f} milliseconds".format(execution_time))
    return parent, weight
