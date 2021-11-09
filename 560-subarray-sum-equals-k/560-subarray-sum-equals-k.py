class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0 
        sum = 0
        sumMap = {}
        sumMap[0] = 1
        
        for i, e in enumerate(nums):
            sum += e
            if sum - k in sumMap:
                count += sumMap.get(sum-k)
            sumMap[sum] = sumMap.setdefault(sum, 0) + 1
        
        return count
        
                
        