from algorithms_support.genetic_support import *
from algorithms.genetic_algorithm import genetic_algorithm
import itertools as it


def genetic_algorithms_params(backpack, set_items):
    population_sizes = [5, 10]
    selections = [selection_tournament, selection_roullete]
    crossovers = [crossover_single, crossover_two]
    terminations = [termination_iteration,
                    termination_deviation, termination_mean_quality]
    crossover_probs = np.arange(0.0, 1.0, 0.1)
    mutation_probs = np.arange(0.0, 1.0, 0.1)

    record = {

    }
    capacity = backpack.capacity

    combs = it.product(population_sizes, selections, crossovers,
                       terminations, crossover_probs, mutation_probs)

    for comb in combs:
        p_s = comb[0]
        s = comb[1]
        c = comb[2]
        t = comb[3]
        c_p = comb[4]
        m_p = comb[5]

        solution_fitnesses = []
        solution_goals = []
        params = {
            'population': generate_population(set_items, p_s),
            'fitness': fitness,
            'capacity': capacity,
            'selection': s,
            'crossover': c,
            'set_items': set_items,
            'mutation': mutation,
            'termination': t,
            'crossover_prob': c_p,
            'mutation_prob': m_p
        }
        for i in range(5):
            solution = genetic_algorithm(params)
            solution_fitnesses.append(
                fitness(capacity, solution))
            solution_goals.append(backpack.goal(solution))

        avg_fitness = np.mean(solution_fitnesses)
        avg_goal = np.mean(solution_goals)
        record[avg_fitness] = {
            'population_size': p_s,
            'selection': s,
            'crossover': c,
            'termination': t,
            'crossover_prob': f'{c_p:.2f}',
            'mutation_prob': f'{m_p:.2f}',
            "avg_fitness": avg_fitness,
            "avg_goal": avg_goal
        }
        print(record[avg_fitness])

    print("Most optimal parameters: ", record[max(record.keys())])
    return record[max(record.keys())]
