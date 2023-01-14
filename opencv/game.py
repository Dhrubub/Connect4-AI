from enum import Enum
from typing import Literal
from board import Board, Piece
import numpy as np


class PlayerType(Enum):
    human: str = "human"
    ai: str = "ai"


class Player:
    def __init__(
        self, piece: Piece = Piece.x, type: PlayerType = PlayerType.human
    ) -> None:
        self.piece: Piece = piece
        self.type: Player = type

    def take_turn(self, board) -> int:
        col: str = input(f"Player {self.piece.value} to move: ")

        return col


empty_board: "list[list[str]]" = [
    [Piece.empty.value for _ in range(7)] for _ in range(6)
]

import copy


class Game:
    def __init__(
        self,
        player1_type: PlayerType = PlayerType.human,
        player2_type: PlayerType = PlayerType.human,
        board: list = copy.deepcopy(empty_board),
    ) -> None:
        self.player1: Player = Player(Piece.x, player1_type)
        self.player2: Player = Player(Piece.o, player2_type)

        self.cur: Player = self.player1

        self.board: Board = Board(board, self.player1.piece, self.player2.piece)
        self.winner: int = -1
        self.take_turn()
        # self.draw_board()

    def take_turn(self):
        self.draw_board()
        if self.winner != -1:
            print("Game has ended.", end=" ")
            self.game_over()
            return

        try:
            col: int = int(self.cur.take_turn(board=self.board.board))
            valid: bool = self.board.move(piece=self.cur.piece, col=col)

            if not valid:
                raise ValueError()

            winner: int = self.check_winner()
            if winner > 0:
                print("Good game.")
                return

        except ValueError:
            print("Invalid move. Enter a single digit between 0-6")
            self.take_turn()

        self.cur = self.player2 if self.cur == self.player1 else self.player1
        self.take_turn()

    def validate_horizontal(self) -> None:
        for j in range(6):
            for i in range(4):
                state: list[str] = self.board.board[j][i : i + 4]
                self.check_state(state)

    def validate_vertical(self) -> None:
        board_t: list[list[str]] = np.array(self.board.board).T.tolist()

        for j in range(7):
            for i in range(3):
                state: list[str] = board_t[j][i : i + 4]
                self.check_state(state)

    def validate_diagonal_down(self) -> None:
        for j in range(3):
            for i in range(4):
                state: list[str] = [self.board.board[j + n][i + n] for n in range(4)]
                self.check_state(state)

    def validate_diagonal_up(self) -> None:
        for j in range(3, 6):
            for i in range(4):
                state: list[str] = [self.board.board[j - n][i + n] for n in range(4)]
                self.check_state(state)

    def check_state(self, state) -> None:
        s: str = "".join(state)
        if s == self.player1.piece.value * 4:
            self.winner = 1

        elif s == self.player2.piece.value * 4:
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
        player: Player = self.player1 if self.winner == 1 else self.player2
        if draw_board:
            self.draw_board()
        if show_winner:
            print(
                f"The winner is player {self.winner} who had piece {player.piece.value}."
            )

    def draw_board(self) -> None:
        print("-" * 29)

        for j in range(6):
            for i in range(7):
                if i == 0:
                    print("| ", end="")
                print(self.board.board[j][i], end=" | ")
            print()
            print("-" * 29)

    def reset_board(self) -> None:
        self.board.board = copy.deepcopy(empty_board)


if __name__ == "__main__":
    game: Game = Game()
