from utils import utils


def cluster(graph, n):
    result = []
    for i in range(len(graph)):
        p, w = utils.prim_cluster(graph, i, n)
        result.append(utils.parent_cluster_to_array(p, w))
    return result

