from matplotlib import pyplot as plt


def graph_items(options):
    '''
    Visual representation of the data
    '''
    options_weights = [x.weight for x in list(options)]
    options_values = [x.value for x in list(options)]

    plt.plot(options_values, options_weights, 'ro')
    plt.ylabel("weights")
    plt.xlabel("values")
    plt.show()
