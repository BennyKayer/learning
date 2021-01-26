from algorithms_support.temperature_functions import default_temperature, fast_temperature, boltz_temperature
from algorithms.simmulated_annealing import simmulated_annealing


def simmulated_annealing_params(backpack, set_items):
    n_iterations = [50, 100, 200, 300]
    temp_funcs = ["default_temperature",
                  "fast_temperature", "boltz_temperature"]
    ks = [0.85, 0.65, 0.40, 0.90]
    Ts = [2000, 1000, 500, 300]

    record = {

    }

    for n_i in n_iterations:
        for t_f in temp_funcs:
            for k in ks:
                for T in Ts:
                    goals = []
                    params = {
                        'backpack': backpack,
                        'set_items': set_items,
                        "n_iterations": n_i,
                        "temp_func": t_f,
                        "k": k,
                        "T": T,
                        "shall_print_goal": False,
                        "shall_graph": False
                    }
                    for i in range(5):
                        solution = simmulated_annealing(params)
                        goals.append(backpack.goal(solution))
                    avg_goal = sum(goals) / len(goals)
                    record[avg_goal] = {
                        "t_f": t_f,
                        "n_iterations": n_i,
                        "k": k,
                        "T": T,
                        "avg_goal": avg_goal
                    }
                    print(record[avg_goal])

    print("Most optimal parameters: ", record[max(record.keys())])
    return record[max(record.keys())]
