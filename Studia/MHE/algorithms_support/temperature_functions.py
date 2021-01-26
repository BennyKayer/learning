from algorithms_in.show_menu import show_menu


def default_temperature(T, k):
    return T * abs(k)


def fast_temperature(T, k):
    import math
    return T / abs(math.log2(k))


def boltz_temperature(T, k):
    return T / abs(k ** 0.5)


def set_temperature_function(name):
    functions = {
        'default_temperature': default_temperature,
        'fast_temperature': fast_temperature,
        'boltz_temperature': boltz_temperature
    }
    return functions[name]


def select_temperature_function():
    functions = {
        1: 'default_temperature',
        2: 'fast_temperature',
        3: 'boltz_temperature'
    }
    show_menu(functions)
    try:
        func = int(input(" Select function..."))
        return functions[func]
    except:
        print("Invalid input setting default_temperature as a function")
        return functions[1]
