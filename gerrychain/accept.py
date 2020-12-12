from .random import random


def always_accept(partition):
    return True


def cut_edge_accept(partition):
    """Always accepts the flip if the number of cut_edges increases.
    Otherwise, uses the Metropolis criterion to decide.

    :param partition: The current partition to accept a flip from.
    :return: True if accepted, False to remain in place

    """
    bound = 1

    # if the partition has a parent, the upper bound is either 1 or a ratio of cut edges, whichever is smaller
    if partition.parent is not None:
        bound = min(1, len(partition.parent["cut_edges"]) / len(partition["cut_edges"]))

    # returns true if some random number is less than the bound (if the bound is 1, this will always be true)
    return random.random() < bound
