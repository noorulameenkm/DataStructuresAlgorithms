package SortedSet;

import java.util.TreeMap;

public class LongestContigousSubArrayWithDifferenceLimit {
     public  int longestSubarray(int[] nums, int limit) {
        int left = 0, maxLength = 0;
        TreeMap<Integer, Integer> sortedMap = new TreeMap<>(); 
        for(int right = 0; right < nums.length; right++) {
            sortedMap.put(nums[right], sortedMap.getOrDefault(nums[right], 0) + 1);

            while(sortedMap.lastKey() - sortedMap.firstKey() > limit) {
                sortedMap.put(nums[left], sortedMap.get(nums[left]) - 1);
                if(sortedMap.get(nums[left]) == 0) {
                    sortedMap.remove(nums[left]);
                }

                left++;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }

    public static void main(String[] args) {
        LongestContigousSubArrayWithDifferenceLimit obj = new LongestContigousSubArrayWithDifferenceLimit();
        int[] nums = {10, 1, 2, 4, 7};
        int limit = 5;
        System.out.println(obj.longestSubarray(nums, limit));

        nums = new int[]{4, 8, 5, 1, 7, 9};
        limit = 3;
        System.out.println(obj.longestSubarray(nums, limit));

        nums = new int[]{3, 3, 3, 3, 3};
        limit = 0;
        System.out.println(obj.longestSubarray(nums, limit));

    }
}
