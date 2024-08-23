import java.util.Arrays;
import java.util.List;


/*
 * This uses two pointer approach
 */

record Input(int[] nums, int target) {}

public class NumberOfSequenceWithSum {
    public int numSubseq(int[] nums, int target) {
        final int MOD = 1000000007;
        int count = 0;
        Arrays.sort(nums);
        int start = 0;
        int end = nums.length - 1;
        int[] exp = new int[nums.length];
        int i = 0;
        exp[i] = 1;
        for(i = 1; i < nums.length; i++) {
            exp[i] = (exp[i - 1] * 2) % MOD;
        }

        while(start <= end) {
            while(start <= end && nums[start] + nums[end] > target) {
                end -= 1;
            }
            
            if(start <= end) {
                count = (count + exp[end - start]) % MOD;
            }

            start += 1;
        }

        return count;
    }

    public static void main(String[] args) {
        NumberOfSequenceWithSum numberOfSequenceWithSum = new NumberOfSequenceWithSum();
        List.of(
            new Input(new int[]{3,5,6,7}, 9),
            new Input(new int[]{3,3,6,8}, 10),
            new Input(new int[]{2,3,3,4,6,7}, 12)
        ).forEach(
            (input) -> System.out.println(numberOfSequenceWithSum.numSubseq(input.nums(), input.target()))
        );
    }
}
