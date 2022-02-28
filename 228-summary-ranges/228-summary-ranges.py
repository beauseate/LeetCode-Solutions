class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res = []
        i = 0
        start = 0
        if not nums:
            return []
        
        while i < len(nums)-1:
            if nums[i] + 1 != nums[i+1]:
                res.append(self.printRange(nums[start], nums[i]))
                start = i+1
            i += 1
        res.append(self.printRange(nums[start], nums[i]))
            
            
            
        return res
    
    def printRange(self, v1, v2):
        if v1 == v2:
            return str(v1)
        else:
            return str(v1) + "->" + str(v2)
            