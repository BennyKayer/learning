from algorithms_support.solution_combinations import solution_combinations


def brute_force(params):
    '''
    Generate all possible combinations and find the one with the highest value
    '''
    backpack = params['backpack']
    set_items = params['set_items']

    combinations = solution_combinations(set_items)
    best_combination_value = 0
    best_combination = []
    for combination in combinations:
        combination_value = backpack.goal(combination)
        if combination_value > best_combination_value:
            best_combination_value = combination_value
            best_combination = combination
    return best_combination
