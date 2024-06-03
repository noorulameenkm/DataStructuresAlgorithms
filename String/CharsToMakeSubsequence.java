public class CharsToMakeSubsequence {
    public int appendCharacters(String s, String t) {
        int i = 0;
        int j = 0;
        int m = s.length();
        int n = t.length();
        while(i < m && j < n) {
            if(s.charAt(i) == t.charAt(j)) {
                i += 1;
                j += 1;
            } else {
                i += 1;
            }
        }

        return n - j;
    }


    public static void main(String[] args) {
        var s = "coaching";
        var t = "coding";
        CharsToMakeSubsequence solution = new CharsToMakeSubsequence();
        System.out.println(solution.appendCharacters(s, t));
    }
}
