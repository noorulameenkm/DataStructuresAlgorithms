import java.util.ArrayDeque;
import java.util.Deque;

public class MaximumRampWidth {

    public static void main(String[] args) {
        MaximumRampWidth mrw = new MaximumRampWidth();
        System.out.println(
            mrw.maximumRampWidth(6,0,8,2,1,5)
        );

        System.out.println(
            mrw.maximumRampWidth(
                9,8,1,0,1,9,4,0,4,1
            )
        );
    }

    private int maximumRampWidth(int ...nums) {
        int max = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        for(int i = 0; i < nums.length - 1; i++) {
           if(stack.isEmpty() || nums[i] < nums[stack.peek()]) {
                stack.push(i);
           }
        }

        for(int end = nums.length - 1; end >= 0; end--) {
            while(!stack.isEmpty() && nums[stack.peek()] <= nums[end]) {
                int start = stack.pop();
                max = Math.max(max, end - start);
            }

            if(stack.isEmpty()) {
                break;
            }
        }

        return max;
    }
}