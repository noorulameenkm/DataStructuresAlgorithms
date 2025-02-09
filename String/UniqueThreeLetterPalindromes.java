import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class UniqueThreeLetterPalindromes {

    public int countPalindromicSubsequence(String s) {
        int[] left = new int[26], right = new int[26];

        Arrays.fill(left, -1);
        Arrays.fill(right, -1);

        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int index = c - 'a';

            if(left[index] == -1) {
                left[index] = i;
            }

            right[index] = i;
        }

        int total = 0;
        for(int i = 0; i < 26; i++) {
            if(left[i] == -1) continue;

            Set<Character> uniqueSet = new HashSet<>();
            for(int j = left[i] + 1; j < right[i]; j++) {
                uniqueSet.add(s.charAt(j));
            }

            total += uniqueSet.size();
        }

        return total;
    }

    public static void main(String[] args) {
        UniqueThreeLetterPalindromes uniqueThreeLetterPalindromes = new UniqueThreeLetterPalindromes();
        System.out.println(uniqueThreeLetterPalindromes.countPalindromicSubsequence("aabca"));
        System.out.println(uniqueThreeLetterPalindromes.countPalindromicSubsequence("adc"));
        System.out.println(uniqueThreeLetterPalindromes.countPalindromicSubsequence("bbcbaba"));
    }
}