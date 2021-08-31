class Solution {
    public int searchInsert(int[] nums, int target) {
        
        int start = 0;
        int end = nums.length;
        
        while(start < end){
            if(nums[start] < target){
                start++;
            }
            else if (nums[end-1] >= target){
                end--;
            }
        }
        
        return start;
    }
}