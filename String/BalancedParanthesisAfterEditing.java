import java.util.Stack;

public class BalancedParanthesisAfterEditing {
    public boolean canBeValid(String s, String locked) {
        Stack<Integer> open = new Stack<>();
        Stack<Integer> openAndClose = new Stack<>();
        if(s.length() % 2 != 0) return false;

        for(int i = 0; i < s.length(); i++) {

            if(locked.charAt(i) == '0') {
                openAndClose.push(i);
            } else if(s.charAt(i) == '(') {
                open.push(i);
            } else {
                if(!open.isEmpty()) {
                    open.pop();
                } else if(!openAndClose.isEmpty()) {
                    openAndClose.pop();
                } else {
                    return false;
                }
            }
        }

        while(!open.isEmpty() && !openAndClose.isEmpty() && open.peek() < openAndClose.peek()) {
            open.pop();
            openAndClose.pop();
        }


        return open.isEmpty();
    }

    public boolean canBeValid2(String s, String locked) {
        if(s.length() % 2 != 0) {
            return false;
        }

        int open = 0;
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '(' || locked.charAt(i) == '0') open++;
            else open--;

            if(open < 0) return false;
        }

        int close = 0;
        for(int i = s.length() - 1; i >= 0; i--) {
            if(s.charAt(i) == ')' || locked.charAt(i) == '0') close++;
            else close--;

            if(close < 0) return false;
        }

        return true;
    }

    public static void main(String[] args) {
        BalancedParanthesisAfterEditing b = new BalancedParanthesisAfterEditing();
        System.out.println(b.canBeValid("))()))", "010100"));
        System.out.println(b.canBeValid("()()", "0000"));
        System.out.println(b.canBeValid(")", "0"));

        System.out.println(b.canBeValid2("))()))", "010100"));
        System.out.println(b.canBeValid2("()()", "0000"));
        System.out.println(b.canBeValid2(")", "0"));
    }
}
