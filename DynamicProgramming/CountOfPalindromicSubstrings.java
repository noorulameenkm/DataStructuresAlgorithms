public class CountOfPalindromicSubstrings {

    public int findCPS(String st) {
    int n = st.length();
    boolean[][] dp = new boolean[n][n];
    int count = 0;
    for(int l = 1; l <= n; l++) {
      for(int i = 0; i + l - 1 < n; i++) {
        int j = i + l - 1;

        if(i == j) dp[i][j] = true;
        else if(i + 1 == j) dp[i][j] = st.charAt(i) == st.charAt(j);
        else dp[i][j] = st.charAt(i) == st.charAt(j) && dp[i + 1][j - 1];

        if(dp[i][j]) count++;
      }
    }

    return count;
  }

  public static void main(String[] args) {
    CountOfPalindromicSubstrings soln = new CountOfPalindromicSubstrings();
    System.out.println(soln.findCPS("abdbca"));
  }
}