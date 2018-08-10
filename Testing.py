class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.new_card = []

    def add_card(self):
        self.new_card = play_deck.deal()
        if self.new_card[1] == 'Ace ':
            ace_value = None
            while True:
                try:
                    while ace_value != 1 and ace_value != 11:
                        ace_value = int(input('Choose 1 or 11:\n'))
                        self.value += ace_value

                    break
                except:
                    print('Enter a valid integer')
        else:
            self.value += values[str(self.new_card[1])]

        self.cards.append(self.new_card)
