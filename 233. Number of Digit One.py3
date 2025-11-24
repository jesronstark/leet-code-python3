




























class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1  # Represents the current digit position (1 for ones, 10 for tens, etc.)

        while n // factor != 0:
            lower = n % factor
            current = (n // factor) % 10
            higher = n // (factor * 10)

            if current == 0:
                count += higher * factor
            elif current == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor

            factor *= 10

        return count
