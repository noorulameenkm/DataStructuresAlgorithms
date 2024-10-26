import java.util.HashSet;
import java.util.Set;
import java.util.List;

record InputOutput<I, O>(I input, O output) {}

public class NonRepeatingSubString {

    public static void main(String[] args) {
        List<InputOutput<String, Integer>> inputOutput =
            List.of(
                new InputOutput<>("tmmzuxt", 5),
                new InputOutput<>("abcdaef", 6),
                new InputOutput<>("aaaaa", 1),
                new InputOutput<>("abrkaabcdefghijjxxx", 10)
            );

        for(InputOutput<String, Integer> io : inputOutput) {
            System.out.println(lengthOfLongestSubstring(io.input()));
        }
    }

    public static int lengthOfLongestSubstring(String str) {
        int maxLength = 0, start = 0;
        Set<Character> uniqueCharacters = new HashSet<>();
        for(int end = 0; end < str.length(); end++) {
            char element = str.charAt(end);
            while(uniqueCharacters.contains(element)) {
                char removeChar = str.charAt(start);
                uniqueCharacters.remove(removeChar);
                start ++;
            }

            uniqueCharacters.add(element);

            maxLength = Math.max(maxLength, end - start + 1);
        }

        return maxLength;
    }
}
