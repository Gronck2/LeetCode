from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_nums = {v: i for i, v in enumerate(nums)}

        for i, v in enumerate(nums):
            s = target - v
            if s in hash_nums and hash_nums[s] != i:
                return [i, hash_nums[s]]
