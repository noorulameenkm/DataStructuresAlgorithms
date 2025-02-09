import java.util.Arrays;

public class AllCharKPalindromicString {
    public boolean canConstruct(String s, int k) {
        if(s.length() == k) return true;

        if(k > s.length())  return false;

        int[] frequency = new int[26];
        Arrays.fill(frequency, 0);
        for(char c : s.toCharArray()) {
            frequency[c - 'a'] ++;
        }

        int oddFrequencyCharCount = 0;
        for(int i = 0; i < 26; i++) {
            if(frequency[i] % 2 != 0) oddFrequencyCharCount++;
        }

        return oddFrequencyCharCount <= k;
    }

    public static void main(String[] args) {
        AllCharKPalindromicString obj = new AllCharKPalindromicString();
        System.out.println(obj.canConstruct("annabelle", 2));
        System.out.println(obj.canConstruct("leetcode", 3));
        System.out.println(obj.canConstruct("true", 4));
        System.out.println(obj.canConstruct("yzyzyzyzyzyzyzy", 2));
    }
}
