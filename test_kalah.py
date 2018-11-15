import unittest
from kalah import Kalah

class KalahTestCase(unittest.TestCase):

    def test_InitialStatus(self):
        game = Kalah(6, 4)
        self.assertEqual(game.status(), (4,4,4,4,4,4,0,4,4,4,4,4,4,0))

    def test_Illegalhole(self):
        game = Kalah(6, 4)
        self.assertRaises(IndexError, game.play, 'A')

    def test_Simplemove(self):
        game = Kalah(6, 4)
        game.play('f')
        self.assertEqual(game.status(), (0,5,5,5,5,4,0,4,4,4,4,4,4,0))
    def test_Crossingmove(self):
        game = Kalah(6, 4)
        game.play('a')
        self.assertEqual(game.status(), (4,4,4,4,4,0,1,5,5,5,4,4,4,0))






if __name__ == '__main__':
    unittest.main()
