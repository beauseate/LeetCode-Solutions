class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsCounter = collections.Counter(chars)
        sum = 0
        for word in words:
            wordCounter = collections.Counter(word)
            for c in wordCounter:
                if wordCounter[c] > charsCounter[c]:
                    break
            else:
                sum += len(word)
        return sum
                    
        