package Greedy;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.Stack;

public class RemoveDuplicatesPreserveOrder {
    public static void main(String[] args) {
        System.out.println(
            removeDuplicateLetters(
                "babc"
            )
        );
        System.out.println(
            removeDuplicateLetters(
                "acbdbc"
            )
        );
    }

    private static String removeDuplicateLetters(String s) {
        // ToDo: Write Your Code Here.
        Map<Character, Integer> counter = new HashMap<>();
        for(char c : s.toCharArray()) {
            counter.compute(c, (key, val) -> {
                return val == null ? 1 : val + 1;
            });
        }

        Set<Character> processed = new HashSet<>();
        Stack<Character> result = new Stack<>();

        for(char c : s.toCharArray()) {
            if(!processed.contains(c)) {

                while(!result.isEmpty() && c < result.peek() && counter.get(result.peek()) > 0) {
                    processed.remove(result.pop());
                }

                processed.add(c);
                result.push(c);
            }

            counter.put(c, counter.get(c) - 1);
        }

        StringBuilder builder = new StringBuilder();
        for(char c : result) {
            builder.append(c);
        }

        return builder.toString();
    }
}
