class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        o=[1]*len(nums)
        m1,m2=1,1
        for i in range(len(nums)):
            j=-1-i
            o[i]*=m1
            o[j]*=m2
            m1*=nums[i]
            m2*=nums[j]
        return o
