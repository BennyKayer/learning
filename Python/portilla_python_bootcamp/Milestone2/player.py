'''
This will serve as the base class for both human and dealer
'''
import tools_of_trade
class Player:
    '''
    Set of actions that game players can perform
    '''
    def __init__(self):
        self.hand = []

    def hit(self, deck):
        '''
        Receive another card
        '''
        print(" I'll hit")
        self.hand.append(deck.pop())

    def stand(self):
        '''
        Stop receiving cards
        '''
        print(" I'll wait")
        return False


    def show_card(self, amount):
        '''
        Prints given amount of cards
        '''
        print(self)
        for i in range(amount):
            print(self.hand[i])

    def hand_value(self):
        hand_val = 0
        for card in self.hand:
            #As the card's value is a string at this point we need to convert it
            card = card.value.split()[0]
            hand_val += tools_of_trade.Card.values.get(card)
        return hand_val

    def is_bust(self):
        hand_val = self.hand_value()
        print(f"{self}'s hand value is {hand_val}'")
        return hand_val > 21
