class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        final = [1] * (len(nums))
        prefix = 1
        for i, v in enumerate(nums):
            final[i] = prefix
            prefix = prefix * v
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            final[i] *= postfix
            postfix *= nums[i]
            
        return final
            