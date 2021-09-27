class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo = 0
        high = len(nums) - 1
        
        while(lo <= high):
            mid = (lo + high) // 2
            
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if target >= nums[mid] or target < nums[lo]:
                    lo = mid + 1
                else:
                    high = mid - 1
            else:
                if target <= nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    lo = mid + 1
        return -1
        