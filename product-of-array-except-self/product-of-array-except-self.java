class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        
        int leftProduct = 1;
        int rightProduct = 1;
        int[] res = new int[nums.length];
        for(int i = 1; i < nums.length+1; i++){
            res[i-1] = leftProduct;
            leftProduct *= nums[i-1];
        }
        for(int i = nums.length-1; i > -1; i--){
            res[i] *= rightProduct;
            rightProduct *= nums[i];
        }
            
            
        
        return res;
    }
}