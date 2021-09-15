class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        low = 0
        high = len(nums)-1
        
        while(low < high):
            res = nums[low] + nums[high]
            if(res == target):
                return [low+1, high+1]
            
            if(res > target):
                high -= 1
            else:
                low += 1
                
        return [0, 0]