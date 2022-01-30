import random

class Card:
    def __init__(self):
        self.card1num = random.randint(1, 14)
        self.card1num_card_suit = '♡'
        self.card2num = random.randint(1, 13)
        self.card2num_card_suit = '♢'
    def draw_card(self):
        # Generate a ramdom number bwteen 1 and 14 for previous card
        self.card2num = self.card1num
        self.card2num_card_suit = self.card1num_card_suit
        self.card1num = random.randint(1, 14)
        self.rand_card_suit()
    def rand_card_suit(self):
        # Generate a random suit for each card
        suit_temp = random.randint(1, 4)
        if suit_temp == 1:
            self.card1num_card_suit = '♡'
        elif suit_temp == 2:
            self.card1num_card_suit = '♢'
        elif suit_temp == 3:
            self.card1num_card_suit = '♤'
        else:
            self.card1num_card_suit = '♧'


# class Card:
#     def __init__(self):
#         self.cardnumber = random.randint(1, 14)


