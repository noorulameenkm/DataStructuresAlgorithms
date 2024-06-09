import java.util.Map;
import java.util.HashMap;
import java.util.List;


record Input(int[] nums, int k) {}

public class MaximumSubArrayMultiple {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> remainders = new HashMap<>();
        remainders.put(0, -1);
        int sum = 0;
        for(int i = 0; i < nums.length; i++) {
            sum += nums[i];
            int remainder = sum % k;
            if(!remainders.containsKey(remainder)) {
                remainders.put(remainder, i);
            } else if(i - remainders.get(remainder) > 1) {
                return true;
            }
        }
        
        return false;
    }

    public static void main(String[] args) {
        MaximumSubArrayMultiple maximumSubArrayMultiple = new MaximumSubArrayMultiple();
        List<Input> inputs = List.of(
            new Input(new int[] {23,2,4,6,7}, 6),
            new Input(new int[] {23,2,6,4,7}, 6),
            new Input(new int[] {23,2,6,4,7}, 13),
            new Input(new int[] {23,2,4,6,6}, 7)
        );

        inputs.forEach((input) -> System.out.println(maximumSubArrayMultiple.checkSubarraySum(input.nums(), input.k())));
    }

}
