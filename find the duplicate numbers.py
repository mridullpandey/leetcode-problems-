from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        for n in nums:
            dict[n] += 1
            if dict[n] > 1: return n
