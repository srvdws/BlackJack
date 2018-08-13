"""
The BlackJack game
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs ')
ranks = ('Two ', 'Three ', 'Four', 'Five', 'Six ', 'Seven ', 'Eight ', 'Nine', 'Ten ', 'Jack', 'Queen ', 'King', 'Ace ')
values = {'Two ': 2, 'Three ': 3, 'Four': 4, 'Five': 5, 'Six ': 6, 'Seven ': 7, 'Eight ': 8, 'Nine': 9, 'Ten ': 10, 'Jack': 10, 'Queen ': 10, 'King': 10, 'Ace ': 11}

playing = True


class Card():
    def __init__(self, rank, suit, number, value):
        self.number = number
        self.suit = suit
        self.rank = rank
        self.card = []
        self.value = value
        self.card = [number, self.rank, ' of ', self.suit, self.value]


    def __repr__(self):
        return ''.join(self.card)




class Deck():
    def __init__(self):
        self.deck = []
        n = 0
        for suit in suits:
            for rank in ranks:
                #print('DEBUG: ', rank)
                n += 1
                play_card = Card(rank, suit, n, (values[rank]))
                #print(play_card.card)
                self.deck.append(play_card.card)

    def __str__(self):
        return self.deck

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def deal(self):
        return self.deck.pop()


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.new_card = []

    def add_card(self):
        self.new_card = play_deck.deal()
        self.cards.append(self.new_card)


class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += (self.bet * 2)

    def lose_bet(self):
        self.total -= self.bet


def print_card(card):
    print(' ______________')
    print('|              |')

    if card[1] == 'Two ':
        print('| 2            |')
    elif card[1] == 'Three ':
        print('| 3            |')
    elif card[1] == 'Four':
        print('| 4            |')
    elif card[1] == 'Five':
        print('| 5            |')
    elif card[1] == 'Six ':
        print('| 6            |')
    elif card[1] == 'Seven ':
        print('| 7            |')
    elif card[1] == 'Eight ':
        print('| 8            |')
    elif card[1] == 'Nine':
        print('| 9            |')
    elif card[1] == 'Ten ':
        print('| 10           |')
    elif card[1] == 'Jack':
        print('| J            |')
    elif card[1] == 'Queen ':
        print('| Q            |')
    elif card[1] == 'King':
        print('| K            |')
    elif card[1] == 'Ace ':
        print('| A            |')

    print('|              |')
    print('|              |')
    print('|', ' ' * int(5 - (len(card[1]) / 2)), card[1], ' ' * int(5 - (len(card[1]) / 2)), '|')
    print('|', ' ' * int(5 - (len(card[2]) / 2)), card[2], ' ' * int(5 - (len(card[2]) / 2)), '|')
    print('|', ' ' * int(5 - (len(card[3]) / 2)), card[3], ' ' * int(5 - (len(card[3]) / 2)), '|')
    print('|              |')

    if card[3] == 'Hearts':
        print('|         /\/\ |')
        print('|          \/  |')
    elif card[3] == 'Diamonds':
        print('|           /\ |')
        print('|           \/ |')
    elif card[3] == 'Spades':
        print('|          / \ |')
        print('|           ^  |')
    elif card[3] == 'Clubs ':
        print('|          oºo |')
        print('|           |  |')

    print('|______________|')


def print_blank_card(card):
    print(' ______________')
    print('|              |')
    print('|/\/\/\/\/\/\/\|')
    print('|\/\/\/\/\/\/\/|')
    print('|/\/\/\/\/\/\/\|')
    print('|\/\/\/\/\/\/\/|')
    print('|/\/\/\/\/\/\/\|')
    print('|\/\/\/\/\/\/\/|')
    print('|/\/\/\/\/\/\/\|')
    print('|\/\/\/\/\/\/\/|')
    print('|/\/\/\/\/\/\/\|')
    print('|______________|')


def print_player_hand(hand):
    for i in range(0, len(hand)):
        print_card(hand[i])


def print_dealer_hand(hand):
    for i in range(0, len(hand)):
        if i == 0:
            print_blank_card(hand[i])

        else:
            print_card(hand[i])


def take_bet():
    bet_amount = 0
    print('\nYou have ', player_chips.total, 'Chips.')
    while True:
        try:
            while bet_amount <= 0 or bet_amount > player_chips.total:
                bet_amount = int(input('Place your bet:\n'))
            break

        except:
            print('Please enter a valid amount')
    return bet_amount


def player_hit(handvalue):
    hityn = None
    while hityn != 'y'.upper() and hityn != 'n'.upper():
        hityn = str(input(print('Hit? (y/n): '))).upper()
        if hityn == 'y'.upper():
            player_hand.add_card()
        else:
            print('No hit')


def dealer_hit(handvalue):
    if handvalue <= 17 and handvalue < 21:
        dealer_hand.add_card()


def check_ace(card):
    if card[1] == 'Ace ':
        ace_value = None
        while True:
            try:
                while ace_value != 1 and ace_value != 11:
                    ace_value = int(input('Choose 1 or 11:\n'))
                break
            except:
                print('Enter a valid integer')
        return ace_value


def dealer_check_ace(card):
    if card[1] == 'Ace ':
        if dealer_hand.value < 10:
            return 11
        else:
            return 1



game_state = True

while True:

    play_deck = Deck()
    play_deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_chips = Chips()

    round_bet = take_bet()

    round_count = 0

    while True:
        dealer_hand.add_card()
        dealer_hand.value += int(dealer_check_ace(dealer_hand.cards[round_count]))
        print('DEALER HAND: ROUND {}'.format(round_count))
        print_dealer_hand(dealer_hand.cards)
        print(dealer_hand.value)

        player_hand.add_card()
        player_hand.value += int(check_ace(player_hand.cards[round_count]))
        print('PLAYER HAND: ROUND {}'.format(round_count))
        print_player_hand(player_hand.cards)
        print(player_hand.value)

        round_count += 1

        while round_count > 1:
            player_hit(player_hand.value)
            dealer_hit(dealer_hand.value)
            round_count += 1

            if round_count == 4:
                break
        if round_count > 4:
            break





#player_hand.add_card()
#player_hand.add_card()

#print_player_hand(player_hand.cards)
#print(player_hand.value)

#player_hand.add_card()

#print_player_hand(player_hand.cards)
#print(player_hand.value)

#print(take_bet())

    break