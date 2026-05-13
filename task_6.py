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
    ROMAN_SYMBOLS = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX'
        , 'V', 'IV', 'I']

    def __init__(self, value) -> None:
        """
        Initializes an instance of a Roman number.
        Args:
            value (str or int): a string with a Roman number or an integer number.
            If the value is invalid, both rom_value and int_value remain None.
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

    def decimal_number(self) -> int | None:
        """
        Returns the decimal equivalent of a Roman number or None
        if the number is invalid.
        """
        return self.int_value

    def roman_number(self) -> str | None:
        """
        Returns a string — the Roman equivalent of a number or None
        if the number is invalid.
        """
        return self.rom_value

    @staticmethod
    def _to_roman(num: int) -> str | None:
        """
        Converts an integer to a Roman numeral string.
        Args:
            num (int):  the integer to convert.
        Returns:
            (str or None): the Roman numeral string, or None if impossible.
        """
        if not RomanNumber.is_int(num):
            return None
        result = ""
        for index in range(len(RomanNumber.DECIMAL_NUMS)):
            while num >= RomanNumber.DECIMAL_NUMS[index]:
                result += RomanNumber.ROMAN_SYMBOLS[index]
                num -= RomanNumber.DECIMAL_NUMS[index]
        return result

    def arithmetic(self, other, operation: str) -> 'RomanNumber':
        """
        Performs an arithmetic operation between two Roman numbers.
        Takes the decimal values of self and other, performs the specified
        operation, converts the result back to a Roman number
        Args:
            other: the Roman number to perform the operation with.
            operation (str): the operation to perform.
        Returns:
            RomanNumber: a new RomanNumber object with the result.
        """
        if self.int_value is None or other.int_value is None:
            print("ошибка")
            return RomanNumber(0)

        match operation:
            case '+':
                result = self.int_value + other.int_value
            case '-':
                result = self.int_value - other.int_value
            case '*':
                result = self.int_value * other.int_value
            case '/':
                result = self.int_value / other.int_value
                if result != int(result):
                    print("ошибка")
                    return RomanNumber(0)
                result = int(result)
            case '//':
                result = self.int_value // other.int_value
            case '%':
                result = self.int_value % other.int_value
            case '**':
                result = self.int_value ** other.int_value
            case _:
                print("ошибка")
                return RomanNumber(0)

        if not RomanNumber.is_int(result):
            print("ошибка")
            return RomanNumber(0)

        roman_res = RomanNumber._to_roman(result)
        if roman_res is None:
            print("ошибка")
            return RomanNumber(0)

        return RomanNumber(roman_res)

    def __add__(self, other):
        """Returns the sum of two Roman numbers"""
        return self.arithmetic(other, '+')

    def __sub__(self, other):
        """Returns the sum of two Roman numbers:"""
        return self.arithmetic(other, '-')

    def __mul__(self, other):
        """Returns the product of two Roman numbers"""
        return self.arithmetic(other, '*')

    def __truediv__(self, other):
        """Returns the true division of two Roman numbers"""
        return self.arithmetic(other, '/')

    def __floordiv__(self, other):
        """Returns the floor division of two Roman numbers"""
        return self.arithmetic(other, '//')

    def __mod__(self, other):
        """Returns the modulo of two Roman numbers"""
        return self.arithmetic(other, '%')

    def __pow__(self, other):
        """Returns the power of two Roman numbers"""
        return self.arithmetic(other, '**')

    def __isub__(self, other):
        """Subtracts other from self in place"""
        result = self.arithmetic(other, '-')
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self

    def __iadd__(self, other):
        """Adds other to self in place"""
        result = self.arithmetic(other, '+')
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self

    def __imul__(self, other):
        """Multiplies self by other in place"""
        result = self.arithmetic(other, '*')
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self

    def __itruediv__(self, other):
        """True divides self by other in place"""
        result = self.arithmetic(other, '/')
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self

    def __ifloordiv__(self, other):
        """Floor divides self by other in place"""
        result = self.arithmetic(other, '//')
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self

    def __imod__(self, other):
        """Modulo in plac"""
        result = self.arithmetic(other, '%')
        self.int_value = result.int_value
        self.rom_value = result.rom_value
        return self

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


a = RomanNumber('XI')
b = RomanNumber('VII')
c = a + b
print(c)
d = RomanNumber('XII')
print(c - d)
e = RomanNumber('XXXIV')
f = e * a
print(f)
print(f / RomanNumber('II') )
g = f / b
print(g.rom_value)
print(f // b)
print(f % b)
print(RomanNumber('II') ** RomanNumber('X'))
a -= b
print(a)
b += RomanNumber('XX')
print(b)
b /= RomanNumber('III')
print(b)
b *= a
print(b)
b /= RomanNumber('X')
print(b)
e //= RomanNumber('X')
print(e)
e %= RomanNumber('II')
print(e)
