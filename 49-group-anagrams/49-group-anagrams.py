class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        
        
        for s in strs:
            charList = [0] * 26
            for c in s:
                charList[ord(c) - ord("a")] += 1
            d[tuple(charList)].append(s)
        
        return d.values()
        