class Solution {
    public boolean isPalindrome(String s) {
        
        String actual = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        int start = 0;
        int end = actual.length()-1;
        
        while(start < end){
            if(actual.charAt(start) != actual.charAt(end)){
                return false;
            }
            
            start++;
            end--;
        }
        
        return true;
    }
}