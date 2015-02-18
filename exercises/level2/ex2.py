__author__ = 'anamaria.sipos'

from random import shuffle

msg_no_decks = 'No cards to deal'
msg_no_players = 'No players in the game'
msg_no_more_cards = 'No more cards'
msg_not_enough_cards = 'Not enough cards'


class Card(object):
    spades = 'spades'
    hearts = 'hearts'
    diamonds = 'diamonds'
    clubs = 'clubs'
    possible_signs = [spades, hearts, diamonds, clubs]
    possible_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    possible_values_weights = {val: index for index, val in enumerate(possible_values)}

    complete_deck = [(sign, value) for sign in possible_signs for value in possible_values]

    def __init__(self, sign, value):
        if sign not in self.possible_signs or value not in self.possible_values:
            self.sign = None
            self.value = None
        else:
            self.sign = sign
            self.value = value

    def __eq__(self, other):
        return (self.sign, self.value) == (other.sign, other.value)

    def __ne__(self, other):
        return (self.sign, self.value) != (other.sign, other.value)

    def __hash__(self):
        return self.sign.__hash__() + self.value.__hash__()


class Deck(object):
    def __init__(self, cards=None, complete=False):
        self.cards = []

        if complete:
            self.cards = [Card(sign, value) for sign, value in Card.complete_deck]
        elif cards is not None:
            self.add_cards(cards)

    def add_cards(self, cards):
        for card in cards:
            if card not in self.cards:
                self.cards.append(card)

    def remove_cards(self, cards):
        if cards is not []:
            self.cards[:] = [item for item in self.cards if item not in cards]

    def shuffle_cards(self):
        shuffle(self.cards)

    def sort_cards_by_sign(self):
        cards_sign_index = {card: Card.possible_signs.index(card.sign) for card in self.cards}
        sorted_cards = sorted(self.cards, key=cards_sign_index.__getitem__)
        self.cards = sorted_cards

    def sort_cards_by_value(self):
        cards_value_index = {card: Card.possible_values.index(card.value) for card in self.cards}
        sorted_cards = sorted(self.cards, key=cards_value_index.__getitem__)
        self.cards = sorted_cards

    def sort_cards_by_sign_and_value(self):
        cards_sign_and_value_weights = {card: (Card.possible_signs.index(card.sign) + 1) * 100 +
                                              Card.possible_values.index(card.value) for card in self.cards}
        sorted_cards = sorted(self.cards, key=cards_sign_and_value_weights.__getitem__)
        self.cards = sorted_cards

    def draw_cards(self, no_of_cards):
        if self.cards == [] or no_of_cards == 0:
            return []

        if len(self.cards) < no_of_cards:
            return msg_no_more_cards

        drawn_cards = self.cards[0:no_of_cards]
        self.cards[:] = self.cards[no_of_cards:len(self.cards)]

        return drawn_cards


class Dealer(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def shuffle(deck):
        deck.shuffle_cards()

    @staticmethod
    def sort_by_sign(deck):
        deck.sort_cards_by_sign()

    @staticmethod
    def sort_by_value(deck):
        deck.sort_cards_by_value()

    @staticmethod
    def sort_by_sign_and_value(deck):
        deck.sort_cards_by_sign_and_value()

    @staticmethod
    def draw(deck):
        if len(deck.cards) < 5:
            return msg_not_enough_cards
        return deck.draw_cards(5)


    @staticmethod
    def deal(deck, players):
        if not deck:
            return msg_no_decks
        if players == []:
            return msg_no_players
        if len(deck.cards) < len(players) * 2:
            return msg_not_enough_cards

        dealt_cards = {}
        for player in players:
            dealt_cards[player] = deck.draw_cards(2)

        return dealt_cards


class Player(object):
    def __init__(self, name):
        self.name = name




