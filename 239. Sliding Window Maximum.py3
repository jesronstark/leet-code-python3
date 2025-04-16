from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        result = []
        dq = deque()  # Stores indices of potential max elements

        for i in range(len(nums)):
            # Remove indices that are out of the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove indices whose corresponding values are less than nums[i]
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Append the current max to the result list
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
