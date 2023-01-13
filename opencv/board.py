from typing import Literal
import numpy as np
from test_boards import horizontally_x

empty_board: "list[list[str]]" = [["." for _ in range(7)] for _ in range(6)]


class Board:
    def __init__(self, board=empty_board) -> None:
        self.board: list[list[str]] = board
        self.player1: Literal["x"] = "x"
        self.player2: Literal["o"] = "o"

        self.winner: int = -1

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
        if s == self.player1 * 4:
            self.winner = 1

        elif s == self.player2 * 4:
            self.winner = 2

    def check_winner(self) -> int:
        self.validate_horizontal()
        self.validate_vertical()
        self.validate_diagonal_down()
        self.validate_diagonal_up()

        if self.winner != -1:
            self.game_over()

        return self.winner

    def game_over(self) -> None:
        token: str = self.player1 if self.winner == 1 else self.player2
        print(f"The winner is player {self.winner} who had token {token}.")
