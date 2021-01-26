from algorithms_support.generate_solution import generate_solution
from algorithms_support.neighbourhood import neighbourhood
from algorithms_support.temperature_functions import set_temperature_function

from algorithms_statistics.annealing_graph import annealing_graph


import numpy as np


def simmulated_annealing(params):
    '''
    Let s = s0
    For k = 0 through kmax (exclusive):
        T ← temperature( kmax/(k+1) )
        Pick a random neighbour, snew ← neighbour(s)
        If P(E(s), E(snew), T) ≥ random(0, 1):
        s ← snew
    Output: the final state s
    '''
    backpack = params['backpack']
    set_items = params['set_items']
    n_iterations = params['n_iterations']
    temp_func = set_temperature_function(params['temp_func'])
    k = params['k']
    T = params['T']
    shall_print_goal = params['shall_print_goal']
    shall_graph = params["shall_graph"]

    # Init & Graph
    solution = generate_solution(set_items)
    temperatures = []
    curr_goals = []

    for i in range(n_iterations):

        neighbour = neighbourhood(
            set_items, solution, rand=True, n_neighbours=2)
        # Neighbour appraisal
        curr_goal = backpack.goal(solution)
        poss_goal = backpack.goal(neighbour)

        if shall_print_goal:
            print("Iteration #", i)
            print("curr_goal: ", curr_goal)
            print("poss_goal: ", poss_goal)

        rn = np.random.rand()
        acceptance_probability = 1 / (np.exp(poss_goal - curr_goal) / T)

        if poss_goal >= curr_goal or rn >= acceptance_probability:
            solution = neighbour

        # Data for graph
        temperatures.append(T)
        curr_goals.append(curr_goal)

        T = temp_func(T, k)

    if shall_graph:
        annealing_graph(temperatures, curr_goals)

    return solution
