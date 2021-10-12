class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        d = dict()
        
        for i, value in enumerate(nums):
            difference = target - value
            if difference in d:
                return {i, d.get(difference)}
            d[value] = i
        return {0, 0}
        