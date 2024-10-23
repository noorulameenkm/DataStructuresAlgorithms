import java.util.Map;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Collectors;

record Input(int[] hand, int groupSize) {}

class HandOfStraights {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if(hand.length % groupSize != 0) {
            return false;
        }

        Map<Integer, Integer> frequency = new HashMap<>();
        for(int h : hand) {
            frequency.put(h, frequency.getOrDefault(h, 0) + 1);
        }

        Queue<Integer> pq = new PriorityQueue<>();
        pq.addAll(IntStream.range(0, 10).collect(Collectors.toList()));
        pq.addAll(frequency.keySet());
        int size = pq.size();
        while(size > 0) {
            int start = pq.peek();
            for(int number = start; number < start + groupSize; number++) {
                if(!frequency.containsKey(number) || frequency.get(number) <= 0) {
                    return false;
                }
                frequency.put(number, frequency.get(number) - 1);
                if(frequency.get(number) == 0)  {
                    if(pq.peek() != number) {
                        return false;
                    }

                    pq.poll();
                    size -= 1;
                }
            }
        }

        return true;
    }

    public static void main(String[] args) {
        HandOfStraights handOfStraights = new HandOfStraights();
        List<Input> iputList = List.of(
            new Input(new int[]{1,2,3,6,2,3,4,7,8}, 3),
            new Input(new int[]{1,2,3,4,5}, 4)
        );

        iputList.forEach((input) -> System.out.println(handOfStraights.isNStraightHand(input.hand(), input.groupSize())));
    }
}