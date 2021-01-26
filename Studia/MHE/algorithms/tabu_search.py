from algorithms_support.generate_solution import generate_solution
from algorithms_support.neighbourhood import neighbourhood
from random import randint


def tabu_search(params):
    '''
    Finds the optimal solution in set_items using random tabu search algorithm

    Args:
        set_items: list of Item objects
        n_iterations: int, number of times to find best candidate
        in the neighbourhood
        tabu_size: int, indicates the maximux length of a tabu list

    Returns:
        list of Item objects
    '''
    backpack = params['backpack']
    set_items = params['set_items']
    n_iterations = params['n_iterations']
    n_neighbours = params['n_neighbours']
    tabu_size = params['tabu_size']

    best_solution = list(generate_solution(set_items))
    best_candidate = best_solution.copy()
    tabu = []
    tabu.append(best_solution)

    for i in range(n_iterations):

        neighbouring_solutions = neighbourhood(
            set_items, best_candidate, n_neighbours=n_neighbours)

        for candidate in neighbouring_solutions:
            if tabu.count(candidate) == 0:
                if backpack.goal(candidate) > backpack.goal(best_candidate):
                    best_candidate = list(candidate).copy()

        if backpack.goal(best_candidate) > backpack.goal(best_solution):
            best_solution = best_candidate.copy()

        tabu.append(best_candidate)
        if len(tabu) > tabu_size:
            tabu.pop(0)

    return best_solution
