class MaximumNumberOfFruitsCollected {

    public int maxCollectedFruits(int[][] fruits) {
        int n = fruits.length;
        int[][] dp = new int[n][n];

        int result = 0;

        // child1 
        for(int i = 0; i < n; i++) result += fruits[i][i];

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if((i < j || i > j) && i + j < n - 1) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = fruits[i][j];
                }
            }
        }

        // child2
        for(int i = 1; i < n; i++) {
            for(int j = i + 1; j < n; j++) {
                dp[i][j] += Math.max(dp[i - 1][j - 1], Math.max(dp[i - 1][j], (j + 1) < n ? dp[i - 1][j + 1] : 0));
            }
        }

        // child3
        for(int j = 1; j < n; j++) {
            for(int i = j + 1; i < n; i++) {
                dp[i][j] += Math.max(dp[i][j - 1], Math.max(dp[i - 1][j - 1], (i + 1) < n ? dp[i + 1][j - 1] : 0));
            }
        }


        return result + dp[n - 2][n - 1] + dp[n - 1][n - 2];
    }

    public static void main(String[] args) {
        MaximumNumberOfFruitsCollected soln = new MaximumNumberOfFruitsCollected();
        int[][] input = new int[][] {{1,2,3,4},{5,6,8,7},{9,10,11,12},{13,14,15,16}};
        System.out.println(soln.maxCollectedFruits(input));
    }
}