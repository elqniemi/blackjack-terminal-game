# This is a practice project for me to help tune my skills using Python3

# Libraries
from random import shuffle
from random import sample

# Create deck behavior to allow play with multiple decks
# First a function to generate a deck to avoid excessive typing
deck = []


def deck_appender(name, lst):
    for i in range(1, 10):
        lst.append([name, i])
    for i in range(4):
        lst.append([name, 10])


deck_appender('Hearts', deck)
deck_appender('Diamonds', deck)
deck_appender('Spades', deck)
deck_appender('Clubs', deck)

def blackjack_cards(decks_amt, deck):
    if type(decks_amt) is int:
            print(f"Amount of decks set at {decks_amt}")
    else:
        decks_amt = 5
        print("Invalid input, defaulted to 5 decks")

    playing_cards = decks_amt * deck
    shuffle(playing_cards)
    return playing_cards

class Player:

    def __init__(self, money, name):
        self.money = money
        self.name = name

    def deal(self, deck):
        self.deck = deck
        player_cards = sample(self.deck, 2)
        for i in self.deck:
            if player_cards[0] == i or player_cards[1]:
                self.deck.remove(i)

        print(f"{self.name}'s cards: \n")

        for i in player_cards:
            land = str(i[0])
            number = str(i[1])
            cards_open = f"{number} of {land}"
            print(cards_open)
        print('\n')
        return player_cards

    def hit(self, deck, player_cards):
        self.deck = deck
        hit_card = sample(self.deck, 1)
        player_cards = player_cards + hit_card

        for i in self.deck:
            if player_cards[0] == i or player_cards[1]:
                self.deck.remove(i)

        print(f"{self.name}'s cards: \n")

        for i in player_cards:
            land = str(i[0])
            number = str(i[1])
            cards_open = f"{number} of {land}"
            print(cards_open)
        print('\n')
        return player_cards



class Dealer(Player):
    def __init__(self):
        pass

    def deal(self, deck):
        self.deck = deck
        player_cards = sample(self.deck, 2)
        for i in self.deck:
            if player_cards[0] == i or player_cards[1]:
                self.deck.remove(i)

        print("Dealer's cards: \n")

        for i in player_cards:
            land = str(i[0])
            number = str(i[1])
            cards_open = f"{number} of {land}"
            print('Mystery')
            print(cards_open)
            break



multideck = blackjack_cards(1, deck)

p1 = Player(100, "Mike")
dealer = Dealer()
p1_cards = p1.deal(multideck)
p1_round1_cards = p1.hit(multideck, p1_cards)
p1_round2_cards = p1.hit(multideck, p1_round1_cards)
dealer_cards = dealer.deal(multideck)
