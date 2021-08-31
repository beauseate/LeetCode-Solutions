class Solution {
    public int findMin(int[] nums) {
        
        int min = Integer.MAX_VALUE;
        
        int start = 0;
        int end = nums.length-1;
        
        while(start <= end){
            
            min = Math.min(min, Math.min(nums[start], nums[end]));
            start++;
            end--;
        }
        
        return min;
        
    }
}