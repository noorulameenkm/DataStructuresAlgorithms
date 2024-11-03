import java.util.Map;
import java.util.HashMap;
import java.util.Stack;

/**
 * Pattern:- Monotonic Stack
 */
public class NextGreaterElements {
    public static int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> stack = new Stack<>();
        Map<Integer, Integer> mapper = new HashMap<>();
        for(int num: nums2) {
            while(!stack.isEmpty() && num > stack.peek()) {
                int popped = stack.pop();
                mapper.put(popped, num);
            }

            stack.push(num);
        }

        for(int num : stack) {
            mapper.put(num, -1);
        }

        for(int i = 0; i < nums1.length; i++) {
            nums1[i] = mapper.get(nums1[i]);
        }

        return nums1;
    }


    public static void main(String[] args) {
        int[] nums1 = {4,2,6};
        int[] nums2 = {6,2,4,5,3,7};
        int[] output = nextGreaterElement(nums1, nums2);
        for (int num : output)
            System.out.print(num + " ");
        System.out.println();
    }
    
}
