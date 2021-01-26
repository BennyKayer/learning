import numpy as np
import random
from algorithms_support.generate_solution import generate_solution


def genetic_algorithm(params):
    population = params["population"]
    fitness = params["fitness"]
    capacity = params["capacity"]
    selection = params["selection"]
    crossover = params["crossover"]
    set_items = params["set_items"]
    mutation = params["mutation"]
    termination = params["termination"]
    crossover_prob = params["crossover_prob"]
    mutation_prob = params["mutation_prob"]
    informative = False

    # Initial Parameters
    fitnesses = [fitness(capacity, x) for x in population]
    population_info = {
        "population": population,
        "population_length": len(population),
        "iteration_count": 0,
        "capacity": capacity,
        "fitnesses": fitnesses,
        "mean_quality": np.mean(fitnesses),
        "quality_threshold": 20,  # specifically for data_4 default
        "contestants": len(population) // 4,
        "deviation_threshold": 2000,  # specifically for data_4 default
        "std_dev": np.std(fitnesses)
    }
    if informative:
        print("population", population)
        print("population length", len(population))

    for _ in iter(int, 1):
        next_gen = []
        for i in range(population_info["population_length"]):
            # For now they're parents
            child_a = selection(population_info)
            child_b = selection(population_info)
            if informative:
                print("child_a", child_a)
                print("child_b", child_b)

            cross = np.random.random_sample() <= crossover_prob
            if cross:
                child_a, child_b = crossover(child_a, child_b)
                if informative:
                    print(f"After crossover:\n{child_a}\n{child_b}")

            mutate = np.random.random_sample() <= mutation_prob
            if mutate:
                child_a = mutation(set_items, child_a)
                child_b = mutation(set_items, child_b)
                if informative:
                    print(f"After mutation:\n{child_a}\n{child_b}")

            fit_a = fitness(capacity, child_a)
            fit_b = fitness(capacity, child_b)
            better_child = child_a if fit_a > fit_b else child_b

            next_gen.append(better_child)
        if informative:
            print(
                f"Prev Gen ({len(population_info['population'])}):\n{population_info['population']}\nNext Gen ({len(next_gen)})\n{next_gen}")

        fitnesses = [fitness(capacity, x) for x in next_gen]
        mean_quality = np.mean(population_info["fitnesses"])
        std_dev = abs(np.std(fitnesses))

        # Update info
        population_info["fitnesses"] = fitnesses
        population_info["mean_quality"] = mean_quality
        population_info["population"] = next_gen
        population_info["std_dev"] = std_dev

        if (termination(population_info)):
            break

    return population_info["population"][population_info["fitnesses"].index(max(population_info["fitnesses"]))]
