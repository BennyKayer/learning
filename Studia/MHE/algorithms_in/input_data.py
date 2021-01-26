from pathlib import Path
from classes.Item import Item


def input_data(filename):
    '''
    Get data from a file in a form of:
    weight value
    and create a list of Items of out them
    '''
    data_folder = Path("data")
    list_of_items = []
    f = open(data_folder / f"{filename}.txt", mode="r")
    for line in f:
        line = line.split()
        list_of_items.append(Item(int(line[0]), int(line[1])))
    return list_of_items
