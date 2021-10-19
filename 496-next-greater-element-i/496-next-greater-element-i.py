class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        res = [-1] * len(nums1)
        
        for n, num1 in enumerate(nums1):
            
            for j in range(0, len(nums2)-1):
                if nums2[j] == num1:
                    k = j
                    while k < len(nums2)-1:
                        if nums2[j] < nums2[k+1]:
                            res[n] = nums2[k+1]
                            break
                        k += 1
                        
        return res
        