import unittest
from tic_tac_toe import TicTacToe

class GameTests(unittest.TestCase):
    def test_move(self):
        g = TicTacToe()
        self.assertTrue(g.move(1))
        self.assertFalse(g.move(1))
        self.assertFalse(g.move(0))
        self.assertFalse(g.move(10))

    def test_winning_lines(self):
        for line in TicTacToe.WIN_LINES:
            g = TicTacToe()
            for i in line:
                g.move(i+1)
            self.assertTrue(g.winner())

    def test_draw(self):
        g = TicTacToe()
        g.board = list('XOXXOOOXX')
        self.assertTrue(g.draw())

    def test_empty(self):
        g = TicTacToe()
        self.assertFalse(g.winner())
        self.assertFalse(g.draw())

if __name__ == '__main__':
    unittest.main()
