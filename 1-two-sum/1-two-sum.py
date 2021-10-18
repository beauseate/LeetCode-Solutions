class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        
        for i, num in enumerate(nums):
            difference = target - num
            
            if difference in d:
                return {i, d.get(difference)}
            d[num] = i
        return {0, 0}
        