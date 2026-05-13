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
        current_cell = NavalBattle.playing_field[y - 1][x - 1]
        if current_cell == 1:
            NavalBattle.playing_field[y - 1][x - 1] = self.symbol
            print("попал")
        elif current_cell == 0:
            NavalBattle.playing_field[y - 1][x - 1] = 'o'
            print("мимо")


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
player1 = NavalBattle('#')
player2 = NavalBattle('*')
NavalBattle.show()
player1.shot(6, 2)
player1.shot(6, 1)
player2.shot(6, 3)
player2.shot(6, 4)
player2.shot(6, 5)
player2.shot(3, 3)
player2.show()
player1.shot(1, 1)
NavalBattle.show()
