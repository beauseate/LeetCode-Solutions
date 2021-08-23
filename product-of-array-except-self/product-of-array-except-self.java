class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        
        int leftProduct = 1;
        int rightProduct = 1;
        int[] res = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            res[i] = leftProduct;
            leftProduct *= nums[i];
        }
        for(int i = nums.length-1; i > -1; i--){
            res[i] *= rightProduct;
            rightProduct *= nums[i];
        }
            
            
        
        return res;
    }
}
