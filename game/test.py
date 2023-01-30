import unittest
from game import Game
from test_boards import *
from board import Piece


class TestWinConditions(unittest.TestCase):
    def test_horizontally_x(self):
        game: Game = Game(board=horizontally_x)
        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), 1)

    def test_horizontally_o(self):
        game: Game = Game(board=horizontally_o)
        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), 2)

    def test_vertically_x(self):
        game: Game = Game(board=vertically_x)
        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), 1)

    def test_vertically_o(self):
        game: Game = Game(board=vertically_o)
        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), 2)

    def test_diagonally_up_x(self):
        game: Game = Game(board=diagonally_up_x)
        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), 1)

    def test_diagonally_up_o(self):
        game: Game = Game(board=diagonally_up_o)
        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), 2)

    def test_diagonally_down_x(self):
        game: Game = Game(board=diagonally_down_x)
        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), 1)

    def test_diagonally_down_o(self):
        game: Game = Game(board=diagonally_down_o)
        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), 2)

    def test_full_board_no_winner(self):
        game: Game = Game(board=full_no_winner)
        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), -1)

    def test_empty_board(self):
        game: Game = Game(board=empty)
        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), -1)

    def test_unfinished_game_no_winner(self):
        game: Game = Game(board=partial_no_winner)
        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), -1)


class TestMoves(unittest.TestCase):
    def test_diagonal_x(self):
        game: Game = Game()

        game.board.move(Piece.x, 0)
        game.board.move(Piece.o, 1)

        game.board.move(Piece.x, 0)
        game.board.move(Piece.o, 2)

        game.board.move(Piece.x, 0)
        game.board.move(Piece.o, 0)

        game.board.move(Piece.x, 3)
        game.board.move(Piece.o, 1)

        game.board.move(Piece.x, 1)
        game.board.move(Piece.o, 6)

        game.board.move(Piece.x, 4)
        game.board.move(Piece.o, 6)

        game.board.move(Piece.x, 0)
        game.board.move(Piece.o, 2)

        game.board.move(Piece.x, 1)
        game.board.move(Piece.o, 5)

        game.board.move(Piece.x, 3)
        game.board.move(Piece.o, 6)

        game.board.move(Piece.x, 2)

        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), 1)

    def test_diagonal_o(self):
        game: Game = Game()

        game.board.move(Piece.x, 0)
        game.board.move(Piece.o, 1)

        game.board.move(Piece.x, 0)
        game.board.move(Piece.o, 2)

        game.board.move(Piece.x, 0)
        game.board.move(Piece.o, 0)

        game.board.move(Piece.x, 3)
        game.board.move(Piece.o, 1)

        game.board.move(Piece.x, 1)
        game.board.move(Piece.o, 6)

        game.board.move(Piece.x, 4)
        game.board.move(Piece.o, 6)

        game.board.move(Piece.x, 0)
        game.board.move(Piece.o, 2)

        game.board.move(Piece.x, 1)
        game.board.move(Piece.o, 5)

        game.board.move(Piece.x, 3)
        game.board.move(Piece.o, 6)

        game.board.move(Piece.x, 5)
        game.board.move(Piece.o, 6)

        self.assertEqual(game.check_winner(show_winner=False, draw_board=False), 2)


if __name__ == "__main__":
    unittest.main()
