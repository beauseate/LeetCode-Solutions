class Solution {
    public int findMin(int[] nums) {
        
        
        int min = nums[(nums.length-1)/2];
        int i = 0;
        int j = nums.length - 1;
        
        while(i < j){
            if(nums[i] < min){
                min = Math.min(nums[i], min);
                i++;
            }
            else{
                min = Math.min(nums[j], min);
                j--;
            }
        }
        
        return min;
    }
}