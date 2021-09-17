class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        currMax = nums[0]
        minMax = nums[0]
        allMax = nums[0]
        
        for i in range(1, len(nums)):
            temp = currMax
            currMax = max(max(minMax * nums[i], currMax * nums[i]), nums[i])
            minMax = min(min(minMax * nums[i], temp * nums[i]), nums[i])
            allMax = max(allMax, currMax)
        
        return allMax
        