import java.util.Stack;

/**
 * Pattern:- Monotonic Stack
 */
record Pair(char character, int count){};

public class RemoveAdjacentKCharacters {
    
    public static String removeDuplicates(String s, int k) {
        Stack<Pair> stack = new Stack<>();
        for(char c : s.toCharArray()) {
            if(!stack.isEmpty() && stack.peek().character() == c) {
                Pair pair = stack.pop();
                Pair updatedPair = new Pair(pair.character(), pair.count() + 1);
                if(updatedPair.count() < k) {
                    stack.push(updatedPair);
                }
            } else {
                stack.push(new Pair(c, 1));
            }
        }

        StringBuilder builder = new StringBuilder();
        for(Pair pair : stack) {
            for(int i = 0; i < pair.count(); i++) {
                builder.append(pair.character());
            }
        }

        return builder.toString();
    }


    public static void main(String[] args) {
        System.out.println(
            removeDuplicates("abbbaaca", 3)
        );

        System.out.println(
            removeDuplicates("abbaccaa", 3)
        );

        System.out.println(
            removeDuplicates("abbacccaa", 3)
        );
    }
}
