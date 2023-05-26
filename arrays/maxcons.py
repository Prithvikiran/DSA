class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        d=0
        for i in range(len(nums)):
            if (nums[i]==1):
                c=c+1
                if(d<c):
                 d=c
            else:
                c=0
        return d