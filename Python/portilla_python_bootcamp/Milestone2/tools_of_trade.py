'''
Representations of physical tools needed to play Black Jack
'''

class Card:
    '''
    Representation of a card
    '''
    values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7,
              "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}
    suits = ("Heart", "Spade", "Club", "Diamond")
    def __init__(self, value, suit):
        self.value = value #value is a string at this point
        self.suit = suit
    def __str__(self):
        return f"{self.value} of {self.suit}s"
    #Doesn't work for some reason
    # def __add__(self, other):
    #     val = self.value.split()[0]
    #     return self.values.get(val) + other
    # def __iadd__(self, other):
    #     val = self.value.split()[0]
    #     return self.values.get(val) + other

# class Deck:
#     '''
#     Deck from which dealer deals cards according to player's actions
#     '''
#     def __init__(self):
#         # Can I shorten it to one liner?
#         self.deck = []
#         for suit in Card.suits:
#             for value in Card.values:
#                 self.deck.append(Card(value, suit))
#     def __str__(self):
#         deck_string = " "
#         for card in self.deck:
#             deck_string += f"{card.value} of {card.suit}, "
#         return deck_string
