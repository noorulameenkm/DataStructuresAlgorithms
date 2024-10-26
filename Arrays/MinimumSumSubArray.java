/**
 * Pattern:- Sliding Window
 */
public class MinimumSumSubArray {
    public static void main(String[] args) {
        System.out.println(
            minSubArrayLen(
                15, new int[] {1, 2, 3, 4, 5, 6, 7, 8})
        );

        System.out.println(
            minSubArrayLen(
                11, new int[] {2, 1, 5, 2, 8})
        );

        System.out.println(
            minSubArrayLen(
                8, new int[] {2, 1, 5, 2, 3})
        );
    }

    public static int minSubArrayLen(int target, int[] nums) {
        int start = 0;
        int sum = 0;
        int minSize = Integer.MAX_VALUE;
        for(int end = 0; end < nums.length; end++) {
            sum += nums[end];
            
            while(sum >= target && start <= end) {
                minSize = Math.min(minSize, end - start + 1);
                sum -= nums[start];
                start ++;
            }
        }

        return minSize == Integer.MAX_VALUE ? 0 : minSize;
    }
}