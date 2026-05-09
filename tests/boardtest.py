import unittest
from Gomoku.board import Board


class TestBoardMethods(unittest.TestCase):

    ## test that the check_win() function can correctly identify a win scenario
    def test_check_win(self):
        error_msg = ("check_win() function from class Board failed to identify the win")
        board_1 = Board()
        for i in range(0,5):
            board_1.add_piece(1,(i,i))
        for i in range(0,5):
            self.assertTrue(board_1.check_win((i,i)),error_msg)

        board_2 = Board()
        for i in reversed(range(10,15)):
            board_2.add_piece(1,(i,i))
        for i in reversed(range(10,15)):
            self.assertTrue(board_2.check_win((i,i)),error_msg)


    ## test that the add_piece() function correctly add
    ## no assert for invalid row/column parameters as these are checked beforehand
    def test_add_piece(self):
        board = Board()
        error_msg_1 = "add_piece() function from class Board returned True to adding a piece to an occupied cell"
        error_msg_2 = "add_piece() function from class Board returned False to adding a piece to empty cell"

        self.assertTrue(board.add_piece(1, (6,7)),error_msg_2)
        self.assertTrue(board.grid[7][6] == 1)
        self.assertFalse(board.add_piece(1,(6,7)),error_msg_1)






