import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

public class MinimumOperationsToExceedThreshold {
    public int minOperations(int[] nums, int k) {
        if (Arrays.stream(nums).min().getAsInt() >= k)
            return 0;

        Queue<Long> pq = new PriorityQueue<>();

        for (int num : nums) {
            if (num < k)
                pq.offer((long) num);
        }

        int operation = 0;
        while (pq.size() >= 2 && pq.peek() < k) {
            long first = pq.poll();
            long second = pq.poll();

            pq.offer(Math.min(first, second) * 2 + Math.max(first, second));

            operation++;
        }

        return pq.isEmpty() || pq.peek() >= k ? operation : operation + 1;
    }

    public static void main(String[] args) {
        MinimumOperationsToExceedThreshold obj = new MinimumOperationsToExceedThreshold();
        int[] nums = { 999999999, 999999999, 999999999 };
        int k = 1000000000;
        System.out.println(obj.minOperations(nums, k));

        nums = new int[] { 2, 11, 10, 1, 3 };
        k = 10;
        System.out.println(obj.minOperations(nums, k));

        nums = new int[] { 1, 1, 2, 4, 9 };
        k = 20;
        System.out.println(obj.minOperations(nums, k));
    }
}
