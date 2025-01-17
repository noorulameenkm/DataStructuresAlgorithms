package Bit;

import java.util.HashMap;
import java.util.Map;

public class BitwiseXorAllPairings {
    public int xorAllNums(int[] nums1, int[] nums2) {
        int result = 0;
        Map<Integer, Integer> frequency = new HashMap<>();

        for(int num1 : nums1) {
            frequency.put(num1, frequency.getOrDefault(num1, 0) + nums2.length);
        }

        for(int num2: nums2) {
            frequency.put(num2, frequency.getOrDefault(num2, 0) + nums1.length);
        }

        for(Map.Entry<Integer, Integer> entry: frequency.entrySet()) {
            if(entry.getValue() % 2 != 0) {
                result = result ^ entry.getKey();
            }
        }

        return result;
    }

    public int xorAllNums2(int[] nums1, int[] nums2) {
        int result = 0;
        if(nums1.length % 2 != 0) {
            for(int num2: nums2) {
                result = result ^ num2;
            }
        }

        if(nums2.length % 2 != 0) {
            for(int num1: nums1) {
                result = result ^ num1;
            }
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        BitwiseXorAllPairings solution = new BitwiseXorAllPairings();
        System.out.println(solution.xorAllNums(new int[]{2,1,3}, new int[]{10,2,5,0}));
        System.out.println(solution.xorAllNums(new int[]{1,2}, new int[]{3,4}));

        System.out.println(solution.xorAllNums2(new int[]{2,1,3}, new int[]{10,2,5,0}));
        System.out.println(solution.xorAllNums2(new int[]{1,2}, new int[]{3,4}));
    }
}
