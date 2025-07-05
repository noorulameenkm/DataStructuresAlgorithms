package PrefixSum;

import java.util.HashMap;
import java.util.Map;

public class NumberOfSubArraysWithSumEqualToGoal {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int count = 0;
        Map<Integer, Integer> cumSumMap = new HashMap<>();
        cumSumMap.put(0, 1);
        int cumSum = 0;
        for(int num : nums) {
            cumSum += num;
            count += cumSumMap.getOrDefault(cumSum - goal, 0);
            cumSumMap.put(cumSum, cumSumMap.getOrDefault(cumSum, 0) + 1);
        }

        return count;
    }

    public static void main(String[] args) {
        NumberOfSubArraysWithSumEqualToGoal solution = new NumberOfSubArraysWithSumEqualToGoal();
        int[] nums = {1, 0, 1, 0, 1};
        int goal = 2;
        System.out.println(solution.numSubarraysWithSum(nums, goal)); // Output: 4
        int[] nums2 = {0, 0, 0, 0, 0};
        int goal2 = 0;
        System.out.println(solution.numSubarraysWithSum(nums2, goal2)); // Output: 15
    }
}
