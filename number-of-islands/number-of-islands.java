class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[i].length; j++){
                if(grid[i][j] == '1'){
                    count++;
                    SearchOthers(grid, i, j);
                }
            }
        }
        return count;
        
    }
    
    public void SearchOthers(char[][] grid, int i, int j){
        if(i < 0 || grid.length <= i || j < 0 || grid[i].length <= j || grid[i][j] == '0'){
            return;
        }
        else{
            grid[i][j] = '0';
        }
        
        SearchOthers(grid, i, j-1);
        SearchOthers(grid, i, j+1);
        SearchOthers(grid, i-1, j);
        SearchOthers(grid, i+1, j);
    }
    
}