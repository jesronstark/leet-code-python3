from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # First pass: calculate prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Second pass: calculate suffix products and multiply with prefix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
