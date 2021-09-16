class Solution:
    def climbStairs(self, n: int) -> int:
        
        if(n == 1):
            return 1
        
        one = 1
        two = 1
        
        for i in range(2, n):
            temp = one
            one = two + one
            two = temp
        return one + two
        
        
        