class ChessFigure:
    def __init__(self):
        self.color = "white"
        self.place = None

    def change_color(self):
        # if isinstance(self.color, str):
        #     self.color = self.color.lower()
        if self.color == "black":
            self.color = "white"
        else:
            self.color = "black"

    def change_place(self, some_tuple: tuple):
        temp = [x for x in some_tuple if 0 <= x <= 7]
        if len(temp) == 2:
            self.place = temp
        else:
            raise ValueError("Invalid position. Values must be in the range [0, 7].")

    def check_move(self, new_position: tuple):
        raise NotImplementedError("Subclasses must implement this method.")


class Pawn(ChessFigure):
    def check_move(self, new_position: tuple) -> bool:
        if 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
            temp1 = new_position[0] - self.place[0]
            temp2 = new_position[1] - self.place[1]
            if temp1 == 1 and temp2 == 0 and self.color == "white":
                return True
            elif temp1 == -1 and temp2 == 0 and self.color == "black":
                return True
            else:
                return False
        else:
            raise ValueError("Invalid position. Values must be in the range [0, 7].")

    def __str__(self):
        return f"Pawn"


class Knight(ChessFigure):
    def check_move(self, new_position: tuple) -> bool:
        if 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
            move = (
                (self.place[0] + 1, self.place[1] + 2),
                (self.place[0] + 1, self.place[1] - 2),
                (self.place[0] + 2, self.place[1] + 1),
                (self.place[0] + 2, self.place[1] - 1),
                (self.place[0] - 1, self.place[1] + 2),
                (self.place[0] - 1, self.place[1] - 2),
                (self.place[0] - 2, self.place[1] + 1),
                (self.place[0] - 2, self.place[1] - 1)
            )
            return new_position in move
        else:
            raise ValueError("Invalid position. Values must be in the range [0, 7].")

    def __str__(self):
        return f"Knight"


class Bishop(ChessFigure):
    def check_move(self, new_position: tuple) -> bool:
        if 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
            temp1 = new_position[0] - self.place[0]
            temp2 = new_position[1] - self.place[1]
            return abs(temp1) == abs(temp2)
        else:
            raise ValueError("Invalid position. Values must be in the range [0, 7].")

    def __str__(self):
        return f"Bishop"


class Rook(ChessFigure):
    def check_move(self, new_position: tuple) -> bool:
        if 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
            temp1 = new_position[0] - self.place[0]
            temp2 = new_position[1] - self.place[1]
            if not temp1 or not temp2:
                return True
            else:
                return False
        else:
            raise ValueError("Invalid position. Values must be in the range [0, 7].")

    def __str__(self):
        return f"Rook"


class Queen(ChessFigure):
    def check_move(self, new_position: tuple) -> bool:
        if 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
            temp1 = new_position[0] - self.place[0]
            temp2 = new_position[1] - self.place[1]
            if not temp1 or not temp2 or (abs(temp1) == abs(temp2)):
                return True
            else:
                return False
        else:
            raise ValueError("Invalid position. Values must be in the range [0, 7].")

    def __str__(self):
        return f"Queen"


class King(ChessFigure):
    def check_move(self, new_position: tuple) -> bool:
        if 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
            temp1 = new_position[0] - self.place[0]
            temp2 = new_position[1] - self.place[1]
            if abs(temp2) <= 1 and abs(temp1) <= 1:
                return True
            else:
                return False
        else:
            raise ValueError("Invalid position. Values must be in the range [0, 7].")

    def __str__(self):
        return f"King"


pawn1 = Pawn()
print(pawn1.color)
pawn1.change_color()
print(pawn1.color)
pawn1.change_place((1, 1))
print(pawn1.check_move((1, 4)))
print(pawn1.check_move((1, 3)))

knight1 = Knight()
knight1.change_place((1, 1))
print(knight1.check_move((1, 4)))
print(knight1.check_move((4, 7)))
print(knight1.check_move((5, 6)))
print(knight1.check_move((1, 4)))
print(knight1.check_move((1, 3)))

print("------------------------------------------")
bishop1 = Bishop()
bishop1.change_place((1, 1))
print(bishop1.check_move((4, 6)))
print(bishop1.check_move((4, 7)))
print(bishop1.check_move((5, 6)))
print(bishop1.check_move((1, 4)))
print(bishop1.check_move((1, 3)))

print("------------------------------------------")
rook1 = Rook()
rook1.change_place((1, 1))
print(rook1.check_move((4, 5)))
print(rook1.check_move((5, 4)))
print(rook1.check_move((3, 4)))
print(rook1.check_move((3, 6)))
print(rook1.check_move((1, 3)))

print("------------------------------------------")
queen1 = Queen()
queen1.change_place((1, 1))
print(queen1.check_move((4, 5)))
print(queen1.check_move((5, 4)))
print(queen1.check_move((3, 4)))
print(queen1.check_move((3, 6)))
print(queen1.check_move((1, 3)))
print(queen1.check_move((7, 1)))
print(queen1.check_move((3, 3)))
print(queen1.check_move((2, 0)))

print("------------------------------------------")
king1 = King()
king1.change_place((1, 1))
print(king1.check_move((4, 5)))
print(king1.check_move((5, 4)))
print(king1.check_move((3, 4)))
print(king1.check_move((3, 6)))
print(king1.check_move((1, 3)))
print(king1.check_move((7, 1)))
print(king1.check_move((3, 3)))
print(king1.check_move((2, 0)))
print(king1.check_move((1, 2)))
print(king1.check_move((2, 2)))
print(king1.check_move((2, 3)))


def get_possible_moves(pieces, new_position: list) -> list:
    valid_pieces = []
    for piece in pieces:
        if piece.check_move(new_position):
            valid_pieces.append(str(piece))
    return valid_pieces


figures = [pawn1, knight1, bishop1, rook1, queen1, king1]

print(get_possible_moves(figures, [0, 1]))


