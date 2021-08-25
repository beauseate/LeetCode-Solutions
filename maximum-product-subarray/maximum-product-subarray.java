class Solution {
    public int maxProduct(int[] nums) {
        
        int currMax = nums[0];
        int max = nums[0];
        int min = nums[0];
        
        for(int i = 1; i < nums.length; i++){
            int temp = currMax;
            currMax = Math.max(Math.max(currMax * nums[i], min * nums[i]), nums[i]);
            min = Math.min(Math.min(temp * nums[i], min * nums[i]), nums[i]);
            max = Math.max(max, currMax);
        }
        
        return max;
        
    }
}