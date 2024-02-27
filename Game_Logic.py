from Deck import Deck
from Player import Player


class Game_Logic:


    player_one = Player("One")
    player_two = Player("Two")

    new_deck = Deck()
    new_deck.shuffle()

    for x in range(26):
         player_one.add_cards(new_deck.deal_one())
         player_two.add_cards(new_deck.deal_one())


    game_on = True

    round_num = 0

    while game_on:

        #for counting round
        round_num+= 1
        print(f'Round {round_num}')

        if len(player_one.all_cards) == 0:
            print('Player one, out of cards! Player Two Wins!')
            game_on= False
            break

        if len(player_two.all_cards) == 0:
            print('Player two, out of cards! Player One Wins!')
            game_on= False
            break


        # Start a new round
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        at_war = True

        while at_war:

            if player_one_cards[-1].value > player_two_cards[-1].value:

                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)

                at_war = False

            elif player_one_cards[-1].value < player_two_cards[-1].value:

                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)

                at_war = False

            else:

                print('WAR!')

                if len(player_one.all_cards) < 5 :
                    print("Player One unable to declare war")
                    print("Player Two WINS!")
                    game_on = False
                    break

                elif len(player_two.all_cards) < 5 :
                    print("Player Two unable to declare war")
                    print("Player One WINS!")
                    game_on = False
                    break

                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

