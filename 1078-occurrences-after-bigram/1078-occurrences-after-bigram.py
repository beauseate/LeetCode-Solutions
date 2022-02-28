class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        res, i = [], 0
        text = text.split()
        
        while i < len(text)-1:
            if text[i] == first and text[i+1] == second:
                if i + 2 > len(text)-1:
                    break;
                else:
                    res.append(text[i+2])
            i += 1
                
        return res
            