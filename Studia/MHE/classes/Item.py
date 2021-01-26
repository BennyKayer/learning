class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"Item({self.weight},{self.value})"

    __str__ = __repr__

    def __eq__(self, other):
        return int(self.weight) == int(other.weight) and int(self.value) == int(other.value)

    def __lt__(self, other):
        return int(self.value) < int(other.value)

    def __gt__(self, other):
        return int(self.value) > int(other.value)
