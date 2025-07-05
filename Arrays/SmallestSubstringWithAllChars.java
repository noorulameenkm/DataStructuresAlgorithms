import java.util.HashMap;
import java.util.Map;

public class SmallestSubstringWithAllChars {

    public String findSubstring(String str, String pattern) {
      Map<Character, Integer> frequency = new HashMap<>();
      int matchedCharCount = 0;
      String result = "";
      int minLength = Integer.MAX_VALUE;
      for(char c : pattern.toCharArray()) {
        frequency.merge(c, 1, Integer::sum);
      }

      int start = 0;
      for(int end = 0; end < str.length(); end++) {
        char c = str.charAt(end);
        if(frequency.containsKey(c)) {
          frequency.put(c, frequency.get(c) - 1);

          if(frequency.get(c) == 0) matchedCharCount++;
        }

        while (matchedCharCount == frequency.size() && start <= end) {
            int length = end - start + 1;
            if(length < minLength) {
              minLength = length;
              result = str.substring(start, end + 1);
            }

            char removeChar = str.charAt(start);
            start ++;
            if (frequency.containsKey(removeChar)) {
              if(frequency.get(removeChar) == 0) {
                matchedCharCount--;
              }
              frequency.put(removeChar, frequency.get(removeChar) + 1);
            }
        }
      }
      return result; 
    }

    public static void main(String[] args) {
        SmallestSubstringWithAllChars finder = new SmallestSubstringWithAllChars();
        String str = "aabdec";
        String pattern = "abc";
        String result = finder.findSubstring(str, pattern);
        System.out.println("Smallest substring containing all characters: " + result);
    }
}