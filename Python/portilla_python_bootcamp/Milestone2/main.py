'''
Game Play
To play a hand of Blackjack the following steps must be followed:
1. Create a deck of 52 cards
2. Shuffle the deck
3. Ask the Player for their bet
4. Make sure that the Player's bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer's cards, the other remains hidden
7. Show both of the Player's cards
8. Ask the Player if they wish to Hit, and take another card
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10. If a Player Stands, play the Dealer's hand.
11. The dealer will always Hit until the Dealer's value meets or exceeds 17
12. Determine the winner and adjust the Player's chips accordingly
13. Ask the Player if they'd like to play again
'''
import tools_of_trade as TOT
import dealer as DE
import human as PA

player = PA.Human(100)
#1 Create a deck of 52 cards (Dealer class creates it)
dealer = DE.Dealer()

game_is_running = True
while game_is_running:

    #2 Shuffle the deck
    dealer.shuffle_deck()
    #3 Ask the Player for their bet
    #4 Make sure that the Player's bet does not exceed their available chips
    money_to_win = dealer.ask_for_bet(player)
    #5 Deal two cards to the Dealer and two cards to the Player
    dealer.deal_cards(dealer, 2)
    dealer.deal_cards(player, 2)
    #6 Show only one of the Dealer's cards, the other remains hidden
    dealer.show_card(1)
    #7 Show both of the Player's cards
    player.show_card(2)
    #8 Ask the Player if they wish to Hit, and take another card
    #9 If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
    playing = True
    while playing and not player.is_bust():
        player_playing = dealer.hit_or_stand()
        if player_playing:
            player.hit(dealer.deck)
        elif player_playing == False:
            #10 If a Player Stands, play the Dealer's hand.
            #11. The dealer will always Hit until the Dealer's value meets or exceeds 17
            dealer_playing = dealer.hit()
        playing = player_playing or dealer_playing

    if dealer.is_bust():
        player.balance += money_to_win
    elif player.hand_value() > dealer.hand_value() and  not player.is_bust():
            player.balance += money_to_win

    #13. Ask the Player if they'd like to play again
    play_again = input(" Do you want to play again? Y/N")
    if play_again.lower() == "y":
        pass
    else:
        game_is_running = False
