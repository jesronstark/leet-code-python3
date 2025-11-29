















e
class Solution:
    def calculate(self, s: str) -> int:
        def helper(s: str, index: int) -> (int, int):
            stack = []
            num = 0
            sign = '+'
            while index < len(s):
                char = s[index]
                if char.isdigit():
                    num = num * 10 + int(char)
                if char == '(':
                    num, index = helper(s, index + 1)
                if (not char.isdigit() and char != ' ') or index == len(s) - 1:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        prev_num = stack.pop()
                        # Ensure the division truncates towards zero
                        stack.append(int(prev_num / num))
                    sign = char
                    num = 0
                if char == ')':
                    break
                index += 1
            return sum(stack), index

        result, _ = helper(s, 0)
        return result
