class RomanNumber:
    """
    A class representing a Roman number.
    Attributes:
        rom_value (str or None): the Roman number, or None if the string is invalid.
        int_value (int or None): decimal value or None.
    """
    ROMAN_NUMS = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

    DECIMAL_NUMS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ROMAN_SYMBOLS = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX',
                     'V', 'IV', 'I']
    
    def __init__(self, value: str|int) -> None:
        """
        Initializes an instance of a Roman number.
        Args:
            value (str or int): a string with a Roman number or an integer number.
        """
        self.rom_value = None
        self.int_value = None
        if isinstance(value, str):
            if RomanNumber.is_roman(value):
                self.rom_value = value
                result = 0
                prev_num = 0
                for char in reversed(self.rom_value):
                    current_num = RomanNumber.ROMAN_NUMS[char]
                    if current_num < prev_num:
                        result -= current_num
                    else:
                        result += current_num
                    prev_num = current_num
                self.int_value = result
            else:
                print("ошибка")

        elif isinstance(value, int):
            if RomanNumber.is_int(value):
                self.int_value = value
                num = value
                result = ""
                for ind in range(len(RomanNumber.DECIMAL_NUMS)):
                    while num >= RomanNumber.DECIMAL_NUMS[ind]:
                        result += RomanNumber.ROMAN_SYMBOLS[ind]
                        num -= RomanNumber.DECIMAL_NUMS[ind]
                self.rom_value = result
            else:
                print("ошибка")
        else:
            print("ошибка")

    def decimal_number(self) -> int | None:
        """
        Returns the decimal equivalent of a Roman number or None.
        """
        return self.int_value

    def roman_number(self) -> str | None:
        """
        Returns a string — the Roman equivalent of a number or None.
        """
        return self.rom_value

    @staticmethod
    def is_roman(value: str) -> bool:
        """
        Checks whether a string is a correct Roman number.

        Arguments:
            value (str): the string to check.

        Returns:
            bool: True if the string is a Roman number, otherwise False.
        """
        if not isinstance(value, str) or len(value) == 0:
            return False

        for char in value:
            if char not in RomanNumber.ROMAN_NUMS:
                return False

        for symbol in ['I', 'X', 'C', 'M']:
            if symbol * 4 in value:
                return False
        for digit in ['V', 'L', 'D']:
            if value.count(digit) > 1:
                return False

        for ind in range(len(value) - 1):
            current_sym = value[ind]
            next_sym = value[ind + 1]
            if current_sym in ['V', 'L', 'D']:
                if RomanNumber.ROMAN_NUMS[next_sym] > RomanNumber.ROMAN_NUMS[current_sym]:
                    return False

        right_pairs = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        remaining_chars = value
        for pair in right_pairs:
            remaining_chars = remaining_chars.replace(pair, '')

        prev_val = float('inf')
        for char in remaining_chars:
            curr_val = RomanNumber.ROMAN_NUMS[char]
            if curr_val > prev_val:
                return False
            prev_val = curr_val

        return True

    @staticmethod
    def is_int(value: int) -> bool:
        """
        Checks whether an integer can be represented as a Roman number.
        Args:
            value (int): an integer to be checked.
        Returns:
            bool: True if the number can be represented as a Roman number,
            otherwise False.
        """
        if not isinstance(value, int):
            return False
        return 1 <= value <= 3999

    def __str__(self) -> str:
        """Returns a string representation."""
        if self.rom_value is not None:
            return str(self.rom_value)
        elif self.int_value is not None:
            return str(self.int_value)
        return 'None'

    def __repr__(self) -> str:
        """
        Returns a string representation of the Roman number for display in lists.
        Shows the roman value as is, or 'None' if the value is invalid.
        """
        if self.rom_value is not None:
            return str(self.rom_value)
        elif self.int_value is not None:
            return str(self.int_value)
        return 'None'


num_1 = RomanNumber(214)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)
num_2 = RomanNumber(5690)
print(num_2.int_value)
num_3 = RomanNumber('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)
print(RomanNumber.is_int(-614))
print(RomanNumber.is_int(3758))
