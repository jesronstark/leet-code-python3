





















from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if indexDiff <= 0 or valueDiff < 0:
            return False

        sorted_list = SortedList()
        for i, num in enumerate(nums):
            # Find the insertion point for num - valueDiff
            pos = sorted_list.bisect_left(num - valueDiff)
            # Check if the number at this position is within num + valueDiff
            if pos < len(sorted_list) and sorted_list[pos] <= num + valueDiff:
                return True

            # Add current number to the sorted list
            sorted_list.add(num)

            # Ensure the sorted list does not exceed the size indexDiff
            if len(sorted_list) > indexDiff:
                sorted_list.remove(nums[i - indexDiff])

        return False

