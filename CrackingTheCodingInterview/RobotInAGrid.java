import java.util.ArrayList;
import java.util.List;

public class RobotInAGrid {
    record Cell(int row, int col) {}

    public static void main(String[] args) {
        int[][] grid = {
            {0, 0, 0, 0},
            {0, 1, 0, 0},
            {0, 0, 0, 1},
            {0, 0, 0, 0}
        };
        
        RobotInAGrid robot = new RobotInAGrid();
        List<Cell> path = new ArrayList<>();
        boolean result = robot.findPath(grid, 0, 0, new boolean[grid.length][grid[0].length], path);
        System.out.println("Is there a path from top-left to bottom-right? " + result + " " + path);
    }

    boolean findPath(int[][] grid, int row, int col, boolean[][] visited, List<Cell> path) {
        if(row == grid.length - 1 && col == grid[0].length - 1) {
            System.out.println("Path found to (" + row + ", " + col + ")");
            path.add(new Cell(row, col));
            return true;
        }

        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || 
           grid[row][col] == 1 || visited[row][col]) {
            return false;
        }

        visited[row][col] = true;

        path.add(new Cell(row, col));

        boolean result =
            findPath(grid, row, col + 1, visited, path) || findPath(grid, row + 1, col, visited, path);
        
        if(!result) {
            path.remove(path.size() - 1);
        }

        return result;
    }
    
}
