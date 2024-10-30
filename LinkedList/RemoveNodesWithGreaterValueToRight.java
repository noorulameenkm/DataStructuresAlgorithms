import java.util.Stack;

/**
 * Pattern:- Monotonic stack
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) {
        this.val = val;
    }
}

public class RemoveNodesWithGreaterValueToRight {

    public static ListNode removeNodes(ListNode head) {
        Stack<ListNode> stack = new Stack<>();
        ListNode current = head;
        while(current != null) {
            while (!stack.isEmpty() && current.val > stack.peek().val)
                stack.pop();

            if(!stack.isEmpty())
                stack.peek().next = current;

            stack.push(current);

            current = current.next;
        }

       return stack.isEmpty() ? null : stack.get(0);
    }


    public static void main(String[] args) {
        // Creating the linked list 5 -> 3 -> 7 -> 4 -> 5 -> 2 -> 1
        ListNode head1 = new ListNode(5);
        head1.next = new ListNode(3);
        head1.next.next = new ListNode(7);
        head1.next.next.next = new ListNode(4);
        head1.next.next.next.next = new ListNode(5);
        head1.next.next.next.next.next = new ListNode(2);
        head1.next.next.next.next.next.next = new ListNode(1);
        head1 = removeNodes(head1);

        // Printing the modified list: 7 -> 5 -> 2 -> 1
        ListNode node = head1;
        while (node != null) {
            System.out.print(node.val);
            if (node.next != null) {
                System.out.print(" -> ");
            }
            node = node.next;
        }
    }
    
}
