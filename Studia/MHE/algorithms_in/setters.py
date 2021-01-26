from algorithms_in.input_data import input_data


def set_n_iterations():
    try:
        n_iterations = int(
            input("Enter number of times that algorithm should iterate: "))
    except:
        print("Invalid input, setting default 10")
        n_iterations = 10
    return n_iterations


def set_tabu_size():
    try:
        tabu_size = int(input("Enter maximum tabu length: "))
    except:
        print("Invalid input, setting default 10")
        tabu_size = 10
    return tabu_size


def set_set_items():
    try:
        filename = input("Enter the data filename: ")
        if len(filename) == 0:
            filename = "default"
    except:
        print("Invalid input, setting default - default.txt")
        filename = "default"
    return input_data(filename)


def set_k():
    try:
        k = float(input("Enter k - ratio at which temperature will cool: "))
    except:
        print("Invalid input, setting default 0.85...")
        k = 0.85
    return k


def set_T():
    try:
        T = int(input("Enter T - an initial temperature for simmulated_annealing: "))
    except:
        print("Invalid input, setting default 1000...")
        T = 1000
    return T


def set_shall_print_goal():
    try:
        shall_print_goal = bool(
            int(input("Should I print goal values?(0, 1): ")))
    except ValueError:
        print("Invalid input, setting default False...")
        shall_print_goal = False
    return shall_print_goal


def set_population_size():
    try:
        population_size = int(
            input("Enter population size for genetic algorithm: "))
    except:
        population_size = 6
        print(f"Invalid input, setting default {population_size}")

    return population_size


def set_selection():
    from algorithms_support.genetic_support import selection_tournament, selection_roullete
    from algorithms_in.show_menu import show_menu

    selections = {
        "selection_tournament": selection_tournament,
        "selection_roulette": selection_roullete
    }
    associated = {
        1: "selection_tournament",
        2: "selection_roulette"
    }

    try:
        show_menu(associated)
        selection = selections[associated[int(
            input("Choose selection method: "))]]
    except:
        print("Invalid input, setting default selection_tournament")
        selection = selection_tournament
    return selection


def set_crossover():
    from algorithms_support.genetic_support import crossover_single, crossover_two
    from algorithms_in.show_menu import show_menu

    crossovers = {
        "crossover_single": crossover_single,
        "crossover_two": crossover_two
    }
    associated = {
        1: "crossover_single",
        2: "crossover_two"
    }

    try:
        show_menu(associated)
        crossover = crossovers[associated[int(
            input("Choose crossover method: "))]]
    except:
        print("Invalid input, setting default crossover_single")
        crossover = crossover_single
    return crossover


def set_termination():
    from algorithms_support.genetic_support import termination_iteration, termination_mean_quality, termination_deviation
    from algorithms_in.show_menu import show_menu

    terminations = {
        "termination_iteration": termination_iteration,
        "termination_mean_quality": termination_mean_quality,
        "termination_deviation": termination_deviation
    }
    associated = {
        1: "termination_iteration",
        2: "termination_mean_quality",
        3: "termination_deviation"
    }

    try:
        show_menu(associated)
        termination = terminations[associated[int(
            input("Choose termination condition: "))]]
    except:
        print("Invalid input, setting default termination_iteration")
        termination = termination_iteration
    return termination


def set_crossover_prob():
    try:
        crossover_prob = abs(float(input("Enter crossover probability: ")))
    except:
        print("Invalid input, setting default 1.0")
        crossover_prob = 1.0
    return crossover_prob


def set_mutation_prob():
    try:
        mutation_prob = abs(float(input("Enter mutation probability: ")))
    except:
        mutation_prob = 0.05
        print(f"Invalid input, setting default {mutation_prob}")

    return mutation_prob
