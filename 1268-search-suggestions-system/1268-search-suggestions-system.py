class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        returnedList = []
        
        
        for i in range(0, len(searchWord)):
            newList = []
            for j in range(0, len(products)):
                if len(newList) >= 3:
                    break
                    
                if searchWord[0:i+1] == products[j][0:i+1]:
                    newList.append(products[j])
            returnedList.append(newList)
                    
        return returnedList
        
        
        
        
        
            
        