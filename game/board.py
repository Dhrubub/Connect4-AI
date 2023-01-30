from enum import Enum
from typing import Literal
import numpy as np
import copy


class Piece(Enum):
    x: str = "X"
    o: str = "O"
    empty: str = " "


class Board:
    def __init__(self, board, player1, player2) -> None:
        self.board: list[list[str]] = copy.deepcopy(board)
        self.player1: Piece = player1
        self.player2: Piece = player2

    def move(self, piece: Piece, col: int) -> bool:
        row: int = self.is_valid(col)
        if row < 0:
            return False

        self.board[6 - row - 1][col] = piece.value
        return True

    def is_valid(self, col) -> int:
        try:
            if not 0 <= col <= 7:
                raise IndexError
            board_col: list = np.array(self.board).T.tolist()[col]
            board_col.reverse()
            row: int = board_col.index(Piece.empty.value)

            return row

        except (ValueError, IndexError):
            return -1
