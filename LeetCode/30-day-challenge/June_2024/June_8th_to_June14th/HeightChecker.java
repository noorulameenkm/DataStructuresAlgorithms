import java.util.Queue;
import java.util.PriorityQueue;
import java.util.Map;
import java.util.HashMap;
import java.util.List;

record Input(int[] heights) {}

public class HeightChecker {
    public int heightChecker(int[] heights) {
        Map<Integer, Integer> frequency = new HashMap<>();
        for(int height : heights) {
            frequency.put(height, frequency.getOrDefault(height, 0) + 1);
        }

        Queue<Integer> pq = new PriorityQueue<>(frequency.keySet());
        int i = 0;
        int size = pq.size();
        int count = 0;
        while(size > 0) {
            int val = pq.peek();
            if(val != heights[i]) {
                count += 1;
            }

            i += 1;
            frequency.put(val, frequency.get(val) - 1);
            if(frequency.get(val) == 0) {
                pq.poll();
                size -= 1;
            }
        }

        return count;

    }

    public static void main(String[] args) {
        HeightChecker heightChecker = new HeightChecker();
        List<Input> inputs = List.of(
            new Input(new int[] {1,1,4,2,1,3}),
            new Input(new int[] {5,1,2,3,4}),
            new Input(new int[] {1,2,3,4,5})
        );

        inputs.forEach((input) -> System.out.println(heightChecker.heightChecker(input.heights())));
    }
}