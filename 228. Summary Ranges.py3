












from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result

        start = nums[0]
        end = nums[0]

        for n in nums[1:]:
            if n == end + 1:
                end = n
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")
                start = end = n

        # Add the final range
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")

        return result
