import random


class Card:
    number_list = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
    mast_list = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __str__(self):
        return f"{self.mast} {self.number}"


class CardsDeck:
    def __init__(self):
        self.cards = [Card(n, m) for m in Card.mast_list for n in Card.number_list]
        self.cards += [Card("Joker", "Black"), Card("Joker", "Red")]

    def shuffle(self):
        random.shuffle(self.cards)

    def get(self, index):
        return self.cards.pop(index) if 0 <= index < len(self.cards) else "Invalid card number"


deck = CardsDeck()
deck.shuffle()

for _ in range(2):
    try:
        card_number = int(input("Выберите карту из колоды (0-55): "))
        print(f"Your card is: {deck.get(card_number)}")
    except ValueError:
        print("Please enter a valid number.")
