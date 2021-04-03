from card import Card, SUITS, VALUES
from random import randrange

class Deck:
    def __init__(self):

        # Rather than actually adding/removing cards from a list, we will just keep all the cards in and keep track of a
        # position in the list for how many cards we've drawn. When we shuffle, we will randomize the cards then
        # reset our position to 0
        self.currPos = 0
        self.cards = []

        # add all of the cards into the list of cards, the deck starts unshuffled as it would be out of a pack
        for suit in SUITS:
            for val in VALUES:
                self.cards.append(Card(suit, val))

    # Shuffle the deck of cards so that new calls to dealOneCard can get any card, any cards already dealt are put
    # back in the deck
    def shuffle(self):

        # reset our position in the list of cards to be the start
        self.currPos = 0

        # Our approach here is to pick a random card out of the cards we haven't already picked, swap it to the
        # front of the deck, and decrease the range of remaining cards. We essentially randomly pick which should
        # the first card, then randomly pick which should be the second out of the remaining 51, etc.

        # placedCards will represent both how many we have placed so far and also the position we should put
        # the newly picked card into. Only need to do this 51 times, since by the time we get to the 52nd card
        # there will only be one left and there is no need to swap it with itself
        for placedCards in range(0, 51):
            # the number of remaining cards is (total number of cards in a deck - the number of cards we placed), so
            # that is the range we use to pick a random number. After we get a random number, we need to turn that into
            # an actual index in the array, so we add the number of cards we have placed to get past all of spots at the
            # start corresponding to cards we already selected
            pos = placedCards + randrange(0, 52 - placedCards)

            # we have selected a card at pos, so save off which card it is
            oldCard = self.cards[pos]

            # take whatever card is in the spot for the newly placed card and put it in the selected card's old position
            self.cards[pos] = self.cards[placedCards]

            # Now, put the selected card in the range of the cards we have already selected
            self.cards[placedCards] = oldCard

    # Deal one card from the deck
    # RETURNS: The next card in the deck, or NONE if empty
    def dealOneCard(self):
        # If we've dealt all cards, return None
        if self.currPos >= len(self.cards):
            return None
        # Return the card at the current position and increment the position
        newCard = self.cards[self.currPos]
        self.currPos = self.currPos + 1
        return newCard