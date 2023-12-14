

class Card(object):
    values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    suits = ('clubs', 'diamonds', 'hearts', 'spades')

    def __init__(self, value='A', suit='spade'):
        self.value, self.suit = value, suit
        print(f"In init; value is {value}; suit is {suit}")

    def __repr__(self):
        return "Card('%s','%s')" % (self.value, self.suit)

    def __gt__(self, other):
        if self.suits.index(self.suit) > self.suits.index(other.suit):
            return True

        if self.suits.index(self.suit) < self.suits.index(other.suit):
            return False

        return self.values.index(self.value) > self.values.index(other.value)

def moc_karty(karta):
    return len(values)*suits.index(karta.suit) + values.index(karta.value)

krol_karo = Card('K', 'diamonds')
as_karo = Card('A', 'diamonds')
dycha_karo = Card('10', 'diamonds')
karty_w_rece = [ as_karo, krol_karo, dycha_karo]

print(karty_w_rece)

karty_w_rece.sort()
print(karty_w_rece)


