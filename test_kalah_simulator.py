import unittest

from kalah_simulator import parse_game, simulate_game
import logging

logging.basicConfig(
format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
level=logging.DEBUG)


class KalahSimulatorTestCase(unittest.TestCase):

  def test_simulate_game_1(self):
        with open(f"data/game_2.txt") as f:
            lines = f.read().splitlines()

        steps = parse_game(lines, 6)
        logger = logging.getLogger(__name__)
        for message, status in simulate_game(6, 6, steps):
            print(message)
            #logger.debug(message, status)
        self.assertEqual((0, 0, 0, 0, 0, 0, 38, 0, 0, 0, 0, 0, 0, 34), status)
        self.assertEqual(message, "Player 1 wins")

  def test_simulate_game_2(self):
        with open(f"data/game_3.txt") as f:
            lines = f.read().splitlines()

        steps = parse_game(lines, 6)
        logger = logging.getLogger(__name__)
        for message, status in simulate_game(6, 6, steps):
            print(message)
            #logger.debug(message, status)
        self.assertEqual((0, 0, 0, 0, 0, 0, 47, 0, 0, 0, 0, 0, 0, 25), status)
        self.assertEqual(message, "Player 1 wins")


if __name__ == '__main__':
    unittest.main()
