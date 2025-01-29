import java.util.Queue;
import java.util.LinkedList;

public class MaximumNumberOfFishInGrid {
    int[] parent;
    int[][] directions = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };
    int[] fishes;
    int m, n;

    public int findMaxFish(int[][] grid) {
        Queue<int[]> fishCells = new LinkedList<>();
        int m = grid.length;
        int n = grid[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0)
                    fishCells.offer(new int[] { i, j });
            }
        }

        int maxFish = 0;
        while (!fishCells.isEmpty()) {
            int[] startingPoint = fishCells.poll();
            int fishes = bfs(grid, startingPoint);
            maxFish = Math.max(maxFish, fishes);
        }

        return maxFish;
    }

    private int bfs(int[][] grid, int[] startingPoint) {
        int m = grid.length, n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> queue = new LinkedList<>();
        int fishes = 0;
        queue.offer(startingPoint);
        visited[startingPoint[0]][startingPoint[1]] = true;
        while (!queue.isEmpty()) {
            int[] point = queue.poll();
            fishes += grid[point[0]][point[1]];

            for (int[] direction : directions) {
                int i_ = point[0] + direction[0];
                int j_ = point[1] + direction[1];

                if (i_ >= 0 && i_ < m && j_ >= 0 && j_ < n && grid[i_][j_] > 0 && !visited[i_][j_]) {
                    visited[i_][j_] = true;
                    queue.offer(new int[] { i_, j_ });
                }
            }
        }

        return fishes;
    }

    public int findMaxFishUsingDSU(int[][] grid) {
        m = grid.length;
        n = grid[0].length;
        parent = new int[m * n];
        fishes = new int[m * n];
        for (int i = 0; i < m * n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) {
                    fishes[i * n + j] = grid[i][j];
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) {
                    for (int[] direction : directions) {
                        int i_ = i + direction[0];
                        int j_ = j + direction[1];

                        if (i_ >= 0 && i_ < m && j_ >= 0 && j_ < n && grid[i_][j_] > 0) {
                            union(i * n + j, i_ * n + j_);
                        }
                    }
                }
            }
        }

        int maxFishes = 0;
        for (int i = 0; i < m * n; i++) {
            if (parent[i] == i) {
                maxFishes = Math.max(maxFishes, fishes[i]);
            }
        }

        return maxFishes;
    }

    private void union(int x, int y) {

        int xParent = findParent(x);
        int yParent = findParent(y);

        if (xParent == yParent)
            return;

        if (fishes[yParent] > fishes[xParent]) {
            parent[xParent] = yParent;
            fishes[yParent] += fishes[xParent];
        } else {
            parent[yParent] = xParent;
            fishes[xParent] += fishes[yParent];
        }
    }

    private int findParent(int node) {
        if (parent[node] != node) {
            parent[node] = findParent(parent[node]);
        }

        return parent[node];
    }

    public static void main(String[] args) {
        MaximumNumberOfFishInGrid maxFish = new MaximumNumberOfFishInGrid();

        System.out.println(
                maxFish.findMaxFish(
                        new int[][] {
                                { 0, 2, 1, 0 },
                                { 4, 0, 0, 3 },
                                { 1, 0, 0, 4 },
                                { 0, 3, 2, 0 }
                        }));

        System.out.println(
                maxFish.findMaxFish(
                        new int[][] {
                                { 1, 0, 0, 0 },
                                { 0, 0, 0, 0 },
                                { 0, 0, 0, 0 },
                                { 0, 0, 0, 1 }
                        }));

        System.out.println(
                maxFish.findMaxFishUsingDSU(
                        new int[][] {
                                { 0, 2, 1, 0 },
                                { 4, 0, 0, 3 },
                                { 1, 0, 0, 4 },
                                { 0, 3, 2, 0 }
                        }));

        System.out.println(
                maxFish.findMaxFishUsingDSU(
                        new int[][] {
                                { 1, 0, 0, 0 },
                                { 0, 0, 0, 0 },
                                { 0, 0, 0, 0 },
                                { 0, 0, 0, 1 }
                        }));
    }
}
