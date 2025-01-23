public class CountServersThatCommunicate {
    public int countServers(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;
        int[] rows = new int[m];
        int[] cols = new int[n];

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1) {
                    rows[i]++;
                    cols[j]++;
                }
            }
        }

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1) {
                    if(rows[i] > 1 || cols[j] > 1)
                        count += 1;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        CountServersThatCommunicate countServersThatCommunicate = new CountServersThatCommunicate();
        System.out.println(
            countServersThatCommunicate.countServers(
                new int[][] {
                    {1, 0},
                    {0, 1}
                }
            )
        );

        System.out.println(
            countServersThatCommunicate.countServers(
                new int[][] {
                    {1, 0},
                    {1, 1}
                }
            )
        );

        System.out.println(
            countServersThatCommunicate.countServers(
                new int[][] {
                    {1, 1, 0, 0},
                    {0, 0, 1, 0},
                    {0, 0, 1, 0},
                    {0, 0, 0, 1}
                }
            )
        );
    }
}
