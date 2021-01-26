import random
from algorithms_support.solution_combinations import solution_combinations
from algorithms_support.generate_solution import generate_solution


def neighbourhood(set_items, current_solution, rand=False, n_neighbours=2):
    '''
    Generates neighbouring Item for every item in the solution

    Args:
        set_items: list of Item objects
        current_solution: list of Item objects
        rand: bool indicates whether we want to turn neighbours
        into all possible combinations of them

    Returns:
        list of Items' lists
    '''
    neighbours = []
    for i in range(n_neighbours):
        item = set_items[random.randint(0, len(set_items) - 1)]
        if item not in neighbours and item not in current_solution:
            neighbours.append(item)

    neighbours.extend(current_solution)
    if rand:
        ran_len = random.randint(
            len(current_solution) - 1, len(current_solution) + 1)
        if ran_len == 0:
            ran_len = len(neighbours) // 2
        return list(generate_solution(neighbours, ran_len))
    else:

        return solution_combinations(neighbours, start=len(current_solution) - 1, stop=len(current_solution) + 1)
