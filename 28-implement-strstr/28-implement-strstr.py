class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        if needle == "":
            return 0
        
        for i in range(0, len(haystack)+1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1
        