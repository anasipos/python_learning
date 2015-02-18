__author__ = 'anamaria.sipos'

from exercises.level2 import ex2
from exercises.level2.ex2 import Player
from exercises.level2.ex2 import Dealer
from exercises.level2.ex2 import Deck
from exercises.level2.ex2 import Card
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_deal_no_deck_no_game(self):
        deck = None
        players = [Player('John'), Player('Michael')]
        dealer = Dealer('Julia')

        dealt_cards = dealer.deal(deck, players)

        self.assertEqual(ex2.msg_no_decks, dealt_cards)

    def test_deal_no_players_no_game(self):
        players = []
        deck = 'does not matter'
        dealer = Dealer('Monica')

        dealt_cards = dealer.deal(deck, players)

        self.assertEqual(ex2.msg_no_players, dealt_cards)

    def test_deal_three_players(self):
        player1 = Player('John')
        player2 = Player('Michael')
        player3 = Player('Tom')
        players = [player1, player2, player3]

        dealer = Dealer('Ana')

        deck = Deck(complete=True)

        dealer.shuffle(deck)
        dealer.sort_by_sign_and_value(deck)

        dealt_cards = dealer.deal(deck, players)
        dealer_cards = dealer.draw(deck)

        self.assertEqual(2, len(dealt_cards[player1]))
        self.assertEqual(2, len(dealt_cards[player2]))
        self.assertEqual(2, len(dealt_cards[player3]))
        self.assertEqual(5, len(dealer_cards))

    def test_deal_three_players_not_enough_cards_get_message(self):
        player1 = Player('John')
        player2 = Player('Michael')
        player3 = Player('Tom')
        players = [player1, player2, player3]
        dealer = Dealer('Ana')

        deck = Deck([Card(Card.clubs, 10), Card(Card.clubs, 'J'), Card(Card.clubs, 'Q'), Card(Card.clubs, 'K'),
                     Card(Card.clubs, 'A')])

        dealt_cards = dealer.deal(deck, players)

        self.assertEqual(ex2.msg_not_enough_cards, dealt_cards)

    def test_deal_three_players_not_enough_cards_for_dealer_get_message(self):
        player1 = Player('John')
        player2 = Player('Michael')
        player3 = Player('Tom')
        players = [player1, player2, player3]
        dealer = Dealer('Ana')

        deck = Deck([Card(Card.clubs, 10), Card(Card.clubs, 'J'), Card(Card.clubs, 'Q'), Card(Card.clubs, 'K'),
                     Card(Card.clubs, 'A'), Card(Card.hearts, 'A'), Card(Card.diamonds, 'A')])

        dealt_cards = dealer.deal(deck, players)
        dealer_cards = dealer.draw(deck)

        self.assertEqual(ex2.msg_not_enough_cards, dealer_cards)


suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
