class RomanNumber:
    """
    A class representing a Roman number.
    Attributes:
        rom_value (str or None): the Roman number, or None if the string is invalid.
    """
    ROMAN_NUMS = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    def __init__(self, value: str) -> None:
        """
        Initializes an instance of a Roman number.
        Args:
            value (str): a string with a Roman number.
        """
        if RomanNumber.is_roman(value):
            self.rom_value = value
        else:
            print("ошибка")
            self.rom_value = None

    def decimal_number(self) -> int:
        """
        Returns the decimal equivalent of a Roman number.
        """
        if self.rom_value is None:
            return None

        result = 0
        prev_num = 0
        for char in reversed(self.rom_value):
            current_num = RomanNumber.ROMAN_NUMS[char]
            if current_num < prev_num:
                result  -= current_num
            else:
                result += current_num
            prev_num = current_num
        return result

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

    def __str__(self) -> str:
        """Returns a string representation."""
        if self.rom_value is None:
            return 'None'
        return str(self.rom_value)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Roman number for display in lists.
        Shows the roman value as is, or 'None' if the value is invalid.
        """
        if self.rom_value is None:
            return 'None'
        return str(self.rom_value)


num_1 = RomanNumber('VI')
print(num_1.rom_value)
print(num_1.decimal_number())
print(num_1)
num_2 = RomanNumber('IIII')
print(num_2.rom_value)
num_3 = RomanNumber('XXIV')
print(num_3.decimal_number())
num_4 = RomanNumber('QER2')
nums = []
nums.append(num_1)
nums.append(num_2)
nums.append(num_3)
nums.append(num_4)
print(nums)
print(RomanNumber.is_roman('MMMCMLXXXVI'))
print(RomanNumber.is_roman('MMМMMLXXXVI'))
