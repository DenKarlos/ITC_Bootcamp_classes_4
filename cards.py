from random import shuffle

class Card:
    def __init__(self, suit, rank):
        hirank = ['J', 'Q', 'K', 'A']
        self.suit = suit
        if 2 <= rank <= 10:
            self.rank = str(rank)
        else:
            self.rank = hirank[rank % 11]
    
    def __str__(self):
        return f'{self.rank}{self.suit}'

class Deck:
    deck = []
    suits = ['♠', '♥', '♣', '♦']
    def __init__(self):
        for i in range(2, 15):
            for j in self.suits:
                self.deck.append(Card(j, i))

    def print_deck(self):
        counter = 0
        row = 8
        for i in self.deck:
            if counter % row != row-1:
                print(i, '', end = '')
            else:
                print(i)
            counter += 1
        print()

    def shufle_deck(self):
        shuffle(self.deck)

    def drag_card(self):
        if self.deck:
            print(f'Вытащена карта: {self.deck.pop()}')
        else:
            print(f'Колода пустая!!!')

    def rest_deck(self):
        print(f'В колоде осталось {len(self.deck)} карт')


simple_deck = Deck()
simple_deck.shufle_deck()

for i in range(20):
    simple_deck.drag_card()

simple_deck.print_deck()
simple_deck.rest_deck()