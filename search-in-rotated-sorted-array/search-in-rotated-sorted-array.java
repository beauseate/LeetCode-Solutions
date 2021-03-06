class Solution {
    public int search(int[] nums, int target) {
        
        int low = 0;
        int high = nums.length-1;
        while(low <= high){
            if(nums[low] == target){
                return low;
            }
            if(nums[high] == target){
                return high;
            }
            low++;
            high--;
        }
        
        return -1;
            
        
    }
}