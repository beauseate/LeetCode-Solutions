class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = 1000000
        maxSell = 0
        for num in prices:
            minPrice = min(minPrice, num)
            maxSell = max(maxSell, num-minPrice)
        return maxSell
        