import itertools as it


def solution_combinations(options, start=1, stop=-1):
    '''
    Generates all solutions
    includes imposible one
    '''
    if stop == -1:
        stop = len(options) + 1

    all_combinations = []
    for i in range(start, stop + 1):
        all_combinations.extend(list(it.combinations(options, i)))
    return all_combinations
