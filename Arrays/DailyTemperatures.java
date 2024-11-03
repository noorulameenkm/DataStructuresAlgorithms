import java.util.Arrays;
import java.util.Stack;

/**
 * Pattern:- Monotonic Stack
 */
public class DailyTemperatures {
    public static int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer[]> stack = new Stack<>();
        for(int i = 0; i < temperatures.length; i++) {
            int value = temperatures[i];
            while(!stack.isEmpty() && stack.peek()[0] < value) {
                Integer[] pair = stack.pop();
                temperatures[pair[1]] = i - pair[1];
            }

            stack.push(new Integer[] {value, i});
        }

        for(Integer[] pair : stack) {
            temperatures[pair[1]] = 0;
        }

        return temperatures;
    }

    public static void main(String[] args) {
        System.out.println(
            Arrays.toString(dailyTemperatures(new int[] {70, 73, 75, 71, 69, 72, 76, 73}))
        );

        System.out.println(
            Arrays.toString(dailyTemperatures(new int[] {73, 72, 71, 70}))
        );

        System.out.println(
           Arrays.toString(dailyTemperatures(new int[] {70, 71, 72, 73}))
        );
    }

}