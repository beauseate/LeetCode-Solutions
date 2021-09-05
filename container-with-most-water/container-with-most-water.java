class Solution {
    public int maxArea(int[] height) {
        
        int start = 0;
        int end = height.length-1;
        int maxCur = Integer.MIN_VALUE;
        int maxAll = Integer.MIN_VALUE;
        
        while(start < end){
            maxCur = Math.max(maxCur, Math.min(height[start], height[end]) * (end-start));
            maxAll = Math.max(maxCur, maxAll);
            
            if(height[start] > height[end]){
                end--;
            }
            else{
                start++;
            }
            
        }
        
        return maxAll;
        
    }
}