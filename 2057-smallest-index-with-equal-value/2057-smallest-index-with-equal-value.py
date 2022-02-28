class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        lowest = 10000000
        for i, num in enumerate(nums):
            if i % 10 == num:
                lowest = min(lowest, i)
        if lowest == 10000000:
            return -1
        return lowest
        