package Graph;

import java.util.HashSet;
import java.util.Set;

public class NumberOfUniqueIslands {
    public int findDistinctIslandsDFS(int[][] matrix) {
    int m = matrix.length, n = matrix[0].length;
    Set<String> uniqueIslands = new HashSet<>();
    boolean[][] visited = new boolean[m][n];
    for(int i = 0; i < m; i++) {
      for(int j = 0; j < n; j++) {
        StringBuilder builder = new StringBuilder();
        if(matrix[i][j] == 1 && !visited[i][j]) {
          visitIsland(i, j, matrix, visited, builder, "O");
          uniqueIslands.add(builder.toString());
        }
      }
    }

    return uniqueIslands.size();
  }

  private void visitIsland(int i, int j, int[][] matrix, boolean[][] visited, StringBuilder builder, String direction) {
    if(i < 0 || j < 0 || i >= matrix.length || j >= matrix[0].length)
      return;
    
    if(matrix[i][j] == 0 || visited[i][j]) return;

    visited[i][j] = true;

    builder.append(direction);

    visitIsland(i, j + 1, matrix, visited, builder, "R");
    visitIsland(i, j - 1, matrix, visited, builder, "L");
    visitIsland(i + 1, j, matrix, visited, builder, "D");
    visitIsland(i - 1, j, matrix, visited, builder, "U");

    builder.append("B");
  }
  
  public static void main(String[] args) {
    NumberOfUniqueIslands solution = new NumberOfUniqueIslands();

    System.out.println(solution.findDistinctIslandsDFS(
        new int[][] {
            { 1, 1, 0, 1, 1 },
            { 1, 1, 0, 1, 1 },
            { 0, 0, 0, 0, 0 },
            { 0, 1, 1, 0, 1 },
            { 0, 1, 1, 0, 1 }
        }));

    System.out.println(solution.findDistinctIslandsDFS(
        new int[][] {
            { 1, 1, 0, 1 },
            { 0, 1, 1, 0 },
            { 0, 0, 0, 0 },
            { 1, 1, 0, 0 },
            { 0, 1, 1, 0 }
        }));
  }
}
