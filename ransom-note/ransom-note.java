class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        
        HashMap<Character, Integer> note = new HashMap<>();
        HashMap<Character, Integer> mag = new HashMap<>();
        
        for(int i = 0; i < magazine.length(); i++){
            mag.put(magazine.charAt(i), mag.getOrDefault(magazine.charAt(i), 0) + 1);
        }
        
        for(int i = 0; i < ransomNote.length(); i++){
            note.put(ransomNote.charAt(i), note.getOrDefault(ransomNote.charAt(i), 0) + 1);
            if(note.getOrDefault(ransomNote.charAt(i), 0) > mag.getOrDefault(ransomNote.charAt(i), 0)){
                return false;
            }
        }
        return true;
        
    }
}