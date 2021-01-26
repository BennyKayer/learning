from random import randint


def generate_solution(set_items, length=1):
    '''
    Generates some solution from the set_items with given length

    Args:
        set_items: list of Item objects
        length: int, length of the solution to generate

    Returns:
        list of Item objects
    '''
    set_items = list(set_items).copy()
    some_solution = []
    for i in range(length):
        if len(set_items) < 1:
            break
        rand_i = randint(0, len(set_items) - 1)
        some_solution.append(set_items.pop(rand_i))
    return some_solution
