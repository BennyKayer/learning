from .generate_solution import generate_solution
import random
import numpy as np


def generate_population(set_items, population_size):
    population = []
    for i in range(population_size):
        ran_len = random.randint(1, population_size)
        population.append(generate_solution(set_items, ran_len))

    return population


def fitness(capacity, items):
    items_value = sum([x.value for x in items])
    items_weight = sum([x.weight for x in items])

    return items_value ** 2 if items_weight <= capacity else items_value


def crossover_single(parent_a, parent_b):
    try:
        shorter = min(len(parent_a), len(parent_b))
        slice_point = np.random.randint(low=0, high=shorter)
        #print(f"from {slice_point}")

        child_a = parent_a[:slice_point:] + parent_b[slice_point::]
        child_b = parent_b[:slice_point:] + parent_a[slice_point::]

    except ValueError:
        #print("Too short")
        return parent_a, parent_b

    #print("parents", parent_a, parent_b)
    #print("children", child_a, child_b)

    return child_a, child_b


def crossover_two(parent_a, parent_b):
    try:
        shorter = min(len(parent_a), len(parent_b))

        slice_1 = np.random.randint(low=0, high=shorter)
        slice_2 = np.random.randint(low=(slice_1 + 1), high=shorter)
        #print(f"from {slice_1} to {slice_2}")

        child_a = parent_a[:slice_1:] + \
            parent_b[slice_1:slice_2:] + parent_a[slice_2::]
        child_b = parent_b[:slice_1:] + \
            parent_a[slice_1:slice_2:] + parent_b[slice_2::]
    except ValueError:
        #print("Too short")
        return parent_a, parent_b

    #print("parents", parent_a, parent_b)
    #print("children", child_a, child_b)

    return child_a, child_b


def mutation(set_items, specimen):
    exclude = [x for x in set_items if x not in specimen]
    # print("set_items", set_items)
    # print("specimen", specimen)
    # print("exclude", exclude)

    if len(exclude) == 0:
        print("Specimen is including whole set - unable to mutate")
        return specimen

    ran_i = np.random.randint(low=0, high=len(exclude))
    dust = exclude[ran_i]

    ran_i = np.random.randint(low=0, high=len(specimen))
    # print("Not mutated yet", specimen)
    specimen.pop(ran_i)
    specimen.append(dust)
    return specimen


def selection_roullete(population_info):
    population = population_info["population"]
    fitnesses = population_info["fitnesses"]

    fit_sum = np.array(fitnesses).sum()
    prob_sum = 0
    probs = []
    for specimen in population:
        specimen_fit = fitnesses[population.index(specimen)]
        prob = (specimen_fit / fit_sum)
        prob_sum += prob
        probs.append(prob)

    for i in range(1, len(probs) - 1):
        rn = random.uniform(0.0, 1.0)
        if probs[i - 1] < rn < probs[i]:
            return population[i]

    # just in case
    return population[0]


def selection_tournament(population_info):
    population = population_info["population"]
    capacity = population_info["capacity"]
    contestants = population_info["contestants"]

    chosen = []
    for i in range(contestants):
        ran_i = np.random.randint(0, len(population))
        chosen.append(population[ran_i])
    fitnesses = [fitness(capacity, x) for x in chosen]

    return chosen[fitnesses.index(max(fitnesses))]


def termination_iteration(population_info):
    iteration_count = population_info["iteration_count"]
    population_length = population_info["population_length"]

    terminate = iteration_count == population_length
    population_info["iteration_count"] += 1

    return terminate


def termination_mean_quality(population_info):
    quality_threshold = population_info["quality_threshold"]
    mean_quality = population_info["mean_quality"]

    terminate = quality_threshold <= mean_quality

    return terminate


def termination_deviation(population_info):
    deviation_threshold = population_info["deviation_threshold"]
    std_dev = population_info["std_dev"]

    # print("std_dev", std_dev)
    # print("deviation_threshold", deviation_threshold)

    terminate = std_dev <= deviation_threshold

    return terminate
