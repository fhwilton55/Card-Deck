# Consts representing valid suits/values for cards
SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]
VALUES = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    # String representation of a card, Value of Suit
    def __str__(self):
        return (self.__value + " of " + self.__suit)

    # Suit getter
    def getSuit(self):
        return self.__suit

    # Value getter
    def getValue(self):
        return self.__value