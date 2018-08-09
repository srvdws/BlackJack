"""
The BlackJack game
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return('{} of {}'.format(self.suit, self.rank))



class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                play_card = Card(rank, suit)
                print(play_card)
                self.deck.append(play_card)

    def __str__(self):
        return self.deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

play_deck = Deck()

print(play_deck.deck)
play_deck.shuffle()
print(play_deck.deck)
print(play_deck.deal())


