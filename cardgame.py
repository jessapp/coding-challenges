"""Design a class to represent the card game War"""

import random

class Card(object):
    """Creates card objects"""

    def __init__(self, suit, value):

        self.suit = suit.lower()
        self.value = value

    def black_or_red(self):
        if self.suit == "hearts" or self.suit == "diamonds":
            return "red"
        else:
            return "black"

    def is_face_card(self):
        face_cards = [11, 12, 13]

        for card in face_cards:
            if self.value == card:
                return True
        return False

    def __repr__(self):

        value = self.value

        if value == 1:
            value = "ace"
        elif value == 11:
            value = "jack"
        elif value = 12:
            value = "queen"
        elif value = 13:
            value = "king"

        return "%s of %s" % (rank, self.suit)

class Deck(object): 
    """Creates deck of cards"""

    def __init__:
        self.stack = []

        self.first_player_hand = []

        self.second_player_hand = []

    def create_deck(self):
        """Creates deck of 52 cards"""
        suits = ["clubs", "diamonds", "hearts", "spades"]

        for suit in suits:
            for value in range(1, 14):
                self.stack.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.stack)

    def deal(self):

        while stack != []:
            self.first_player_hand.append(self.stack.pop())
            self.second_player_hand.append(self.stack.pop())

class PlayGame(object):
    """Initiates gameplay"""

    def start_game(self):
        new_deck = Deck.create_deck().shuffle().deal()

        first_player = new_deck.first_player_hand

        second_player = new_deck.second_player_hand

        while len(first_player) > 0 or len(second_player) > 0:
            first_player_card = first_player.pop()
            second_player_card = second_player.pop()

            if first_player_card > second_player_card:
                first_player.insert(0, second_player_card)
                first_player.insert(0, first_player_card)
            elif second_player_card > first_player_card:
                second_player.insert(0, first_player_card)
                second_player.insert(0, second_player_card)






