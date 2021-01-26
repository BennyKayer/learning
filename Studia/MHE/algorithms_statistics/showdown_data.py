from pathlib import Path


def showdown_data(method, set_length, time, value):
    '''
    Output data formatted for showdown
    '''
    out_folder = Path("out")
    raw_data = ""
    f = open(out_folder / f'showdown_{method}.txt', mode="a")
    raw_data += f"{method} "
    raw_data += f"{set_length} "
    raw_data += f"{time} "
    raw_data += f"{value} \n"
    f.write(raw_data)
    f.close()
