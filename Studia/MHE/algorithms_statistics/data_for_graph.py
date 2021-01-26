from pathlib import Path
from matplotlib import pyplot as plt


def data_for_graph(filename):
    data_folder = Path("out")
    graph_folder = Path("graphs")
    f = open(data_folder / f"{filename}.txt", mode="r")
    next(f)

    sizes = []
    times = []
    values = []

    for line in f:
        line = line.split()
        name = line[0]
        sizes.append(int(line[1]))
        times.append(float(line[2]))
        values.append(float(line[3]))

    plt.plot(sizes, times, 'ro')
    plt.title(f"{name} czasy obliczeń a rozmiary zadania")
    plt.xlabel("Rozmiar")
    plt.ylabel("Czas ")
    plt.savefig(graph_folder / f"{name}_time_size_plot.png")

    plt.clf()

    plt.plot(sizes, values, 'ro')
    plt.title(f"{name} jakość rozwiązania a rozmiary zadania")
    plt.xlabel("Rozmiar")
    plt.ylabel("Jakość")
    plt.savefig(graph_folder / f"{name}_value_size_plot.png")

    plt.clf()
