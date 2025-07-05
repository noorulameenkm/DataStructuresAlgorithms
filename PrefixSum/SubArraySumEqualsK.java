package PrefixSum;

import java.util.HashMap;
import java.util.Map;

public class SubArraySumEqualsK {
    public int maxSubArrayLen(int[] nums, int k) {
        Map<Integer, Integer> cumSumMap = new HashMap<>();
        int cumSum = 0;
        int maxLength = 0;
        for(int i = 0; i < nums.length; i++) {
            cumSum += nums[i];
            if(cumSum == k) maxLength = Math.max(maxLength, i + 1);
            else if(cumSumMap.containsKey(cumSum - k) && i - cumSumMap.get(cumSum - k) > maxLength)
                maxLength = i - cumSumMap.get(cumSum - k);

            cumSumMap.put(cumSum, Math.min(cumSumMap.getOrDefault(cumSum, Integer.MAX_VALUE), i));
        }  

        return maxLength;
    }

    public static void main(String[] args) {
        SubArraySumEqualsK solution = new SubArraySumEqualsK();
        int[] nums = {1, -1, 5, -2, 3};
        int k = 3;
        System.out.println(solution.maxSubArrayLen(nums, k)); // Output: 4
        int[] nums2 = {-2, -1, 2, 1};
        int k2 = 1;
        System.out.println(solution.maxSubArrayLen(nums2, k2)); // Output: 2
    }
}
