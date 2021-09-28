class Solution:
    def frequencySort(self, s: str) -> str:
        
        chars = {}
        newString = ''
        for i in range(len(s)):
            chars.setdefault(s[i], 0)
            chars[s[i]] += 1
        while chars:
            maxLen = max(chars.values())
            c = max(chars, key=chars.get)
            while maxLen != 0:
                newString += c
                maxLen -= 1
            chars.pop(c)
        return newString