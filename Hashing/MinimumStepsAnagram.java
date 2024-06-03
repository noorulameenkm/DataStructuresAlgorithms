package Hashing;

import java.util.Map;
import java.util.HashMap;
import java.util.List;

record Input(String s, String t) {};

public class MinimumStepsAnagram {
    public int minSteps(String s, String t) {
        Map<Character, Integer> sFrequency = this.getFrequencyMap(s);
        int length = t.length();
        int count = 0;
        for(int k = 0; k < length; k++) {
            Character c = t.charAt(k);
            if(sFrequency.containsKey(c) && sFrequency.get(c) > 0) {
                sFrequency.put(c, sFrequency.get(c) - 1);
            } else {
                count += 1;
            }
        }

        return count;
    }

    public Map<Character, Integer> getFrequencyMap(String str) {
        Map<Character, Integer> frequency = new HashMap<>();
        int length = str.length();
        for(int i = 0; i < length; i++) {
            Character c = str.charAt(i);
            frequency.put(c, frequency.getOrDefault(c, 0) + 1);
        }

        return frequency;
    }

    public static void main(String[] args) {
        List<Input> inputs = List.of(
            new Input("bab", "aba"),
            new Input("leetcode", "practice"),
            new Input("anagram", "mangaar")
        );

        MinimumStepsAnagram solutioAnagram = new MinimumStepsAnagram();

        for(Input input : inputs) {
            System.out.println(solutioAnagram.minSteps(input.s(), input.t()));
        }
    }
}