class Solution {
    public int maxSubArray(int[] nums) {
        
        int currMax = nums[0];
        int overallMax = nums[0];
        
        for(int i = 1; i < nums.length; i++){
            
            currMax = Math.max(currMax + nums[i], nums[i]);
            overallMax = Math.max(overallMax, currMax);
        }
        
        return overallMax;
        
    }
}