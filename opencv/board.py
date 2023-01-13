from enum import Enum
from typing import Literal
import numpy as np


class Piece(Enum):
    x: str = "X"
    o: str = "O"
    empty: str = " "


empty_board: "list[list[str]]" = [
    [Piece.empty.value for _ in range(7)] for _ in range(6)
]


class Board:
    def __init__(self, board: list = empty_board) -> None:
        self.board: list[list[str]] = board
        self.player1: Piece = Piece.x
        self.player2: Piece = Piece.o

        self.winner: int = -1

    def move(self, piece: Piece, col: int) -> bool:
        if self.winner != -1:
            print("Game has ended.", end=" ")
            self.game_over()
            return True

        row: int = self.is_valid(col)
        if row < 0:
            return False

        self.board[6 - row - 1][col] = piece.value
        return True

    def is_valid(self, col) -> int:
        board_col: list = np.array(self.board).T.tolist()[col]
        board_col.reverse()

        try:
            row: int = board_col.index(Piece.empty.value)
            return row
        except ValueError:
            return -1

    def validate_horizontal(self) -> None:
        for j in range(6):
            for i in range(4):
                state: list[str] = self.board[j][i : i + 4]
                self.check_state(state)

    def validate_vertical(self) -> None:
        board_t: list[list[str]] = np.array(self.board).T.tolist()

        for j in range(7):
            for i in range(3):
                state: list[str] = board_t[j][i : i + 4]
                self.check_state(state)

    def validate_diagonal_down(self) -> None:
        for j in range(3):
            for i in range(4):
                state: list[str] = [self.board[j + n][i + n] for n in range(4)]
                self.check_state(state)

    def validate_diagonal_up(self) -> None:
        for j in range(3, 6):
            for i in range(4):
                state: list[str] = [self.board[j - n][i + n] for n in range(4)]
                self.check_state(state)

    def check_state(self, state) -> None:
        s: str = "".join(state)
        if s == self.player1.value * 4:
            self.winner = 1

        elif s == self.player2.value * 4:
            self.winner = 2

    def check_winner(self, show_winner=True, draw_board=True) -> int:
        self.validate_horizontal()
        self.validate_vertical()
        self.validate_diagonal_down()
        self.validate_diagonal_up()

        if self.winner != -1:
            self.game_over(show_winner, draw_board)

        return self.winner

    def game_over(self, show_winner=True, draw_board=True) -> None:
        piece: str = self.player1 if self.winner == 1 else self.player2
        if draw_board:
            self.draw_board()
        if show_winner:
            print(f"The winner is player {self.winner} who had piece {piece.value}.")

    def reset_board(self):
        self.board = [[Piece.empty.value for _ in range(7)] for _ in range(6)]

    def draw_board(self) -> None:
        print("-" * 29)

        for j in range(6):
            for i in range(7):
                if i == 0:
                    print("| ", end="")
                print(self.board[j][i], end=" | ")
            print()
            print("-" * 29)
