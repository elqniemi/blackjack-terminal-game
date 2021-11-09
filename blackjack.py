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
        self.money = self.money - amount_bet



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

own_name = str(input("Enter your name: "))
amt_of_players = int(input(f"Hello {own_name}.\nPlease specify amount of players in game (1 - 6): "))
player_name = str()
playing_cards = blackjack_cards(int(input('How many decks? ')), deck)
total_money = int(input("How much $$$ you have?"))
player_names = [own_name, "Player2", "Player3", "Player4", "Player5", "Player6"]
dealer = Dealer()

if amt_of_players == 1:
    print("Playing alone")
    player_names = [player_names.pop(i) for i in range(amt_of_players)]
elif amt_of_players in range(2, 7):
    print(f"Playing with {amt_of_players - 1} other persons.")
    player_names = [player_names.pop(0) for i in range(amt_of_players)]
else:
    error_test = int(input('Invalid number of players. Press 1 to restart, 2 to play alone.'))
    if error_test == 2:
        amt_of_players = 1
        player_names = [player_names.pop(i) for i in range(amt_of_players)]
        print("Playing alone")
    else:
        raise Exception("Something was incorrectly entered, restart")

player_names_as_str = str()
for i in range(len(player_names)):
    assert isinstance(i, object)
    player_names_as_str += (player_names[i] + ", ")

print(f'Dealer: We have {player_names_as_str}playing now.')


# bet = int(input('Bet: '))

# Player objects for gameplay

players = []
player_1 = Player(total_money, own_name)

if amt_of_players >= 2:
    player_2 = Player(9999, player_names[1])

if amt_of_players >= 3:
    player_3 = Player(9999, player_names[2])

if amt_of_players >= 4:
    player_4 = Player(9999, player_names[3])

if amt_of_players >= 5:
    player_5 = Player(9999, player_names[4])

if amt_of_players > 5:
    player_6 = Player(9999, player_names[5])


def blackjack(sum_cards):
    if sum_cards == 21:
        print('Blackjack!')

def round_of_blackjack(player):
    print('Dealer: Place your bets!')
    player_1.bet(int(input('Bet amount: ')))
    input("Press any key to deal...")

    round_dealer = dealer.deal(playing_cards)
    round_player = player.deal(playing_cards)

    dealer_cards_value = round_dealer[0][1] + round_dealer[1][1]
    amtcards = 2
    while dealer_cards_value < 16:
        round_dealer = dealer.hit(playing_cards, round_dealer)
        dealer_cards_value += round_dealer[amtcards][1]
        amtcards += 1






round_of_blackjack(player_1)