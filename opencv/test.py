import unittest
from test_boards import *
from board import Board, Piece


class TestWinConditions(unittest.TestCase):
    def test_horizontally_x(self):
        board = Board(board=horizontally_x)
        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), 1)

    def test_horizontally_o(self):
        board = Board(board=horizontally_o)
        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), 2)

    def test_vertically_x(self):
        board = Board(board=vertically_x)
        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), 1)

    def test_vertically_o(self):
        board = Board(board=vertically_o)
        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), 2)

    def test_diagonally_up_x(self):
        board = Board(board=diagonally_up_x)
        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), 1)

    def test_diagonally_up_o(self):
        board = Board(board=diagonally_up_o)
        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), 2)

    def test_diagonally_down_x(self):
        board = Board(board=diagonally_down_x)
        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), 1)

    def test_diagonally_down_o(self):
        board = Board(board=diagonally_down_o)
        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), 2)

    def test_full_board_no_winner(self):
        board = Board(board=full_no_winner)
        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), -1)

    def test_empty_board(self):
        board = Board(board=empty)
        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), -1)

    def test_unfinished_game_no_winner(self):
        board = Board(board=partial_no_winner)
        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), -1)


class TestMoves(unittest.TestCase):
    def test_diagonal_x(self):
        board = Board()
        board.reset_board()

        board.move(Piece.x, 0)
        board.move(Piece.o, 1)

        board.move(Piece.x, 0)
        board.move(Piece.o, 2)

        board.move(Piece.x, 0)
        board.move(Piece.o, 0)

        board.move(Piece.x, 3)
        board.move(Piece.o, 1)

        board.move(Piece.x, 1)
        board.move(Piece.o, 6)

        board.move(Piece.x, 4)
        board.move(Piece.o, 6)

        board.move(Piece.x, 0)
        board.move(Piece.o, 2)

        board.move(Piece.x, 1)
        board.move(Piece.o, 5)

        board.move(Piece.x, 3)
        board.move(Piece.o, 6)

        board.move(Piece.x, 2)

        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), 1)

    def test_diagonal_o(self):
        board = Board()
        board.reset_board()

        board.move(Piece.x, 0)
        board.move(Piece.o, 1)

        board.move(Piece.x, 0)
        board.move(Piece.o, 2)

        board.move(Piece.x, 0)
        board.move(Piece.o, 0)

        board.move(Piece.x, 3)
        board.move(Piece.o, 1)

        board.move(Piece.x, 1)
        board.move(Piece.o, 6)

        board.move(Piece.x, 4)
        board.move(Piece.o, 6)

        board.move(Piece.x, 0)
        board.move(Piece.o, 2)

        board.move(Piece.x, 1)
        board.move(Piece.o, 5)

        board.move(Piece.x, 3)
        board.move(Piece.o, 6)

        board.move(Piece.x, 5)
        board.move(Piece.o, 6)

        self.assertEqual(board.check_winner(show_winner=False, draw_board=False), 2)


if __name__ == "__main__":
    unittest.main()
