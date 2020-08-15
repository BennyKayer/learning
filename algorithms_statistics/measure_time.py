def measure_time(**kwargs):
    import time
    start = time.time()
    result = kwargs['algorithm'](kwargs['params'])
    stop = time.time()
    diff = stop - start
    return (result, diff)
