class PuzzlePiece:
    shape: list[list[bool]]
    nr_of_used_spaces: int

    def __init__(self, shape: list[list[bool]]) -> None:
        self.shape = shape
        self.nr_of_used_spaces = sum(1 for row in shape for cell in row if cell)


class Puzzle:
    width: int
    height: int
    number_of_pieces: list[int]

    def __init__(self, width: int, height: int, piece_indexes: list[int]) -> None:
        self.width = width
        self.height = height
        self.number_of_pieces = piece_indexes


def parse():
    file = open("./12/input.txt", "r")
    pieces = list[PuzzlePiece]()
    for _ in range(6):
        file.readline()
        shape = [[c == "#" for c in file.readline().strip()] for _ in range(3)]
        pieces.append(PuzzlePiece(shape))
        file.readline()

    puzzles = list[Puzzle]()
    for line in file:
        parts = line.strip().split(": ")
        width, height = map(int, parts[0].split("x"))
        piece_indexes = [int(x) for x in parts[1].split()]
        puzzles.append(Puzzle(width, height, piece_indexes))

    return pieces, puzzles


def process(pieces: list[PuzzlePiece], puzzles: list[Puzzle]) -> int:
    solvable_puzzles = 0

    for puzzle in puzzles:
        total_used_spaces = sum(
            [
                pieces[index].nr_of_used_spaces * puzzle.number_of_pieces[index]
                for index in range(6)
            ]
        )
        possible_spaces = puzzle.width * puzzle.height
        if possible_spaces < total_used_spaces:
            continue

        solvable_puzzles += 1

    return solvable_puzzles


pieces, puzzles = parse()
solvable_puzzles = process(pieces, puzzles)
print(solvable_puzzles)
