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


class Game:
    def __init__(
        self,
        player1: PlayerType = PlayerType.human,
        player2: PlayerType = PlayerType.human,
    ) -> None:
        self.player1: Player = Player(Piece.x, player1)
        self.player2: Player = Player(Piece.o, player2)

        self.cur: Player = self.player1

        self.board: Board = Board()

        self.take_turn()
        # self.draw_board()

    def take_turn(self) -> None:
        self.board.draw_board()
        try:
            col: int = int(input(f"Player {self.cur.piece.value} to move: "))

            valid: bool = self.board.move(piece=self.cur.piece, col=col)

            if not valid:
                raise ValueError()

            winner: int = self.board.check_winner()
            if winner > 0:
                print("Good game.")
                return

            self.cur = self.player2 if self.cur == self.player1 else self.player1
            self.take_turn()

        except ValueError:
            print("Invalid move. Enter a single digit between 0-6")
            self.take_turn()


if __name__ == "__main__":
    game = Game()
