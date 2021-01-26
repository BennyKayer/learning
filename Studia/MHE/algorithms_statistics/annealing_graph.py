import matplotlib.pyplot as plt
from pathlib import Path


def annealing_graph(temperatures, values):
    graph_folder = Path("graphs")

    plt.plot(temperatures, values)
    plt.title("Values at given temperatures", fontsize=20, fontweight='bold')
    plt.xlabel("Temperature", fontsize=18, fontweight='bold')
    plt.ylabel("Z", fontsize=18, fontweight='bold')

    plt.gca().invert_xaxis()

    plt.savefig(graph_folder / "annealing_graph")
    plt.clf()
