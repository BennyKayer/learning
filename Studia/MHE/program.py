from classes.Item import Item
from classes.Backpack import Backpack

from algorithms.brute_force import brute_force
from algorithms.hill_climb import hill_climb_random, hill_climb_full
from algorithms.tabu_search import tabu_search
from algorithms.simmulated_annealing import simmulated_annealing
from algorithms.genetic_algorithm import genetic_algorithm

from algorithms_support.temperature_functions import select_temperature_function
from algorithms_support.genetic_support import generate_population, fitness, selection_tournament, mutation

from algorithms_in.in_out_from_console import in_out_from_console
from algorithms_in.generate_data_set import generate_data_set_with_input
from algorithms_in.setters import set_set_items, set_n_iterations, set_tabu_size, set_k, set_T, set_shall_print_goal, set_population_size, set_selection, set_crossover, set_termination, set_crossover_prob, set_mutation_prob
from algorithms_in.show_menu import show_menu

from algorithms_statistics.graph_items import graph_items
from algorithms_statistics.measure_time import measure_time
from algorithms_statistics.output_data import output_data
from algorithms_statistics.showdown import showdown

from algorithms_params.simmulated_annealing_params import simmulated_annealing_params
from algorithms_params.genetic_algorithm_params import genetic_algorithms_params

goal_calls = 0
if __name__ == "__main__":
    # Setup
    backpack = Backpack(15)

    algorithms = {
        "brute_force": brute_force,
        "hill_climb_full": hill_climb_full,
        "hill_climb_random": hill_climb_random,
        "tabu_search": tabu_search,
        "simmulated_annealing": simmulated_annealing,
        "genetic_algorithm": genetic_algorithm
    }

    menu_items = {
        1: "Generate data set",
        2: "Test algorithm",
        3: "Print goal function calls",
        4: "Algorithms Showdown",
        5: "Graph set_items",
        6: "Automated Params Simmulated Annealing",
        7: "Automated Params Genetic Algorithm"
    }

    associated = {
        1: "brute_force",
        2: "hill_climb_full",
        3: "hill_climb_random",
        4: "tabu_search",
        5: "simmulated_annealing",
        6: "genetic_algorithm"
    }

    # Input from console and defaults
    set_items, output_filename = in_out_from_console()

    while True:
        show_menu(menu_items)
        try:
            choice = int(
                input("\nSelect one of the options or press any other key to exit: "))
        except ValueError:
            break

        # QUIT
        if choice not in menu_items.keys():
            break

        # GENERATE DATA SET
        if menu_items[choice] == "Generate data set":
            generate_data_set_with_input()
            print("DATA SET GENERATED \n")

        # TEST ALGORITHM
        if menu_items[choice] == "Test algorithm":
            show_menu(associated)

            chosen_method = int(input("Waiting for an algorithm... "))
            while (chosen_method not in associated):
                chosen_method = int(input("Try again... "))

            if chosen_method == 1:
                params = {
                    "backpack": backpack,
                    "set_items": set_set_items()
                }
            if chosen_method == 2 or chosen_method == 3:
                params = {
                    "backpack": backpack,
                    "set_items": set_set_items(),
                    "n_iterations": set_n_iterations(),
                    "n_neighbours": 2
                }
            if chosen_method == 4:
                params = {
                    "backpack": backpack,
                    "set_items": set_set_items(),
                    "n_iterations": set_n_iterations(),
                    "n_neighbours": 2,
                    "tabu_size": set_tabu_size()
                }
            if chosen_method == 5:
                params = {
                    "backpack": backpack,
                    "set_items": set_set_items(),
                    "n_iterations": set_n_iterations(),
                    "n_neighbours": 2,
                    "temp_func": select_temperature_function(),
                    "k": set_k(),
                    "T": set_T(),
                    "shall_print_goal": set_shall_print_goal(),
                    "shall_graph": True
                }
            if chosen_method == 6:
                genetic_set_items = set_set_items()
                params = {
                    "population": generate_population(genetic_set_items, set_population_size()),
                    "fitness": fitness,
                    "set_items": genetic_set_items,
                    "capacity": backpack.capacity,
                    "selection": set_selection(),
                    "crossover": set_crossover(),
                    "mutation": mutation,
                    "termination": set_termination(),
                    "crossover_prob": set_crossover_prob(),
                    "mutation_prob": set_mutation_prob()
                }

            # Calculate, Time Complexity, Graph
            solution, time = measure_time(
                algorithm=algorithms[associated[chosen_method]], params=params)
            graph_items(solution)
            # Output
            # goalOrFitness = backpack.goal(solution) if chosen_method != 6 else fitness(
            #     backpack.capacity, solution)
            output_data(goal=backpack.goal(solution), solution=solution, filename=output_filename, time=time,
                        method=associated[chosen_method])
        # PRINT GOAL FUNCTION CALLS
        if menu_items[choice] == "Print goal function calls":
            print(f"Goal function called {backpack.goal_calls} times")

        # SHOWDOWN
        if menu_items[choice] == "Algorithms Showdown":
            showdown(backpack)

        # GRAPH CURRENT DATASET
        if menu_items[choice] == "Graph set_items":
            graph_items(set_items)

        # AUTOMATED PARAMS SIMMULATED
        if menu_items[choice] == "Automated Params Simmulated Annealing":
            simmulated_annealing_params(backpack, set_set_items())

        # AUTOMATED PARAMS GENETIC
        if menu_items[choice] == "Automated Params Genetic Algorithm":
            genetic_algorithms_params(backpack, set_items)
