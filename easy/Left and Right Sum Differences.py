from typing import List


class Solution:
    def leftRightDifference2(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = []

        for i, v in enumerate(nums):
            left = 0 if i == 0 else sum(nums[:i])

            right = 0 if i == l-1 else sum(nums[i+1: l])

            res.append(abs(left - right))

        return res

    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = []
        c_sum = [0]

        for i in range(l):
            c_sum.append(c_sum[i] + nums[i])

        for i in range(l):
            left = c_sum[i]
            right = c_sum[l] - c_sum[i+1]
            res.append(abs(left-right))

        return res
