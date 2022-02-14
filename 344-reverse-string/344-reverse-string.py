class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        high = len(s)-1
        low = 0
        
        while low < high:
            temp = s[low]
            s[low] = s[high]
            s[high] = temp
            low += 1
            high -= 1
        