public class GridGame {
    public long gridGame(int[][] grid) {
        long firstRowSum = 0;
        for(int i = 0; i < grid[0].length; i++) {
            firstRowSum += grid[0][i];
        }

        long secondRowSum = 0;
        long minRobot2Points = Long.MAX_VALUE;
        for(int robot1Col = 0; robot1Col < grid[0].length; robot1Col++)  {
            firstRowSum -= grid[0][robot1Col];
            long robot2Max = Math.max(firstRowSum, secondRowSum);
            minRobot2Points = Math.min(robot2Max, minRobot2Points);
            secondRowSum += grid[1][robot1Col];
        }

        return minRobot2Points;
    }


    public static void main(String[] args) {
        GridGame gridGame = new GridGame();

        System.out.println(
            gridGame.gridGame(
                new int[][] {
                    {2, 5, 4},
                    {1, 5, 1}
                }
            )
        );

        System.out.println(
            gridGame.gridGame(
                new int[][] {
                    {3, 3, 1},
                    {8, 5, 2}
                }
            )
        );

        System.out.println(
            gridGame.gridGame(
                new int[][] {
                    {1, 3, 1, 15},
                    {1, 3, 3, 1}
                }
            )
        );
    }
}