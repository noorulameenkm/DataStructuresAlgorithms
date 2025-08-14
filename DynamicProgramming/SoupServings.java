package DynamicProgramming;

import java.util.Arrays;

public class SoupServings {
    static final int[][] serves = new int[][] {{100, 0}, {75, 25}, {50, 50}, {25, 75}};
    double[][] dp;
    public double soupServings(int n) {
        if(n > 5000) return 1.0;
        dp = new double[n + 1][n + 1];
        for(int i = 0; i <= n; i++) {
            Arrays.fill(dp[i], -1.0);
        }
        return solve(n, n);
    }

    private double solve(int A, int B) {
        if(A <= 0 && B <= 0) return 0.5;
        if(A <= 0) return 1.0;
        if(B <= 0) return 0.0;

        if(dp[A][B] != -1.0) return dp[A][B];
        double total = 0.0;
        for(int[] serve: serves) {
            total += 0.25 * solve(A - serve[0], B - serve[1]); 
        }

        dp[A][B] = total;
        return dp[A][B];
    }

    public static void main(String[] args) {
        SoupServings soln = new SoupServings();
        System.out.println(soln.soupServings(100));
    }
}
