import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;


record Input(int[] arr1, int[] arr2) {}

public class RelativeSortedArray {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        Map<Integer, Integer> frequency = new HashMap<>();
        for(int a : arr1) {
            frequency.put(a, frequency.getOrDefault(a, 0) + 1);
        }

        int i = 0;
        int j = 0;
        while(j < arr2.length) {
            int element = arr2[j];
            int internalSize = frequency.get(element);
            while(internalSize > 0) {
                arr1[i] = element;
                frequency.put(element, frequency.get(element) - 1);
                if(frequency.get(element) == 0) {
                    frequency.remove(element);
                }
                internalSize -= 1;
                i += 1;
            }

            j += 1;
        }

        if(i != arr1.length) {
            Queue<Integer> pq = new PriorityQueue<>(frequency.keySet());
            while(i != arr1.length) {
                int smallest = pq.peek();
                int smallestCount = frequency.get(smallest);
                while(smallestCount > 0) {
                    arr1[i] = smallest;
                    smallestCount -= 1;
                    i += 1;
                    frequency.put(smallest, frequency.get(smallest) - 1);
                }

                pq.poll();
            }
        }

        return arr1;
    }


    public static void main(String[] args) {
        RelativeSortedArray relativeSortedArray = new RelativeSortedArray();
        List.of(
            new Input(new int[] {2,3,1,3,2,4,6,7,9,2,19}, new int[] {2,1,4,3,9,6}),
            new Input(new int[] {28,6,22,8,44,17}, new int[] {22,28,8,6})
        ).forEach(input -> RelativeSortedArray.printArray(relativeSortedArray.relativeSortArray(input.arr1(), input.arr2())));
    }

    public static void printArray(int[] arr) {
        for (int a : arr) {
            System.out.printf("%d ", a);
        }
        System.out.println();
    }
}