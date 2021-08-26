class Solution {
    public int maxArea(int[] height) {
        
        int low = 0;
        int high = height.length-1;
        int water = 0;
        
        while(low < high){
            water = Math.max(water, Math.min(height[low] * (high-low), height[high]*(high-low)));
            if(height[low] <= height[high]){
                low++;
            }
            else{
                high--;
            }
        }
        
        return water;
        
    }
}