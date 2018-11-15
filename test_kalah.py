import unittest
from kalah import Kalah

class KalahTestCase(unittest.TestCase):

    def test_InitialStatus(self):
        game = Kalah(6, 4)
        self.assertEqual(game.status(), (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_Illegalhole(self):
        game = Kalah(6, 4)
        self.assertRaises(IndexError, game.play, 'A')

    def test_Simplemove(self):
        game = Kalah(6, 4)
        game.play('f')
        self.assertEqual(game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_Crossingmove(self):
        game = Kalah(6, 4)
        game.play('a')
        self.assertEqual(game.status(), (4, 4, 4, 4, 4, 0, 1, 5, 5, 5, 4, 4, 4, 0))

    def test_TwosimpleMoves(self):
        game = Kalah(6, 4)
        game.play('e')
        self.assertEqual(game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0))
        game.play('E')
        self.assertEqual(game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 0, 5, 5, 5, 5, 0))

    def test_Player2crosses(self):
        game = Kalah(6, 4)
        game.play('e')
        self.assertEqual(game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0))
        game.play('E')
        self.assertEqual(game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 0, 5, 5, 5, 5, 0))
        game.play('a')
        self.assertEqual(game.status(), (4, 0, 5, 5, 5, 0, 1, 5, 1, 6, 6, 5, 5, 0))
        game.play('A')
        self.assertEqual(game.status(), (5, 1, 6, 6, 5, 0, 1, 5, 1, 6, 6, 5, 0, 1))

    def test_crossing_other_bank(self):
        game = Kalah(6, 4)
        game.play('e')
        game.play('E')
        game.play('d')
        game.play('D')
        game.play('c')
        game.play('C')
        game.play('b')
        game.play('B')
        game.play('a')
        game.play('A')
        self.assertEquals(game.status(), (9, 4, 3, 2, 2, 1, 4, 9, 4, 3, 2, 1, 0, 4))

    def test_EmptyHole(self):
        game = Kalah(6, 4)
        game.play('e')
        self.assertEqual(game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0))
        game.play('A')
        self.assertEqual(game.status(), (5, 1, 6, 5, 5, 5, 0, 4, 4, 4, 4, 4, 0, 1))
        game.play('f')
        self.assertEqual(game.status(), (0, 2, 7, 6, 6, 6, 0, 4, 4, 4, 4, 4, 0, 1))
        self.assertRaises(ValueError, game.play, 'A')


















if __name__ == '__main__':
    unittest.main()
