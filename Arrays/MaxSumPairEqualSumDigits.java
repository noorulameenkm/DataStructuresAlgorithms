import java.util.HashMap;
import java.util.Map;


public class MaxSumPairEqualSumDigits {

    public int maximumSum(int[] nums) {
        int max = Integer.MIN_VALUE;
        Map<Integer, Integer> digitSumToMax = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            int digitSum = sumOfDigits(nums[i]);

            if(!digitSumToMax.containsKey(digitSum)) {
                digitSumToMax.put(digitSum, nums[i]);
                continue;
            }

            int cachedMaxNum = digitSumToMax.get(digitSum);
            max = Math.max(max, nums[i] + cachedMaxNum);
            digitSumToMax.put(digitSum, Math.max(nums[i], cachedMaxNum));
        }

        return max == Integer.MIN_VALUE ? -1 : max;
    }

    int sumOfDigits(int num) {
        int sum = 0;
        while(num > 0) {
            sum += num % 10;
            num = num / 10;
        }

        return sum;
    }

    public static void main(String[] args) {
        MaxSumPairEqualSumDigits obj = new MaxSumPairEqualSumDigits();
        int[] nums = {18,43,36,13,7};
        System.out.println(obj.maximumSum(nums));

        nums = new int[]{10,12,19,14};
        System.out.println(obj.maximumSum(nums));
    }
}