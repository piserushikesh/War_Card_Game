

class Player:

    def __init__(self,name):

        self.name = name
        self.all_cards = []


    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            #for multiple cards adding
            self.all_cards.extend(new_cards)
        else:
            #for single card adding
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'