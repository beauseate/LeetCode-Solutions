class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        total = 0
        min_val = 0
        for i in nums:
            total += i
            min_val = min(min_val, total)
            
        return -min_val + 1
            
        