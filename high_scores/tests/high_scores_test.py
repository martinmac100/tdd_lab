import unittest

from src.high_scores import latest, personal_best, personal_top_three, highest_to_lowest, top_three_tie

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [34, 54, 765, 234, 1, 32, 764, 98, 901, 378, 811]

    # Test latest score (the last thing in the list)
    def test_latest(self):
        self.assertEqual(811, latest(self.scores))

    # Test personal best (the highest score in the list)

    def test_personal_best(self):
        self.assertEqual(901, personal_best(self.scores))

    # Test top three from list of scores

    def test_personal_top_three(self):
        self.assertEqual([765, 811, 901], personal_top_three(self.scores))

    # Test ordered from highest tp lowest

    def test_highest_to_lowest(self):
        self.assertEqual([901, 811, 765, 764, 378, 234, 98, 54, 34, 32,1], highest_to_lowest(self.scores))

    # Test top three when there is a tie
    def test_top_three_tie(self):
        tied_scores = [130,7,11,42,130]
        self.assertEqual([42,130,130], top_three_tie(tied_scores))
    # Test top three when there are less than three

    # Test top three when there is only one
