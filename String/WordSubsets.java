import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class WordSubsets {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        List<String> result = new ArrayList<>();
        int[] maxFrequency = new int[26];
        Arrays.fill(maxFrequency, 0);

        for(String b: words2) {
            int[] bFrequency = new int[26];
            Arrays.fill(bFrequency, 0);
            for(char c : b.toCharArray()) {
                bFrequency[c - 'a'] ++;
                maxFrequency[c - 'a'] = Math.max(maxFrequency[c - 'a'], bFrequency[c - 'a']);
            }
        }

        for(String a: words1) {
            int[] aFrequency = new int[26];
            Arrays.fill(aFrequency, 0);
            for(char c : a.toCharArray()) {
                aFrequency[c - 'a'] ++;
            }

            if(isSubSet(maxFrequency, aFrequency)) {
                result.add(a);
            }
        }

        return result;
    }

    private boolean isSubSet(int[] maxFrequency, int[] aFrequency) {
        for(int i = 0; i < 26; i++) {
            if(maxFrequency[i] != 0 && maxFrequency[i] > aFrequency[i]) return false;
        }

        return true;
    }
    
    public static void main(String[] args) {
        WordSubsets obj = new WordSubsets();
        String[] words1 = {"amazon","apple","facebook","google","leetcode"};
        String[] words2 = {"e","o"};
        System.out.println(obj.wordSubsets(words1, words2));
    }
}
