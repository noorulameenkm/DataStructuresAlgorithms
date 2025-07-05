import java.util.HashMap;
import java.util.Map;

public class FruitBasket {

    public static int findLength(char[] arr) {
        int maxLength = 0;
        Map<Character, Integer> frequency = new HashMap<>();
        int start = 0;
        for(int end = 0; end < arr.length; end++) {
            frequency.put(arr[end], frequency.getOrDefault(arr[end], 0) + 1);

            while(frequency.size() > 2) {
                char removalChar = arr[start];
                frequency.put(removalChar, frequency.get(removalChar) - 1);
                if(frequency.get(removalChar) == 0) {
                    frequency.remove(removalChar);
                }
                start++;
            }

            maxLength = Math.max(maxLength, end - start + 1);
        }

        return maxLength;
    }

    public static void main(String[] args) {
        System.out.println(
            findLength(new char[]{'A', 'B', 'C', 'A', 'C'})
        );

        System.out.println(
           findLength( new char[]{'A', 'B', 'C', 'B', 'B', 'C'})
        );
    }
}