

public class MinimumAreaToCoverAllOnesTwo {

    private int minimumArea(int[][] grid, int startRow, int endRow, int startCol, int endCol) {
        int m = grid.length;
        int n = grid[0].length;
        int minRow = m, maxRow = -1, minCol = n, maxCol = -1;
        for(int i = startRow; i < endRow; i++) {
            for(int j = startCol; j < endCol; j++) {
                if(grid[i][j] == 1) {
                    minRow = Math.min(minRow, i);
                    maxRow = Math.max(maxRow, i);
                    minCol = Math.min(minCol, j);
                    maxCol = Math.max(maxCol, j);
                }
            }
        }

        if(maxRow == -1) return 0;
        return (maxRow - minRow + 1) * (maxCol - minCol + 1);
    }   

    private int minimum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int result = Integer.MAX_VALUE;
        for(int rowSplit = 1; rowSplit < m; rowSplit++) {
            for(int colSplit = 1; colSplit < n; colSplit++) {
                int top = minimumArea(grid, 0, rowSplit, 0, n);
                int bottomLeft = minimumArea(grid, rowSplit, m, 0, colSplit);
                int bottomRight = minimumArea(grid, rowSplit, m, colSplit, n);

                result = Math.min(result, top + bottomLeft + bottomRight);

                int bottom = minimumArea(grid, rowSplit, m, 0, n);
                int topLeft = minimumArea(grid, 0, rowSplit, 0, colSplit);
                int topRight = minimumArea(grid, 0, rowSplit, colSplit, n);

                result = Math.min(result, bottom + topLeft + topRight);
            }
        }

        for(int split1 = 1; split1 < m - 1; split1++) {
            for(int split2 = split1 + 1; split2 < m; split2++) {
                int top = minimumArea(grid, 0, split1, 0, n);
                int middle = minimumArea(grid, split1, split2, 0, n);
                int bottom = minimumArea(grid, split2, m, 0, n);
                result = Math.min(result, top + middle + bottom);
            }
        }

        return result;
    }

    public int minimumSum(int[][] grid) {
        int result = minimum(grid);

        int[][] rotated = rotate(grid);

        result = Math.min(result, minimum(rotated));
        return result;
    }

    private int[][] rotate(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] rotated = new int[n][m];
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                rotated[j][m - i - 1] = grid[i][j];
            }
        }

        return rotated;
    }

    public static void main(String[] args) {
        MinimumAreaToCoverAllOnesTwo soln = new MinimumAreaToCoverAllOnesTwo();
        int[][] grid = new int[][]{{1, 0, 1}, {1, 1, 1}};
        System.out.println(soln.minimumSum(grid));
    }
    
}