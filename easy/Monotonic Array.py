from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        pm = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if pm == 1:
                    return False
                pm = -1

            if nums[i - 1] < nums[i]:
                if pm == -1:
                    return False
                pm = 1

        return True


print(Solution().isMonotonic([1,3,2]))