import unittest
from kalah import Kalah

class KalahTestCase(unittest.TestCase):

    def test_InitialStatus(self):
        game = Kalah(6, 4)
        self.assertEqual(game.status(), (4,4,4,4,4,4,0,4,4,4,4,4,4,0))





if __name__ == '__main__':
    unittest.main()
