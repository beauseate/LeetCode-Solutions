class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        arr = [0] * len(nums)
        evenP = 0
        oddP = 1
        numP = 0
        
        while numP < len(nums):
            if nums[numP] % 2 == 0:
                arr[evenP] = nums[numP]
                evenP += 2
                numP += 1
            else:
                arr[oddP] = nums[numP]
                oddP += 2
                numP += 1
        return arr