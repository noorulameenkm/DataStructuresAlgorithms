package Graph;

public class CycleInMatrix {
    public boolean hasCycle(char[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean[][] visited = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    if (cycleExists(matrix, visited, i, j, matrix[i][j], -1, -1))
                        return true;
                }
            }
        }
        return false;
    }

    private boolean cycleExists(char[][] matrix, boolean[][] visited, int x, int y, char startingChar, int prevX,
            int prevY) {
        if (x < 0 || y < 0 || x >= matrix.length || y >= matrix[0].length)
            return false;

        if (matrix[x][y] != startingChar)
            return false;

        if (visited[x][y])
            return true;

        visited[x][y] = true;

        if (x + 1 != prevX && cycleExists(matrix, visited, x + 1, y, startingChar, x, y))
            return true;
        if (x - 1 != prevX && cycleExists(matrix, visited, x - 1, y, startingChar, x, y))
            return true;
        if (y + 1 != prevY && cycleExists(matrix, visited, x, y + 1, startingChar, x, y))
            return true;
        if (y - 1 != prevY && cycleExists(matrix, visited, x, y - 1, startingChar, x, y))
            return true;

        return false;
    }

    public static void main(String[] args) {
    CycleInMatrix sol = new CycleInMatrix();
        System.out.println(sol.hasCycle(
        new char[][] {
            { 'a', 'a', 'a', 'a' },
            { 'b', 'a', 'c', 'a' },
            { 'b', 'a', 'c', 'a' },
            { 'b', 'a', 'a', 'a' }
        }));

    System.out.println(sol.hasCycle(
        new char[][] {
            { 'a', 'a', 'a', 'a' },
            { 'a', 'b', 'b', 'a' },
            { 'a', 'b', 'a', 'a' },
            { 'a', 'a', 'a', 'c' }
        }));

    System.out.println(sol.hasCycle(
        new char[][] {
            { 'a', 'b', 'e', 'b' },
            { 'b', 'b', 'b', 'b' },
            { 'b', 'c', 'c', 'd' },
            { 'c', 'c', 'd', 'd' }
        }));
    }
}
