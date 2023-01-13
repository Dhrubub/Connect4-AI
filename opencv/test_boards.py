horizontally_x: list = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", "x", "x", "x", "x", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]

horizontally_o: list = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "o", "o", "o", "o"],
    [".", ".", ".", ".", ".", ".", "."],
]

vertically_x: list = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "x", ".", ".", "."],
    [".", ".", ".", "x", ".", ".", "."],
    [".", ".", ".", "x", ".", ".", "."],
    [".", ".", ".", "x", ".", ".", "."],
]

vertically_o: list = [
    [".", ".", ".", ".", ".", ".", "o"],
    [".", ".", ".", ".", ".", ".", "o"],
    [".", ".", ".", ".", ".", ".", "o"],
    [".", ".", ".", ".", ".", ".", "o"],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]

diagonally_up_x: list = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "x", ".", ".", "."],
    [".", ".", "x", ".", ".", ".", "."],
    [".", "x", ".", ".", ".", ".", "."],
    ["x", ".", ".", ".", ".", ".", "."],
]
diagonally_up_o: list = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "o"],
    [".", ".", ".", ".", ".", "o", "."],
    [".", ".", ".", ".", "o", ".", "."],
    [".", ".", ".", "o", ".", ".", "."],
]

diagonally_down_x: list = [
    ["x", ".", ".", ".", ".", ".", "."],
    [".", "x", ".", ".", ".", ".", "."],
    [".", ".", "x", ".", ".", ".", "."],
    [".", ".", ".", "x", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]

diagonally_down_o: list = [
    [".", ".", ".", "o", ".", ".", "."],
    [".", ".", ".", ".", "o", ".", "."],
    [".", ".", ".", ".", ".", "o", "."],
    [".", ".", ".", ".", ".", ".", "o"],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]

empty: list = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]

full_no_winner: list = [
    ["x", "x", "x", "o", "o", "o", "x"],
    ["o", "o", "o", "x", "x", "x", "o"],
    ["x", "x", "x", "o", "o", "o", "x"],
    ["o", "o", "o", "x", "x", "x", "o"],
    ["x", "x", "x", "o", "o", "o", "x"],
    ["o", "o", "o", "x", "x", "x", "o"],
]

partial_no_winner: list = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", "x", "o", "x", ".", "."],
    [".", ".", "o", "x", "o", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    ["x", "o", "x", "o", ".", ".", "."],
]
