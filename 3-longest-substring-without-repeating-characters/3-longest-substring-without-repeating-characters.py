class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashmap = {} # char, int
        start = maxLen = 0
        for i, n in enumerate(s):
            if n in hashmap and start <= hashmap[n]:
                start = hashmap[n] + 1
            else:
                maxLen = max(maxLen, i - start + 1)
            hashmap[n] = i
                
        return maxLen
            