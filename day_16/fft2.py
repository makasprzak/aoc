def calculate_sums(signal: []) -> []:
    sums = []
    last_sum = 0
    for i in signal:
        last_sum += i
        sums.append(last_sum)
    return sums


class DigitCalculator:
    def __init__(self, sums):
        self.sums = sums

    def calculate_digit(self, position: int, offset=0) -> int:
        pos = 0
        neg = 0
        word_len = (position + 1 + offset) * 4
        part_len = int(word_len / 4)
        for i in range(0, len(self.sums), word_len):
            pos += self.get_sum(2, part_len, i, offset) - (self.get_sum(1, part_len, i, offset) if i > 0 or position > 0 else 0)
            neg += self.get_sum(4, part_len, i, offset) - self.get_sum(3, part_len, i, offset)
        return abs(pos - neg) % 10

    def get_sum(self, offset, part_len, i, big_offset):
        idx = i - big_offset + offset * part_len - 2
        return self.sums[idx] if idx < len(self.sums) else self.sums[-1]


def create_digit_calculator(signal: []) -> DigitCalculator:
    return DigitCalculator(calculate_sums(signal))