# Tests simulating Tic-Tac-Toe.

import unittest
import tic_tac_toe

class TestTicTacToe(unittest.TestCase):
    def test01_check_grid(self):
        grid = [["O", None, "X"],
                ["O", "X", None],
                [None, None, "X"]]

        won = tic_tac_toe.check_row(grid)
        self.assertFalse(won)
        won = tic_tac_toe.check_column(grid)
        self.assertFalse(won)
        won = tic_tac_toe.check_diagonal(grid)
        self.assertFalse(won)
        won = tic_tac_toe.check_grid(grid)
        self.assertFalse(won)

    def test02_check_grid(self):
        grid = [["O", None, "X"],
                ["O", "X", None],
                ["O", None, "X"]]

        won = tic_tac_toe.check_row(grid)
        self.assertFalse(won)
        won = tic_tac_toe.check_column(grid)
        self.assertTrue(won)
        won = tic_tac_toe.check_diagonal(grid)
        self.assertFalse(won)
        won = tic_tac_toe.check_grid(grid)
        self.assertTrue(won)


if __name__ == "__main__":
    unittest.main()
