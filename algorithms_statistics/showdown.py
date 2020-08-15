
from pathlib import Path
from algorithms_in.input_data import input_data

from algorithms.hill_climb import hill_climb_random, hill_climb_full
from algorithms.tabu_search import tabu_search

from algorithms_support.temperature_functions import default_temperature

from algorithms_statistics.measure_time import measure_time
from algorithms_statistics.showdown_data import showdown_data
from algorithms_statistics.data_for_graph import data_for_graph


def showdown(backpack):
    out_folder = Path("out")

    f = open(out_folder / "showdown_hill_climb_full.txt", mode="w+")
    f.write("metoda rozmiar czas_sredni wynik_sredni \n")
    f.close()

    f = open(out_folder / "showdown_tabu_search.txt", mode="w+")
    f.write("metoda rozmiar czas_sredni wynik_sredni \n")
    f.close()

    f = open(out_folder / "showdown_hill_climb_random.txt", mode="w+")
    f.write("metoda rozmiar czas_sredni wynik_sredni \n")
    f.close()

    items_sets = [input_data("data_2"), input_data(
        "data_3"), input_data("data_4"), input_data("data_5")]
    algorithms = [hill_climb_full, tabu_search, hill_climb_random]
    algorithms_names = {
        hill_climb_full: "hill_climb_full",
        tabu_search: "tabu_search",
        hill_climb_random: "hill_climb_random"
    }
    for i_set in items_sets:
        for algorithm in algorithms:
            times = []
            goals = []
            i = 25
            while i > 0:
                i -= 1
                solution, diff = measure_time(
                    algorithm=algorithm, params={
                        'backpack': backpack,
                        'set_items': i_set,
                        'n_iterations': 100,
                        "n_neighbours": 2,
                        "tabu_size": 10,
                        "temp_func": "default_temperature"
                    })
                times.append(diff)
                goals.append(backpack.goal(solution))

            showdown_data(method=algorithms_names[algorithm], set_length=len(
                i_set), time=sum(times) / len(times), value=sum(goals) / len(goals))

    data_for_graph("showdown_tabu_search")
    data_for_graph("showdown_hill_climb_full")
    data_for_graph("showdown_hill_climb_random")
