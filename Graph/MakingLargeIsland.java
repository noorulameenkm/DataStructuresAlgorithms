package Graph;

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

public class MakingLargeIsland {
    int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int largestIsland(int[][] grid) {
        int n = grid.length;
        boolean[][] visited = new boolean[n][n];
        Map<Integer, Integer> cache = new HashMap<>();
        int maxArea = 0;
        int uniqueID = 2;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1 && !visited[i][j]) {
                    int area = bfs(i, j, grid, visited, uniqueID);
                    cache.put(uniqueID, area);
                    uniqueID++;
                }
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 0) {
                    Set<Integer> set = new HashSet<>();
                    int area = 1;
                    for(int[] direction: directions) {
                        int i_ = i + direction[0];
                        int j_ = j + direction[1];
                        if(i_ >= 0 && i_ < n && j_ >= 0 && j_ < n && grid[i_][j_] > 1 && !set.contains(grid[i_][j_])) {
                            int id = grid[i_][j_];
                            area += cache.get(grid[i_][j_]);
                            set.add(id);
                        }
                    }

                    maxArea = Math.max(area, maxArea);
                }
            }
        }

        if(maxArea == 0) maxArea = n * n;

        return maxArea;
    }

    private int bfs(int i, int j, int[][] grid, boolean[][] visited, int uniqueID) {
        int n = grid.length;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{i, j});
        
        visited[i][j] = true;
        int area = 0;

        while(!queue.isEmpty()) {
            int[] indices = queue.poll();
            area++;
            grid[indices[0]][indices[1]] = uniqueID;
            for(int[] direction: directions) {
                int i_ = indices[0] + direction[0];
                int j_ = indices[1] + direction[1];

                if(i_ >= 0 && i_ < n && j_ >= 0 && j_ < n && grid[i_][j_] == 1 && !visited[i_][j_]) {
                    queue.offer(new int[]{i_, j_});
                    visited[i_][j_] = true;
                }
            }
        }

        return area;
    }

    public static void main(String[] args) {
        MakingLargeIsland solution = new MakingLargeIsland();

        System.out.println(
            solution.largestIsland(
                new int[][]{
                    {1, 0},
                    {0, 1}
                }
            )
        );

        System.out.println(
            solution.largestIsland(
                new int[][]{
                    {1, 1},
                    {1, 0}
                }
            )
        );

        System.out.println(
            solution.largestIsland(
                new int[][]{
                    {1, 1},
                    {1, 1}
                }
            )
        );
    }
}
