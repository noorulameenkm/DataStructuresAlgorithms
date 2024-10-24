


/**
 * Pattern:- Sliding Window
 */
public class LongestSubArrayOnesAfterDeletingOneElement {

    public static void main(String[] args) {
        System.out.println(longestSubarray(new int[]{1, 1, 0, 0, 1, 1}));
        System.out.println(longestSubarray(new int[]{1, 1, 0, 1, 1, 1}));
        System.out.println(longestSubarray(new int[]{1, 0, 1, 1, 0, 1}));
    }

    public static int longestSubarray(int[] nums) {
        int start = 0;
        int maxLength = 0;
        int zeroCount = 0;
        for(int end = 0; end < nums.length; end++) {
            zeroCount += nums[end] == 0 ? 1 : 0;

            while(zeroCount > 1) {
                if(nums[start] == 0) {
                    zeroCount--;
                }

                start++;
            }

            maxLength = Math.max(maxLength, end - start);
        }
        return maxLength;
    } 
}