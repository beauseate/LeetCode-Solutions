class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        Arrays.sort(nums);
        List<List<Integer>> arrList = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        
        
        for(int i = 0; i < nums.length; i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int start = i+1;
            int end = nums.length-1;
            while(start < end){
            int threeSum = nums[i] + nums[start] + nums[end];
            if(threeSum > 0){
                end--;
            }
            else if(threeSum < 0){
                start++;
            }
            else{
                list.add(nums[start]);
                list.add(nums[i]);
                list.add(nums[end]);
                arrList.add(new ArrayList(list));
                list.clear();
                start++;
                while(nums[start] == nums[start-1] && start < end){
                    start++;
                }
                }
            
        }
        }
        
        return arrList;
    }
}