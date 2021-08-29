class Solution {
    public int findKthLargest(int[] nums, int k) {
        int ans = 0;
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        
        for(int i = 0; i < nums.length; i++){
            
            maxHeap.add(-nums[i]);
        }
        
        while(k >= 1){
            ans = maxHeap.poll();
            k--;
        }
        
        return -ans;
    }
}