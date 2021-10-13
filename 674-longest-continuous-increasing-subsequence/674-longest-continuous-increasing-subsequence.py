class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        curMax = 1
        allMax = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curMax += 1
            else:
                curMax = 1
            allMax = max(allMax, curMax)
        return allMax
        