package Heap;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;


/**
 * Pattern:- Top 'K' Elements
 */
public class TopKFrequentElement {

    public static List<Integer> findTopKFrequentNumbers(int[] nums, int k) {
    List<Integer> topNumbers = new ArrayList<>(k);
    Map<Integer, Integer> frequency = new HashMap<>();
    for(int num: nums) {
      frequency.put(
        num, frequency.getOrDefault(num, 0) + 1
      );
    }

    Queue<Map.Entry<Integer, Integer>> minHeap =
      new PriorityQueue<>((e1, e2) -> e1.getValue() - e2.getValue());

    for(Map.Entry<Integer, Integer> entry: frequency.entrySet()) {
      minHeap.add(entry);
      if(minHeap.size() > k) {
        minHeap.poll();
      }
    }

    for(Map.Entry<Integer, Integer> entry: minHeap) {
      topNumbers.add(entry.getKey());
    }

    return topNumbers;
  }

  public static void main(String[] args) {
    System.out.println(
        findTopKFrequentNumbers(
            new int[]{1, 3, 5, 12, 11, 12, 11}, 2)
    );

    System.out.println(
        findTopKFrequentNumbers(
            new int[]{5, 12, 11, 3, 11}, 2)
    );
  }
    
}