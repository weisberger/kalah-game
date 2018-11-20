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
        game.play('E')
        self.assertEqual(game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 0, 5, 5, 5, 5, 0))

    def test_Player2crosses(self):
        game = Kalah(6, 4)
        game.play('e')
        game.play('E')
        game.play('a')
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
        game.play('A')
        game.play('f')
        self.assertRaises(ValueError, game.play, 'A')

    def test_BonusMovePlayer1(self):
       game = Kalah(6, 4)
       self.assertEqual(game.play('d'), 'Player 1 plays next')

    def test_BonusMovePlayer2(self):
       game = Kalah(6, 4)
       game.play('f')
       self.assertEqual(game.play('D'), 'Player 2 plays next')

    def test_CapturePlayer1(self):
        game = Kalah(6, 4)
        game.play('f')
        game.play('F')
        game.play('b')
        game.play('F')
        game.play('c')
        game.play('F')
        game.play('d')
        game.play('F')
        game.play('b')
        game.play('a')
        self.assertEqual(game.status(), (0, 5, 0, 1, 0, 0, 11, 1, 11, 7, 6, 6, 0, 0))

    def  test_CapturePlayer2(self):
        game = Kalah(6, 4)
        game.setStatus({'f': 4, 'e': 4, 'd': 4, 'c': 8, 'b': 8, 'a': 8, 'bankPlayerone': 1, 'F': 0, 'E': 0, 'D': 0, 'C': 0, 'B': 0, 'A': 9, 'bankPlayertow': 2})
        game.turn = [0,1]
        game.play('A')
        self.assertEqual(game.status(), (5, 5, 5, 9, 0, 9, 1, 1, 0, 0, 0, 0, 0, 13))

    def test_NonCapture(self):
        game = Kalah(6, 4)
        game.turn = [0,1]
        game.setStatus({'f': 4, 'e': 4, 'd': 4, 'c': 8, 'b': 0, 'a': 8, 'bankPlayerone': 1, 'F': 1, 'E': 0, 'D': 0, 'C': 0, 'B': 0, 'A': 5, 'bankPlayertow': 13})
        game.play('F')
        self.assertEqual(game.status(), (4, 4, 4, 8, 0, 8, 1, 0, 1, 0, 0, 0, 5, 13))
    def test_EndGamePlayer1Win(self):
        game = Kalah(6, 4)
        game.setStatus({'f': 2, 'e': 3, 'd': 0, 'c': 0, 'b': 8, 'a': 8, 'bankPlayerone': 15, 'F': 0, 'E': 0, 'D': 0, 'C': 2, 'B': 0, 'A': 0, 'bankPlayertow': 10})
        self.assertEqual(game.play('f'), 'player 1 win')

    def test_EndGamePlayer2Win(self):
        game = Kalah(6, 4)
        game.turn = [0, 1]
        game.setStatus({'f': 0, 'e': 0, 'd': 0, 'c': 2, 'b': 0, 'a': 0, 'bankPlayerone': 10, 'F': 2, 'E': 3, 'D': 0, 'C': 0,'B': 8, 'A': 8, 'bankPlayertow': 15})
        self.assertEqual(game.play('F'), 'player 2 win')


if __name__ == '__main__':
    unittest.main()
