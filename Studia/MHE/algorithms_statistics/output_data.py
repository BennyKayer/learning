from pathlib import Path


def output_data(goal, solution, filename, time, method, mode="w+"):
        '''
        Saves the results in the form of (goal value, time and method used)
        Solution value: {goal's value}
        {[solution[0], solution[1], ..., solution[len(solution) - 1]]}
        Time: {time}
        Method: {method}
        to the file

        Args:
            solution: list of Item objects
            filename: string with output's filename
            time: float with time in seconds
            method: string with name of the methos used

        Returns:
            nothing
        '''
        out_folder = Path("out")
        f = open(out_folder / f'{filename}.txt', mode)
        formated_solution = f"Solution value: {goal} \n"
        for item in solution:
            formated_solution += f"[{item}]"
        formated_solution += f"\n Time: {time}"
        formated_solution += f"\n Method: {method}"
        formated_solution += "\n"
        f.write(formated_solution)
        f.close()
