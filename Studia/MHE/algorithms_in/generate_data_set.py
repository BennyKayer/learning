from pathlib import Path
from random import randint


def generate_data_set_with_input():
    try:
        name = input("Enter name for the data set: ")
        if len(name) < 2:
            name = "default"
    except:
        name = "default"

    try:
        n_of_datum = int(input("Enter number of data points: "))
    except:
        n_of_datum = 20

    try:
        max_weight = int(input("Enter maximum weight of an item: "))
    except:
        max_weight = 15

    try:
        max_value = int(input("Enter maximum value of an item: "))
    except:
        max_value = 30

    return generate_data_set(name=name, n_of_datum=n_of_datum, max_weight=max_weight, max_value=max_value)


def generate_data_set(name, n_of_datum, max_weight, max_value):
    '''
    Generates data set with give name, length as well as range for the datum points

    Args:
        name: string, name of a file to be put into data
        n_of_datum: int, how many Item's in data set
        max_weight: int, maximum weight for an Item
        max_value: int, maximum value for an Item
    Returns:
        nothing
    '''

    data_folder = Path("data")
    f = open(data_folder / f"{name}.txt", mode="w")
    while n_of_datum > 0:
        weight = str(int(randint(0, max_weight)))
        value = str(int(randint(0, max_value)))
        f.write(f"{weight} {value}")
        f.write("\n")
        n_of_datum -= 1
