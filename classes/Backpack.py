class Backpack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.goal_calls = 0

    # Helper Methods

    def goal(self, solution):
        '''
        Calculates goal value of a given solution.

        Args:
            solution: list of Item objects

        Returns:
            integer that represents solution's "quality"
            -1 represents an imposible solution
            (items weight more than backpack is able to carry)
        '''
        self.goal_calls += 1

        items_value = 0
        items_weight = 0
        for item in solution:
            items_value += item.value
            items_weight += item.weight
        return items_value if items_weight <= self.capacity else -len(solution)
