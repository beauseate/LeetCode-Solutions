class Solution {
    public int maxArea(int[] height) {
        
        int lower = 0;
        int higher = height.length-1;
        int currMax = Integer.MIN_VALUE;
        int overallMax = Integer.MIN_VALUE;
        while(lower < higher){
            currMax = Math.max(currMax, Math.min(height[lower], height[higher]) * (higher-lower));
            overallMax = Math.max(overallMax, currMax);
            if(height[higher] > height[lower]){
                lower++;
            } else{
                higher--;
            }
            
        }
        return overallMax;
        
    }
}