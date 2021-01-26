from algorithms_in.input_data import input_data


def in_out_from_console():

    try:
        set_items = input_data(sys.argv[1])
    except:
        print("No data filename provided   - setting default...")
        set_items = input_data("default")

    try:
        output_filename = sys.argv[2]
    except:
        print("No output filename provided   - setting default...")
        output_filename = "default"

    return set_items, output_filename
