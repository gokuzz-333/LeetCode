class Solution {
    public int numEnclaves(int[][] grid) {
        int n=grid.length;
        int m=grid[0].length;
        Queue<int[]> queue=new LinkedList<>();
        for(int i=0;i<n;i++){
            if(grid[i][0]==1){
                grid[i][0]=0;
                queue.add(new int[]{i,0});
            }
            if(grid[i][m-1]==1){
                grid[i][m-1]=0;
                queue.add(new int[]{i,m-1});
            }
        }
        for(int j=0;j<m;j++){
            if(grid[0][j]==1){
                grid[0][j]=0;
                queue.add(new int[]{0,j});
            }
            if(grid[n-1][j]==1){
                grid[n-1][j]=0;
                queue.add(new int[]{n-1,j});
            }
        }
        int dr[]={-1,1,0,0};
        int dc[]={0,0,-1,1};
        while(!queue.isEmpty()){
            int current[]=queue.poll();
            int r=current[0];
            int c=current[1];
            for(int d=0;d<4;d++){
                int nr=r+dr[d];
                int nc=c+dc[d];
                if(nr>=0&&nr<n&&nc>=0&&nc<m&&grid[nr][nc]==1){
                    grid[nr][nc]=0;
                    queue.add(new int[]{nr,nc});
                }
            }
        }
        int count=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1){
                    count+=1;
                }
            }
        }
        return count;
    }
}