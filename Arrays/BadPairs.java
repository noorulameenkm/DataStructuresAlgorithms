import java.util.HashMap;
import java.util.Map;

public class BadPairs {
    public long countBadPairs(int[] nums) {
        int n = nums.length;
        long count = 0;
        Map<Integer, Integer> numToCount = new HashMap<>();
        for(int i = 0; i < n; i++)
            nums[i] = nums[i] - i;
        
        numToCount.put(nums[0], 1);
        for(int i = 1; i < n; i++) {
            count += (i - numToCount.getOrDefault(nums[i], 0));
            numToCount.put(nums[i], numToCount.getOrDefault(nums[i], 0) + 1);
        }

        return count;
    }

    public static void main(String[] args) {
        BadPairs badPairs = new BadPairs();

        int[] nums1 = {4, 1, 3, 3};
        System.out.println(badPairs.countBadPairs(nums1));  

        int[] nums2 = {1, 2, 3, 4, 5};
        System.out.println(badPairs.countBadPairs(nums2));
    }
}
