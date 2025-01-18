package Graph;

import java.util.Arrays;
import java.util.PriorityQueue;

public class MinimumCostForOneValidGridPath {

    int[][] directions = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int minCost(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int[][] result = new int[m][n];
        for(int[] row: result) Arrays.fill(row, Integer.MAX_VALUE);

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            for(int x = 0; x < 3; x++) {
                if(a[x] != b[x]) {
                    return Integer.compare(a[x], b[x]);
                }
            }

            return Integer.compare(a[0], b[0]);
        });

        pq.offer(new int[]{0, 0, 0});
        result[0][0] = 0;

        while(!pq.isEmpty()) {
            int[] current = pq.poll();

            int cost = current[0];
            int i = current[1];
            int j = current[2];

            if(result[i][j] < cost) {
                continue;
            }

            for(int l = 0; l < 4; l++) {
                int i_ = i + directions[l][0];
                int j_ = j + directions[l][1];

                if(i_ >= 0 && j_ >= 0 && i_ < m && j_ < n) {
                    int newCost = cost + (grid[i][j] - 1 != l ? 1 : 0);
                    if(newCost < result[i_][j_]) {
                        result[i_][j_] = newCost;
                        pq.offer(new int[]{newCost, i_, j_});
                    }
                }
            }
        }

        return result[m - 1][n - 1];
    }

    public static void main(String[] args) {
        MinimumCostForOneValidGridPath obj = new MinimumCostForOneValidGridPath();
        System.out.println(obj.minCost(new int[][] {{1,1,1,1},{2,2,2,2},{1,1,1,1},{2,2,2,2}}));
        System.out.println(obj.minCost(new int[][] {{1,1,3},{3,2,2},{1,1,4}}));
    }
}