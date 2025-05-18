package Hashing;

import java.util.HashMap;
import java.util.Map;

public class LongestPalindromicStringLength {

   public static int longestPalindrome(String s) {
        int length = 0;
        Map<Character, Integer> frequency = new HashMap<>();
        for(char c: s.toCharArray()) {
            frequency.put(c, frequency.getOrDefault(c, 0) + 1);
        }

        boolean oddFound = false;
        for(Map.Entry<Character, Integer> entry : frequency.entrySet()) {
            if(entry.getValue() % 2 == 0) {
                length += entry.getValue();
            } else {
                length += entry.getValue() - 1;
                oddFound = true;
            }
        }

        if(oddFound) {
            length ++;
        }

        return length;
    }

    public static void main(String[] args) {
        System.out.println(
            longestPalindrome("applepie")
        );

        System.out.println(
            longestPalindrome("aabbcc")
        );

        System.out.println(
            longestPalindrome("bananas")
        );
    }
}