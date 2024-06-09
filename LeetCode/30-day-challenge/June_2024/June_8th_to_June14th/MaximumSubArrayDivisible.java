import java.util.Map;
import java.util.HashMap;
import java.util.List;


record Input(int[] nums, int k) {}

public class MaximumSubArrayDivisible {
    public int subarraysDivByK(int[] nums, int k) {
        Map<Integer, Integer> remainders = new HashMap<>();
        remainders.put(0, 1);
        int count = 0;
        int sum = 0;
        for(int i = 0; i < nums.length; i++) {
            sum += nums[i];
            int remainder = sum % k;
            if(remainder < 0)   remainder += k;
            if(!remainders.containsKey(remainder)) {
                remainders.put(remainder, 1);
            } else {
                count += remainders.get(remainder);
                remainders.put(remainder, remainders.get(remainder) + 1);
            }
        }
        return count;
    }

    public static void main(String[] args) {
        MaximumSubArrayDivisible maximumSubArrayDivisible = new MaximumSubArrayDivisible();
        List<Input> inputs = List.of(
            new Input(new int[] {4,5,0,-2,-3,1}, 5),
            new Input(new int[] {5}, 9),
            new Input(new int[] {-1,2,9}, 2),
            new Input(new int[] {2,-2,2,-4}, 6)
        );

        inputs.forEach((input) -> System.out.println(maximumSubArrayDivisible.subarraysDivByK(input.nums(), input.k())));
    }
}
