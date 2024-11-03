import java.util.Stack;

/**
 * Pattern:- Monotonic Stack
 */
public class RemoveKDigitsToSmallest {
    
    public static String removeKdigits(String num, int k) {
        Stack<Character> stack = new Stack<>();
        for(char c: num.toCharArray()) {
            while(!stack.isEmpty() && k > 0 && Character.getNumericValue(c) < Character.getNumericValue(stack.peek())) {
                stack.pop();
                k--;
            }

            stack.push(c);
        }

        for(int i = 0; i < k; i++) {
            stack.pop();
        }

        StringBuilder builder = new StringBuilder();
        for(char c : stack) {
            builder.append(c);
        }

        while(builder.length() > 1 && builder.charAt(0) == '0') {
            builder.deleteCharAt(0);
        }

        return builder.length() == 0 ? "0" : builder.toString();
    }

    public static void main(String[] args) {
        System.out.println(
            removeKdigits("1432219", 3)
        );

        System.out.println(
            removeKdigits("10200", 1)
        );

        System.out.println(
            removeKdigits("1901042", 4)
        );
    }
}
