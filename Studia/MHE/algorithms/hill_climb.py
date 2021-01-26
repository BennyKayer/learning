from algorithms_support.neighbourhood import neighbourhood
from algorithms_support.generate_solution import generate_solution

from random import randint


def hill_climb_full(params):
    '''
    Finds the optimal solution in set_items using full hill climb algorithm

    Args:
        set_items: list of Item objects
        n_iterations: int, number of times to search the neighbourhood

    Returns:
        list of Item objects
    '''
    backpack = params['backpack']
    set_items = params['set_items']
    n_iterations = params['n_iterations']
    n_neighbours = params['n_neighbours']

    current_solution = list(generate_solution(set_items))

    for i in range(n_iterations):

        neighbours = neighbourhood(
            set_items, current_solution, n_neighbours=n_neighbours)
        for neighbour in neighbours:
            if backpack.goal(neighbour) > backpack.goal(current_solution):
                current_solution = list(neighbour).copy()

    return current_solution


def hill_climb_random(params):
    '''
    Finds the optimal solution in set_items using random hill climb algorithm

    Args:
        set_items: list of Item objects
        n_iterations: int, number of times to draw from neighbourhood

    Returns:
        list of Item objects
    '''
    backpack = params['backpack']
    set_items = params['set_items']
    n_iterations = params['n_iterations']
    n_neighbours = params['n_neighbours']

    current_solution = list(generate_solution(set_items))

    for i in range(n_iterations):

        neighbour = neighbourhood(
            set_items, current_solution, rand=True, n_neighbours=n_neighbours)

        if backpack.goal(neighbour) > backpack.goal(current_solution):
            current_solution = neighbour

    return current_solution
