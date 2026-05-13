import random


class NavalBattle:
    """
    A class representing the game "Sea Battle".

    Attributes:
        playing_field: playing field 10x10, where 1 is a ship,
            0 is an empty cell.
    """
    playing_field = []
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    @staticmethod
    def show() -> None:
        """
        Displays the playing field, indicating
        the hidden cells with the "~" symbol,
        the cells with damaged ships with the symbols of the players.
        Moves made "by" the "o" symbol
        """
        for line in NavalBattle.playing_field:
            for cell in line:
                if cell == 0 or cell == 1:
                    print("~", end ="")
                else:
                    print(cell, end="")
            print()

    def shot(self, x: int, y: int) -> None:
        """
        Displays the string "попал" or "мимо" on the screen.
        Args:
            x (int): column number (from 1 to 10).
            y (int): row number (from 1 to 10).
        """
        if not NavalBattle.playing_field:
            print("игровое поле не заполнено")
            return

        current_cell = NavalBattle.playing_field[y - 1][x - 1]

        if current_cell != 0 and current_cell != 1:
            print("ошибка")
            return
        if current_cell == 1:
            NavalBattle.playing_field[y - 1][x - 1] = self.symbol
            print("попал")
        elif current_cell == 0:
            NavalBattle.playing_field[y - 1][x - 1] = 'o'
            print("мимо")

    @staticmethod
    def new_game() -> None:
        """
        Creates a new 10×10 game board and randomly places ships on it:
        1 four-decked, 2 three-decked, 3 two-decked, 4 one-decked
        Ships can't be adjacent to each other
        """
        NavalBattle.playing_field = [[0] * 10 for _ in range(10)]
        ship_lens = [4, 3, 3, 2, 2, 1, 1, 1, 1]
        for size in ship_lens:
            placed = False
            while not placed:
                orientation = random.choice(["горизонтально", "вертикально"])
                if orientation == "горизонтально":
                    row = random.randint(0, 9)
                    col = random.randint(0, 10 - size)
                else:
                    row = random.randint(0, 10 - size)
                    col = random.randint(0, 9)

                if orientation == "горизонтально":
                    row_over, row_under = max(0, row - 1), min(9, row + 1)
                    col_left, col_right = max(0, col - 1), min(9, col + size)
                else:
                    row_over, row_under = max(0, row - 1), min(9, row + size)
                    col_left, col_right = max(0, col - 1), min(9, col + 1)

                clash = False
                for r in range(row_over, row_under + 1):
                    for c in range(col_left, col_right + 1):
                        if NavalBattle.playing_field[r][c] != 0:
                            clash = True
                            break
                    if clash:
                        break

                if not clash:
                    if orientation == "горизонтально":
                        for cell_num in range(size):
                            NavalBattle.playing_field[row][col + cell_num] = 1
                    else:
                        for cell_num in range(size):
                            NavalBattle.playing_field[row + cell_num ][col] = 1
                    placed = True


player1 = NavalBattle('#')
player1.shot(6, 2)
NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle.show()
player1.shot(1,1)
player1.shot(1,1)
NavalBattle.new_game()
NavalBattle.show()
player1.shot(6, 2)
