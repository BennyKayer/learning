from player import Player
from tools_of_trade import Card
class Human(Player):

    def __init__(self, balance):
        super().__init__()
        self.balance = balance

    def __str__(self):
        return "Human player"
