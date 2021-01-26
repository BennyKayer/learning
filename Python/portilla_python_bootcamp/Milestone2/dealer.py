'''
Automated dealer that will also serve as the deck management system
'''
from tools_of_trade import Card
from player import Player
import random

class Dealer(Player):
    '''
    Representation of an automated dealer
    '''
    def __init__(self):
        super().__init__()
        self.deck = []
        for suit in Card.suits:
            for value in Card.values:
                self.deck.append(Card(value, suit))

    def __str__(self):
        return "Dealer"

    def show_deck(self):
        '''
        Only for test purposes
        Prints deck in order
        '''
        deck_string = " "
        card_count = 1
        for card in self.deck:
            deck_string += f"{card_count} {card.value} of {card.suit}s, \n"
            card_count += 1
        print(deck_string)

    def shuffle_deck(self):
        '''
        2. Shuffle the deck
        OUTPUT: Shuffled deck
        '''
        random.shuffle(self.deck)

    def ask_for_bet(self, player):
        '''
        Modifies player's balance
        '''
        bet = int(input(f" How much do you want to bet? (${player.balance} available): "))
        while bet > player.balance:
            bet = int(input(f"Insufficient funds please try again: "))
        player.balance -= bet
        return bet * 2

    def deal_cards(self, being_dealt, amount):
        '''
        Adds given amount of cards to being_dealt's hand
        then removes them from a deck
        '''
        i = 0
        while i < amount:
            try:
                index = random.randrange(1, len(self.deck))
                being_dealt.hand.append(self.deck.pop(index))
                i += 1
            except IndexError:
                print(" No more cards to be dealt")
                break

    def hit_or_stand(self):
        answer = 0
        while answer not in [1, 2]:
            answer = int(input(" Do you wish to hit or stand?\n 1. Hit\n 2. Stand\n"))

        if answer == 1:
            return True
        else:
            return False

    def hit(self):
        '''
        Receive another card
        '''
        if self.hand_value() <= 17:
            self.hand.append(self.deck.pop())
            return True
        else:
            self.stand()
