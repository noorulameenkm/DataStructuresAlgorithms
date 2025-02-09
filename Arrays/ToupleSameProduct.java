import java.util.HashMap;
import java.util.Map;

public class ToupleSameProduct {

    public int tupleSameProduct(int[] nums) {
        if (nums.length < 4)
            return 0;
        Map<Integer, Integer> map = new HashMap<>();
        int n = nums.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int prod = nums[i] * nums[j];
                map.put(prod, map.getOrDefault(prod, 0) + 2);
            }
        }

        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int prod = nums[i] * nums[j];
                count += (map.get(prod) - 2) * 2;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        ToupleSameProduct tsp = new ToupleSameProduct();
        int[] nums = {2, 3, 4, 6};
        System.out.println(tsp.tupleSameProduct(nums));

        int[] nums1 = {1, 2, 4, 5, 10};
        System.out.println(tsp.tupleSameProduct(nums1));
    }
}