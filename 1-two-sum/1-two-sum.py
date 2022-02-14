class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsDict = {}
        
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in numsDict:
                return {i, numsDict.get(difference)}
            numsDict[nums[i]] = i
        return {-1, -1}
            