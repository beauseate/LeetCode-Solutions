class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numDict = {}
        
        for i, num in enumerate(nums):
            difference = target - num
            
            if difference in numDict:
                return{i, numDict.get(difference)}
            numDict[num] = i
        
        return{0, 0}
        