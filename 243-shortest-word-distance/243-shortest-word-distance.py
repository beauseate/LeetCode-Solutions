class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = inf
        index2 = inf
        shortestD = inf
        for i, w in enumerate(wordsDict):
            if w == word1:
                index1 = i
            if w == word2:
                index2 = i
            if index1 < inf and index2 < inf:
                shortestD = min(shortestD, abs(index1 - index2))
        return shortestD
            
        