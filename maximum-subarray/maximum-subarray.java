class Solution {
    public int maxSubArray(int[] nums) {
        int sumSoFar = nums[0];
        int maxSum = nums[0];
        
        for(int i = 1; i < nums.length; i++){
            sumSoFar = Math.max(sumSoFar + nums[i], nums[i]);
            maxSum = Math.max(maxSum, sumSoFar);
        }
        
        return maxSum;
    }
}