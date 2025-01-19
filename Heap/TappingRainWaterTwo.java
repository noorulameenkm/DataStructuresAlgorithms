package Heap;

import java.util.Comparator;
import java.util.PriorityQueue;

public class TappingRainWaterTwo {

    public int trapRainWater(int[][] heightMap) {
        int m = heightMap.length;
        int n = heightMap[0].length;

        boolean[][] visited = new boolean[m][n];

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        for(int row = 0; row < m; row++) {
            pq.offer(new int[]{heightMap[row][0], row, 0});
            visited[row][0] = true;

            pq.offer(new int[]{heightMap[row][n - 1], row, n - 1});
            visited[row][n - 1] = true;
        }

        for(int col = 0; col < n; col++) {
            pq.offer(new int[]{heightMap[0][col], 0, col});
            visited[0][col] = true;

            pq.offer(new int[]{heightMap[m - 1][col], m - 1, col});
            visited[m - 1][col] = true;
        }

        int water = 0;
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while(!pq.isEmpty()) {
            int[] cell = pq.poll();
            int height = cell[0];
            int i = cell[1];
            int j = cell[2];

            for(int[] direction : directions) {
                int neighbourRow = i + direction[0];
                int neighbourCol = j + direction[1];

                if(neighbourRow >= 0 && neighbourRow < m && neighbourCol >= 0 && neighbourCol < n && 
                !visited[neighbourRow][neighbourCol]) {
                    water += Math.max(height - heightMap[neighbourRow][neighbourCol], 0);
                    pq.offer(new int[]{Math.max(height, heightMap[neighbourRow][neighbourCol]), neighbourRow, neighbourCol});
                    visited[neighbourRow][neighbourCol] = true;
                }
            }
        }

        return water;
    }

    public static void main(String[] args) {
        TappingRainWaterTwo obj = new TappingRainWaterTwo();
        System.out.println(
            obj.trapRainWater(new int[][]{{1,4,3,1,3,2},{3,2,1,3,2,4},{2,3,3,2,3,1}})
        );

        System.out.println(
            obj.trapRainWater(new int[][]{{3,3,3,3,3},{3,2,2,2,3},{3,2,1,2,3},{3,2,2,2,3},{3,3,3,3,3}})
        );
    }
    
}
