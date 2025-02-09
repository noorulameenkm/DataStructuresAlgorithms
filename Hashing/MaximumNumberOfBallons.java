package Hashing;

import java.util.HashMap;
import java.util.Map;

public class MaximumNumberOfBallons {
    
    public static int maxNumberOfBalloons(String text) {      
        int minCount = Integer.MAX_VALUE;
        Map<Character, Integer> frequency = new HashMap<>();
        for(char c: text.toCharArray()) {
            frequency.put(c, frequency.getOrDefault(c, 0) + 1);
        }

        minCount = Math.min(minCount, frequency.getOrDefault('b', 0));
        minCount = Math.min(minCount, frequency.getOrDefault('a', 0));
        minCount = Math.min(minCount, frequency.getOrDefault('l', 0) / 2);
        minCount = Math.min(minCount, frequency.getOrDefault('o', 0) / 2);
        minCount = Math.min(minCount, frequency.getOrDefault('n', 0));

        return minCount;
    }

    public static void main(String[] args) {
        System.out.println(
            maxNumberOfBalloons("balloonballoon")
        );

        System.out.println(
            maxNumberOfBalloons("bbaall")
        );

        System.out.println(
            maxNumberOfBalloons("balloonballoooon")
        );
    }
}
