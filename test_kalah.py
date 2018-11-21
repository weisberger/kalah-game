import unittest
from kalah import Kalah


class Kalah_testCase(unittest.TestCase):

    def test_initial_Status(self):
        game = Kalah(6, 4)
        self.assertEqual(game.status(), (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_illegal_hole(self):
        game = Kalah(6, 4)
        self.assertRaises(IndexError, game.play, 'A')

    def test_simple_move(self):
        game = Kalah(6, 4)
        game.play('f')
        self.assertEqual(game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_crossing_move(self):
        game = Kalah(6, 4)
        game.play('a')
        self.assertEqual(game.status(), (4, 4, 4, 4, 4, 0, 1, 5, 5, 5, 4, 4, 4, 0))

    def test_two_simple_moves(self):
        game = Kalah(6, 4)
        game.play('e')
        game.play('E')
        self.assertEqual(game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 0, 5, 5, 5, 5, 0))

    def test_player_2_crosses(self):
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

    def test_empty_hole(self):
        game = Kalah(6, 4)
        game.play('e')
        game.play('A')
        game.play('f')
        self.assertRaises(ValueError, game.play, 'A')

    def test_bonus_move_player_1(self):
        game = Kalah(6, 4)
        self.assertEqual(game.play('d'), 'Player 1 plays next')

    def test_bonus_move_player_2(self):
        game = Kalah(6, 4)
        game.play('f')
        self.assertEqual(game.play('D'), 'Player 2 plays next')

    def test_capture_player_1(self):
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

    def test_capture_player_2(self):
        game = Kalah(6, 4)
        game.setStatus(
            {'f': 4, 'e': 4, 'd': 4, 'c': 8, 'b': 8, 'a': 8, 'bank_player_one': 1, 'F': 0, 'E': 0, 'D': 0, 'C': 0,
             'B': 0,
             'A': 9, 'bank_player_tow': 2})
        game.turn = [0, 1]
        game.play('A')
        self.assertEqual(game.status(), (5, 5, 5, 9, 0, 9, 1, 1, 0, 0, 0, 0, 0, 13))

    def test_non_capture(self):
        game = Kalah(6, 4)
        game.turn = [0, 1]
        game.setStatus(
            {'f': 4, 'e': 4, 'd': 4, 'c': 8, 'b': 0, 'a': 8, 'bank_player_one': 1, 'F': 1, 'E': 0, 'D': 0, 'C': 0,
             'B': 0,
             'A': 5, 'bank_player_tow': 13})
        game.play('F')
        self.assertEqual(game.status(), (4, 4, 4, 8, 0, 8, 1, 0, 1, 0, 0, 0, 5, 13))

    def test_end_game_player_1_win(self):
        game = Kalah(6, 4)
        game.setStatus(
            {'f': 2, 'e': 3, 'd': 0, 'c': 0, 'b': 8, 'a': 8, 'bank_player_one': 15, 'F': 0, 'E': 0, 'D': 0, 'C': 2,
             'B': 0, 'A': 0, 'bank_player_tow': 10})
        self.assertEqual(game.play('f'), 'player 1 win')

    def test_end_game_player_2_win(self):
        game = Kalah(6, 4)
        game.turn = [0, 1]
        game.setStatus(
            {'f': 0, 'e': 0, 'd': 0, 'c': 2, 'b': 0, 'a': 0, 'bank_player_one': 10, 'F': 2, 'E': 3, 'D': 0, 'C': 0,
             'B': 8, 'A': 8, 'bank_player_tow': 15})
        self.assertEqual(game.play('F'), 'player 2 win')

    def test_end_tie(self):
        game = Kalah(6, 4)
        game.setStatus(
            {'f': 2, 'e': 2, 'd': 0, 'c': 0, 'b': 8, 'a': 8, 'bank_player_one': 2, 'F': 0, 'E': 0, 'D': 0, 'C': 2,
             'B': 0,
             'A': 0, 'bank_player_tow': 24})
        self.assertEqual(game.play('f'), 'tie')

    def test_repr(self):
        assert repr(Kalah(6, 4)) == "Kalah(4, 6, status=(4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0), player=0)"

    def test_render(self):
        game = Kalah(6, 4)
        s = f" ****   ===========================================   ****\n" \
            f"*    *  |      |      |      |      |      |      |  *    *\n" \
            f"*    *  |  {game.board['A']}{' ' if game.board['A']<10 else ''}  |  {game.board['B']}{' ' if game.board['B']<10 else ''}  |  {game.board['C']}{' ' if game.board['C']<10 else ''}  |  {game.board['D']}{' ' if game.board['D']<10 else ''}  |  {game.board['E']}{' ' if game.board['E']<10 else ''}  |  {game.board['F']}{' ' if game.board['F']<10 else ''}  |  *    *\n" \
            f"*    *  |      |      |      |      |      |      |  *    *\n" \
            f"* {game.board['bank_player_tow']}{' ' if game.board['bank_player_tow']<10 else ''} *  ===========================================  *{' ' if game.board['bank_player_one']<10 else ''}{game.board['bank_player_one']}  *\n" \
            f"*    *  |      |      |      |      |      |      |  *    *\n" \
            f"*    *  |  {game.board['a']}{' ' if game.board['a']<10 else ''}  |  {game.board['b']}{' ' if game.board['b']<10 else ''}  |  {game.board['c']}{' ' if game.board['c']<10 else ''}  |  {game.board['d']}{' ' if game.board['d']<10 else ''}  |  {game.board['e']}{' ' if game.board['e']<10 else ''}  |  {game.board['f']}{' ' if game.board['f']<10 else ''}  |  *    *\n" \
            f"*    *  |      |      |      |      |      |      |  *    *\n" \
            f" ****   ===========================================   ****\n"
        self.assertEqual(game.__str__(), s)


if __name__ == '__main__':
    unittest.main()
