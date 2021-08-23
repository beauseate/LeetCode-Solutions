class Solution {
    public int rob(int[] nums) {
        
        int  firstRob = 0;
        int secondRob = 0;
        int max = 0;
        for(int pointer: nums){
            max = Math.max(firstRob + pointer, secondRob);
            firstRob = secondRob;
            secondRob = max;
        }
        return secondRob;
        
    }
}