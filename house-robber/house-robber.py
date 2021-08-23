class Solution:
    def rob(self, nums: List[int]) -> int:
        
        first = 0
        second = 0
        maxRob = 0
        
        for i in nums:
            maxRob = max(first + i, second)
            first = second
            second = maxRob
            
        return maxRob
        