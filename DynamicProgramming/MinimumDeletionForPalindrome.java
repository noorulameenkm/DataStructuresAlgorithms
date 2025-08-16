public class MinimumDeletionForPalindrome {
    public int findMinimumDeletionsBottomUp(String st) {
        int n = st.length();
        int[][] dp = new int[n][n];
        for(int length = 1; length <= n; length++) {
            for(int start = 0; start + length - 1 < n; start++) {
                int end = start + length - 1;
                
                if(start == end) dp[start][end] = 0;
                else if(st.charAt(start) == st.charAt(end)) dp[start][end] = dp[start + 1][end - 1];
                else dp[start][end] = 1 + Math.min(dp[start][end - 1], dp[start + 1][end]);
            }
        }
        return dp[0][n - 1];
    }

    public int findMinimumDeletionsMemoizationRecursive(String st) {
        int n = st.length();
        Integer[][] dp = new Integer[n][n];
        return findMinimumDeletionsMemoizationRecursive(st, 0, n - 1, dp);
    }

    private int findMinimumDeletionsMemoizationRecursive(String st, int start, int end, Integer[][] dp) {
        if(start > end) return 0;
        if(start == end) return 0;
        if(dp[start][end] != null) return dp[start][end];
        if(st.charAt(start) == st.charAt(end)) {
            dp[start][end] = findMinimumDeletionsMemoizationRecursive(st, start + 1, end - 1, dp);
            return dp[start][end];
        }

        dp[start][end] = 1 + Math.min(findMinimumDeletionsMemoizationRecursive(st, start + 1, end, dp), findMinimumDeletionsMemoizationRecursive(st, start, end - 1, dp));
        return dp[start][end];
    }

    public int findMinimumDeletionsRecursive(String st) {
        int n = st.length();
        return findMinimumDeletionsRecursive(st, 0, n - 1);
    }

    private int findMinimumDeletionsRecursive(String st, int start, int end) {
        if(start > end) return 0;
        if(start == end) return 0;
        if(st.charAt(start) == st.charAt(end)) {
            return findMinimumDeletionsRecursive(st, start + 1, end - 1);
        }

        return 1 + Math.min(findMinimumDeletionsRecursive(st, start + 1, end), findMinimumDeletionsRecursive(st, start, end - 1));
    }

    public static void main(String[] args) {
        MinimumDeletionForPalindrome soln  = new MinimumDeletionForPalindrome();
        String s = "abdbca";
        System.out.println(soln.findMinimumDeletionsRecursive(s));
        System.out.println(soln.findMinimumDeletionsMemoizationRecursive(s));
        System.out.println(soln.findMinimumDeletionsBottomUp(s));

        s = "cddpd";
        System.out.println(soln.findMinimumDeletionsRecursive(s));
        System.out.println(soln.findMinimumDeletionsMemoizationRecursive(s));
        System.out.println(soln.findMinimumDeletionsBottomUp(s));
    }
}
