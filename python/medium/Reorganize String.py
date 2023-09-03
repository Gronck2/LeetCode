from collections import defaultdict


class Solution:
    def reorganizeString(self, s: str) -> str:
        letter_counter = defaultdict(int)
        l = len(s)

        for letter in s:
            letter_counter[letter] += 1

        



print(Solution().reorganizeString(s="aaab"))