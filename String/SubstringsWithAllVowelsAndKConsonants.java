import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class SubstringsWithAllVowelsAndKConsonants {
    public long countOfSubstrings(String word, int k) {
        if (word.length() < 5) {
            return 0;
        }
        Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u');
        Map<Character, Integer> vowelsMap = new HashMap<>();
        long count = 0;
        int start = 0, end = 0;
        int n = word.length();
        int consonants = 0;
        int[] nextCons = new int[n];
        int lastConsIndex = n;
        for (int i = n - 1; i >= 0; i--) {
            nextCons[i] = lastConsIndex;
            if (!vowels.contains(word.charAt(i))) {
                lastConsIndex = i;
            }
        }

        while (end < n) {
            char c = word.charAt(end);
            if (vowels.contains(c)) {
                vowelsMap.put(c, vowelsMap.getOrDefault(c, 0) + 1);
            } else {
                consonants++;
            }

            while (consonants > k) {
                char removeChar = word.charAt(start);
                if (vowels.contains(removeChar)) {
                    vowelsMap.put(removeChar, vowelsMap.get(removeChar) - 1);
                    if (vowelsMap.get(removeChar) == 0)
                        vowelsMap.remove(removeChar);
                } else {
                    consonants--;
                }

                start++;
            }

            while (start < n && vowelsMap.size() == 5 && consonants == k) {
                int index = nextCons[end];
                count += index - end;

                char removeChar = word.charAt(start);
                if (vowels.contains(removeChar)) {
                    vowelsMap.put(removeChar, vowelsMap.get(removeChar) - 1);
                    if (vowelsMap.get(removeChar) == 0)
                        vowelsMap.remove(removeChar);
                } else {
                    consonants--;
                }

                start++;
            }

            end++;
        }

        return count;
    }

    public static void main(String[] args) {
        SubstringsWithAllVowelsAndKConsonants obj = new SubstringsWithAllVowelsAndKConsonants();
        System.out.println(obj.countOfSubstrings("aeioqq", 1));
        System.out.println(obj.countOfSubstrings("aeiou", 0));
        System.out.println(obj.countOfSubstrings("ieaouqqieaouqq", 1));
    }
}
