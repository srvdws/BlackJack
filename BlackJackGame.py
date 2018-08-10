"""
The BlackJack game
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs ')
ranks = ('Two ', 'Three ', 'Four', 'Five', 'Six ', 'Seven ', 'Eight ', 'Nine', 'Ten ', 'Jack', 'Queen ', 'King', 'Ace ')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card():

    def __init__(self, rank, suit, number):
        self.number = number
        self.suit = suit
        self.rank = rank
        self.card = []
        self.card = [number, self.rank, ' of ', self.suit]

    def __repr__(self):
        return ''.join(self.card)



class Deck():

    def __init__(self):
        self.deck = []
        n = 0
        for suit in suits:
            for rank in ranks:
                n += 1
                play_card = Card(rank, suit, n)
                print(play_card.card)
                self.deck.append(play_card.card)

    def __str__(self):
        return self.deck

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def deal(self):
        return self.deck.pop()


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
        print('|           ^^ |')
        print('|           \/ |')
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

play_deck = Deck()

print(play_deck.deck)
print(play_deck.shuffle())
#print(''.join(play_deck.deal()[1:]))
print_card(play_deck.deal())


