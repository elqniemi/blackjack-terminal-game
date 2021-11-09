# This is a practice project for me to help tune my skills using Python3

# Libraries
from random import shuffle
from random import sample

# Create deck behavior to allow play with multiple decks
# First a function to generate a deck to avoid excessive typing
deck = []


def deck_appender(name, lst):
    for i in range(1, 14):
        lst.append([name, i])


deck_appender('Hearts', deck)
deck_appender('Diamonds', deck)
deck_appender('Spades', deck)
deck_appender('Clubs', deck)


class BlackjackCards:

    def __init__(self, decks_amt):
        self.decks_amt = decks_amt
        try:
            type(self.decks_amt) == int()
        except:
            self.decks_amt = 5
            print("Invalid input, defaulted to 5 decks")
        playing_cards = shuffle([self.decks_amt * deck])

        return playing_cards


class Player:

    def __init__(self, money):
        self.money = money

    def deal(self, deck):
        return sample(deck, 2)

    def hit(self, deck):
        pass

class Dealer(Player):


