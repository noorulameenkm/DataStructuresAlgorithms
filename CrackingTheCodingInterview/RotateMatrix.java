import java.util.Arrays;

public class RotateMatrix {
    public static void main(String[] args) {
        RotateMatrix rm = new RotateMatrix();
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        printMatrix(rm.rotateMatrix(matrix, 3));
        System.out.println();
        rm.inPlaceRotateMatrix(matrix);
        printMatrix(matrix);
    }

    private int[][] rotateMatrix(int[][] matrix, int n) {
        int[][] result = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[j][n - 1 - i] = matrix[i][j];
            }
        }

        return result;
    }

    private void inPlaceRotateMatrix(int[][] matrix) {
        int n = matrix.length;
        for(int layer = 0; layer < n / 2; layer++) {
            int last = n - 1 - layer;
            for (int i = layer; i < last; i++) {
                int offset = i - layer;
                int top = matrix[layer][i];
                // left -> top
                matrix[layer][i] = matrix[last - offset][layer];
                // bottom -> left
                matrix[last - offset][layer] = matrix[last][last - offset];
                // right -> bottom
                matrix[last][last - offset] = matrix[i][last];
                // top -> right
                matrix[i][last] = top;
            }
        }
    }

    static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            System.out.println(Arrays.toString(matrix[i]));
        }
    }
}
