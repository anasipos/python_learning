__author__ = 'anamaria.sipos'

from exercises.level2 import ex2
from exercises.level2.ex2 import Deck
from exercises.level2.ex2 import Card
import unittest


def verify_if_sorted_by_sign(cards):
    spades = cards[0:len(Card.possible_values)]
    hearts = cards[len(Card.possible_values):len(Card.possible_values) * 2]
    diamonds = cards[len(Card.possible_values) * 2:len(Card.possible_values) * 3]
    clubs = cards[len(Card.possible_values) * 3:len(Card.possible_values) * 4]

    all_spades = reduce(lambda valid, card: valid and (card.sign == 'spades'), spades)
    all_hearts = reduce(lambda valid, card: valid and (card.sign == 'hearts'), hearts)
    all_diamonds = reduce(lambda valid, card: valid and (card.sign == 'diamonds'), diamonds)
    all_clubs = reduce(lambda valid, card: valid and (card.sign == 'clubs'), clubs)

    if all_spades and all_diamonds and all_hearts and all_clubs:
        return spades, hearts, diamonds, clubs
    return False


def verify_if_sorted_by_value(cards):
    step = len(Card.possible_signs)
    index = step
    for value in Card.possible_values:
        cards_with_same_value = cards[index - step:index]
        same_value = reduce(lambda valid, card: valid and card.value == value, cards_with_same_value)
        if not same_value:
            return False
        index += step
    return True


def verify_if_sorted_by_sign_and_value(cards):
    sorted_by_sign = verify_if_sorted_by_sign(cards)

    if not sorted_by_sign or not isinstance(sorted_by_sign, tuple):
        return False

    for cards_by_sign in sorted_by_sign:
        for index, value in enumerate(Card.possible_values):
            if cards_by_sign[index].value != value:
                return False

    return True


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_add_cards_same_cards_not_added_twice(self):
        deck = Deck()
        deck.add_cards([Card(Card.clubs, 10), Card(Card.clubs, 'J'), Card(Card.clubs, 10), Card(Card.clubs, 'K'),
                        Card(Card.clubs, 'J')])
        self.assertEqual(3, len(deck.cards))
        self.assertEqual({card for card in [Card(Card.clubs, 10), Card(Card.clubs, 'J'), Card(Card.clubs, 'K')]},
                         set(deck.cards))

    def test_draw_cards_deck_has_no_cards_return_zero(self):
        deck = Deck()
        cards = deck.draw_cards(5)
        self.assertEqual(0, len(cards))

    def test_draw_cards_zero_cards_return_zero_cards(self):
        deck = Deck([Card(Card.clubs, 10)])
        cards = deck.draw_cards(0)
        self.assertEqual(0, len(cards))

    def test_draw_5_cards_return_5_cards(self):
        deck = Deck([Card(Card.clubs, 10), Card(Card.clubs, 'J'), Card(Card.clubs, 'Q'), Card(Card.clubs, 'K'),
                     Card(Card.clubs, 'A')])
        initial_no_of_cards = len(deck.cards)

        cards = deck.draw_cards(5)

        self.assertEqual(5, len(cards))
        self.assertEqual(initial_no_of_cards - 5, len(deck.cards))

    def test_draw_5_cards_from_2_card_deck(self):
        deck = Deck([Card(Card.clubs, 10), Card(Card.clubs, 'J')])

        cards = deck.draw_cards(5)

        self.assertEqual(ex2.msg_no_more_cards, cards)

    def test_shuffle_cards(self):
        deck = Deck(complete=True)

        original_card_positions = {card: deck.cards.index(card) for card in deck.cards}

        deck.shuffle_cards()
        after_shuffle_card_positions = {card: deck.cards.index(card) for card in deck.cards}

        self.assertNotEqual(original_card_positions, after_shuffle_card_positions)

    def test_sort_cards_by_sign(self):
        deck = Deck(complete=True)
        deck.shuffle_cards()

        deck.sort_cards_by_sign()

        self.assertTrue(verify_if_sorted_by_sign(deck.cards))

    def test_sort_cards_by_value(self):
        deck = Deck(complete=True)
        deck.shuffle_cards()

        deck.sort_cards_by_value()

        self.assertTrue(verify_if_sorted_by_value(deck.cards))

    def test_sort_by_sign_and_value(self):
        deck = Deck(complete=True)
        deck.shuffle_cards()

        deck.sort_cards_by_sign_and_value()

        self.assertTrue(verify_if_sorted_by_sign_and_value(deck.cards))


# if __name__ == '__main__':
# unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
