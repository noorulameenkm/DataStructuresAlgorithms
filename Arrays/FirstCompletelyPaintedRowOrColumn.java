import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class FirstCompletelyPaintedRowOrColumn {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int length = arr.length;

        int m = mat.length;
        int n = mat[0].length;

        int[] rows = new int[m];
        int[] cols = new int[n];

        Arrays.fill(rows, 0);
        Arrays.fill(cols, 0);
        Map<Integer, int[]> location = new HashMap<>();

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                location.put(mat[i][j], new int[]{i, j});
            }
        }

        for(int i = 0; i < length; i++) {
            int number = arr[i];
            int[] rowCol = location.get(number);
            rows[rowCol[0]]++;
            cols[rowCol[1]]++;

            if(rows[rowCol[0]] == n || cols[rowCol[1]] == m) return i;
        }

        return -1;
    }

    public int firstCompleteIndex2(int[] arr, int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;

        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < m * n; i++) {
            map.put(arr[i], i);
        }

        int minIndex = Integer.MAX_VALUE;

        for(int row = 0; row < m; row++) {
            int maxIndex = Integer.MIN_VALUE;
            for(int col = 0; col < n; col++) {
                int number = mat[row][col];
                int index = map.get(number);
                maxIndex = Math.max(maxIndex, index);
            }

            minIndex = Math.min(minIndex, maxIndex);
        }

        for(int col = 0; col < n; col++) {
            int maxIndex = Integer.MIN_VALUE;
            for(int row = 0; row < m; row++) {
                int number = mat[row][col];
                int index = map.get(number);
                maxIndex = Math.max(maxIndex, index);
            }

            minIndex = Math.min(minIndex, maxIndex);
        }

        return minIndex;
    }

    public static void main(String[] args) {
        FirstCompletelyPaintedRowOrColumn firstCompletelyPaintedRowOrColumn = new FirstCompletelyPaintedRowOrColumn();
        System.out.println(
            firstCompletelyPaintedRowOrColumn.firstCompleteIndex(
                new int[]{1,3,4,2},
                new int[][]{
                    {1,4},
                    {2,3},
                }
            )
        );

        System.out.println(
            firstCompletelyPaintedRowOrColumn.firstCompleteIndex(
                new int[]{2,8,7,4,1,3,5,6,9},
                new int[][]{
                    {3,2,5},
                    {1,4,6},
                    {8,7,9}
                }
            )
        );

        System.out.println(
            firstCompletelyPaintedRowOrColumn.firstCompleteIndex2(
                new int[]{1,3,4,2},
                new int[][]{
                    {1,4},
                    {2,3},
                }
            )
        );

        System.out.println(
            firstCompletelyPaintedRowOrColumn.firstCompleteIndex2(
                new int[]{2,8,7,4,1,3,5,6,9},
                new int[][]{
                    {3,2,5},
                    {1,4,6},
                    {8,7,9}
                }
            )
        );
    }
}
