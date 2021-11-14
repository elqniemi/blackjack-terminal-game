# This is a practice project for me to help tune my skills using Python3

# Libraries
from random import shuffle
from random import sample
from random import choice

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


def blackjack_cards(decks_amt, deck) -> object:
    if type(decks_amt) is int:
        print(f"Amount of decks set at {decks_amt}")
    else:
        decks_amt = 5
        print("Invalid input, defaulted to 5 decks")

    playing_cards = decks_amt * deck
    shuffle(playing_cards)
    return playing_cards


class Player:

    def __init__(self, name, money):
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

        print(f"Dealer's cards: \n")

        for i in player_cards:
            land = str(i[0])
            number = str(i[1])
            cards_open = f"{number} of {land}"
            print(cards_open)
        print('\n')
        return player_cards

    def bet(self, amount_bet):
        self.amount_bet = amount_bet
        self.money = self.money - self.amount_bet
        return self.amount_bet

    def total(self):
        return self.money

    def name(self):
        return str(self.name())



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
            print('Closed')
            print(cards_open)
            break
        return player_cards

# multideck = blackjack_cards(1, deck)
#
# p1 = Player(100, "Mike")
# dealer = Dealer()
# p1_cards = p1.deal(multideck)
# p1_round1_cards = p1.hit(multideck, p1_cards)
# p1_round2_cards = p1.hit(multideck, p1_round1_cards)
# dealer_cards = dealer.deal(multideck)

######### Gameplay ############

amt_of_players = int(input(f"Hello! \nPlease specify amount of players in game (1 - 6): "))
player_names = []

for player in range(amt_of_players):
    print(f"Input Player {player + 1} money and name.")
    playerobj = Player(input("Player name:"), int(input("Amount of money:")))
    player_names.append(playerobj)

playing_cards = blackjack_cards(int(input('How many decks? ')), deck)

dealer = Dealer()

if amt_of_players == 1:
    print("Playing alone")

elif amt_of_players in range(2, 7):
    print(f"Playing with {amt_of_players}  persons.")

else:
    error_test = int(input('Invalid number of players. Press 1 to restart, 2 to play alone.'))
    if error_test == 2:
        amt_of_players = 1

        print("Playing alone")
    else:
        raise Exception("Something was incorrectly entered, restart")



def blackjack(sum_cards):
    if sum_cards == 21:
        print('Blackjack!')

def round_of_blackjack(players):
    print('Dealer: Place your bets!')
    bets_round = [player.bet(int(input('Bet size:'))) for player in players]

    for player in range(len(player_names)):
        money = player_names[player].total()
        print(f"Player {player + 1} has {money} money left")




    input("Press any key to deal...")

    round_dealer = dealer.deal(playing_cards)
    round_player = [player.deal(playing_cards) for player in players]

    dealer_cards_value = round_dealer[0][1] + round_dealer[1][1]
    amtcards = 2
    while dealer_cards_value < 16:
        round_dealer = dealer.hit(playing_cards, round_dealer)
        dealer_cards_value += round_dealer[amtcards][1]
        amtcards += 1

    # for player in players






round_of_blackjack(player_names)