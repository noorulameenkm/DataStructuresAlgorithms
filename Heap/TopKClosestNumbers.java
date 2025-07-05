package Heap;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

public class TopKClosestNumbers {
    /**
     * Pattern:- Top 'K' Elements
     * 
     * Time Complexity - O(N * logK)
     * 
     * @param arr
     * @param K
     * @param X
     * @return
     */
    public static List<Integer> findClosestElements(int[] arr, int K, int X) {
        List<Integer> result = new ArrayList<>();
        Queue<Map.Entry<Integer, Integer>> maxHeap = new PriorityQueue<>((e1, e2) -> {
            if (e1.getKey().equals(e2.getKey())) {
                return e2.getValue() - e1.getValue();
            }

            return e2.getKey() - e1.getKey();
        });

        for (int i = 0; i < arr.length; i++) {
            maxHeap.add(
                    Map.entry(Math.abs(arr[i] - X), arr[i]));

            if (maxHeap.size() > K) {
                maxHeap.poll();
            }
        }

        while (!maxHeap.isEmpty()) {
            result.add(maxHeap.poll().getValue());
        }

        Collections.sort(result);

        return result;
    }

    /**
     * 
     * Pattern:- Binary Search and Top 'K' Elements
     * Time Complexity - O(logN + KlogK)
     * 
     * @param arr
     * @param K
     * @param X
     * @return
     */
    public static List<Integer> findClosestElements2(int[] arr, int K, int X) {
        int index = binarySearch(arr, X);
        int low = index - K, high = index + K;
        low = Math.max(low, 0); // 'low' should not be less than zero
        // 'high' should not be greater the size of the array
        high = Math.min(high, arr.length - 1);

        Queue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<>((n1, n2) -> n1.getKey() - n2.getKey());
        // add all candidate elements to the min heap, sorted by their absolute
        // difference
        // from 'X'
        for (int i = low; i <= high; i++)
            minHeap.add(Map.entry(Math.abs(arr[i] - X), i));

        // we need the top 'K' elements having smallest difference from 'X'
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < K; i++)
            result.add(arr[minHeap.poll().getValue()]);

        Collections.sort(result);
        return result;
    }

    /**
     * Pattern:- Two pointers
     * Time Complexity - O(logN + K)
     * 
     * @param arr
     * @param K
     * @param X
     * @return
     */
    public static List<Integer> findClosestElements3(int[] arr, int K, Integer X) {
        List<Integer> result = new LinkedList<>();

        // Find the index of the element closest to X using binary search
        int index = binarySearch(arr, X);
        int leftPointer = index;
        int rightPointer = index + 1;

        for (int i = 0; i < K; i++) {
            if (leftPointer >= 0 && rightPointer < arr.length) {
                int diff1 = Math.abs(X - arr[leftPointer]);
                int diff2 = Math.abs(X - arr[rightPointer]);

                // Choose the element with the smaller absolute difference
                if (diff1 <= diff2)
                    result.add(0, arr[leftPointer--]); // Add to the beginning of the list
                else
                    result.add(arr[rightPointer++]); // Add to the end of the list
            } else if (leftPointer >= 0) {
                result.add(0, arr[leftPointer--]);
            } else if (rightPointer < arr.length) {
                result.add(arr[rightPointer++]);
            }
        }

        return result;
    }

    private static int binarySearch(int[] arr, int target) {
        int low = 0;
        int high = arr.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == target)
                return mid;
            if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        if (low > 0) {
            return low - 1;
        }
        return low;
    }

    public static void main(String[] args) {

        System.out.println(
                findClosestElements(new int[] { 5, 6, 7, 8, 9 }, 3, 7));

        System.out.println(
                findClosestElements(new int[] { 2, 4, 5, 6, 9 }, 3, 6));

        System.out.println(
                findClosestElements(new int[] { 2, 4, 5, 6, 9 }, 3, 10));

        System.out.println("************Second Solution*******************");

        System.out.println(
                findClosestElements2(new int[] { 5, 6, 7, 8, 9 }, 3, 7));

        System.out.println(
                findClosestElements2(new int[] { 2, 4, 5, 6, 9 }, 3, 6));

        System.out.println(
                findClosestElements2(new int[] { 2, 4, 5, 6, 9 }, 3, 10));

        System.out.println("************Third Solution*******************");

        System.out.println(
                findClosestElements3(new int[] { 5, 6, 7, 8, 9 }, 3, 7));

        System.out.println(
                findClosestElements3(new int[] { 2, 4, 5, 6, 9 }, 3, 6));

        System.out.println(
                findClosestElements3(new int[] { 2, 4, 5, 6, 9 }, 3, 10));
    }
}
