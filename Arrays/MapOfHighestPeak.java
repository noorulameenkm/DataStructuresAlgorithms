import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class MapOfHighestPeak {
    public int[][] highestPeak(int[][] isWater) {
        int m = isWater.length;
        int n = isWater[0].length;
        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[m][n];
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(isWater[i][j] == 1) {
                    isWater[i][j] = 0;
                    queue.offer(new int[]{i, j});
                    visited[i][j] = true;
                }
            }
        }

        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while(!queue.isEmpty()) {
            int[] indices = queue.poll();
            int i = indices[0];
            int j = indices[1];
            for(int[] direction : directions) {
                int i_ = i + direction[0];
                int j_ = j + direction[1];
                if(i_ >= 0 && i_ < m && j_ >= 0 && j_ < n && !visited[i_][j_]) {
                    isWater[i_][j_] = isWater[i][j] + 1;
                    visited[i_][j_] = true;
                    queue.offer(new int[]{i_, j_});
                }
            }
        }

        return isWater;
    }

    public static void main(String[] args) {
        MapOfHighestPeak mapOfHighestPeak = new MapOfHighestPeak();

        System.out.println(
            Arrays.deepToString(
                mapOfHighestPeak.highestPeak(
                new int[][] {
                    {0, 1},
                    {0, 0}
                }
            )
            )
        );

        System.out.println(
            Arrays.deepToString(
                mapOfHighestPeak.highestPeak(
                    new int[][] {
                        {0, 0, 1},
                        {1, 0, 0},
                        {0, 0, 0}
                    }
                )
            )
        );
    }
}
