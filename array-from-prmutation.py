class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n=[]
        for i in range(len(nums)):
            a=nums[i]
            n.append(nums[a])
        return n
        
