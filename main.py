from deck import Deck

if __name__ == '__main__':
    # Make a new deck
    newDeck = Deck()
    # Deal 56 cards, should stop giving cards after 52
    for idx in range(0, 56):
        theCard = newDeck.dealOneCard()
        if theCard is None:
            print("No more cards in deck")
            continue
        print(theCard)

    # Shuffle the deck
    print("Shuffling...")
    newDeck.shuffle()

    # Deal 60 cards of shuffled deck
    for idx in range(0, 60):
        theCard = newDeck.dealOneCard()
        if theCard is None:
            print("No more cards in deck")
            continue
        print(theCard)
