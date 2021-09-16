class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        
        for index, num in enumerate(nums):
            difference = target - num
            if difference in hmap:
                return [index, hmap[difference]]
            hmap[num] = index
        return [-1, -1]
        