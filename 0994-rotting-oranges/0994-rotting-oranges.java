class Solution {
    public int orangesRotting(int[][] grid) {

        int n = grid.length;
        int m = grid[0].length;

        Queue<int[]> queue = new LinkedList<>();

        // Step 1: Add all initially rotten oranges
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 2) {
                    queue.add(new int[]{i, j});
                }
            }
        }

        int time = 0;

        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, 1, -1};

        // Step 2: BFS
        while (!queue.isEmpty()) {

            int size = queue.size();
            boolean rotten = false;

            for (int i = 0; i < size; i++) {

                int current[] = queue.poll();

                int r = current[0];
                int c = current[1];

                // Check 4 directions
                for (int d = 0; d < 4; d++) {

                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr >= 0 && nr < n &&
                        nc >= 0 && nc < m &&
                        grid[nr][nc] == 1) {

                        grid[nr][nc] = 2;
                        queue.add(new int[]{nr, nc});

                        rotten = true;
                    }
                }
            }

            // One minute passed only if at least
            // one fresh orange became rotten
            if (rotten) {
                time++;
            }
        }

        // Step 3: Check for remaining fresh oranges
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {

                if (grid[i][j] == 1) {
                    return -1;
                }
            }
        }

        return time;
    }
}