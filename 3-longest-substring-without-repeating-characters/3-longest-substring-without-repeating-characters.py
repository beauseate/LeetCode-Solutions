class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        left = 0
        longest = 0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[left])
                left += 1
            longest = max(longest, i - left + 1)
            charSet.add(s[i])
        return longest
        