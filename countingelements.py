class Solution:
    def countElements(self, arr: List[int]) -> int:
        x=set([num-1 for num in arr])
        cnt=[num in x for num in arr]
        return sum(cnt)
