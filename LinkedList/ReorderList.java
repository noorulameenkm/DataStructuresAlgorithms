import java.util.ArrayDeque;
import java.util.Deque;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class ReorderList {
    public void reorder(ListNode head) {
        Deque<ListNode> deque = new ArrayDeque<>();
        int length = 0;
        ListNode tempHead = head;
        while(tempHead != null) {
            length += 1;
            // Add the node to the queue
            deque.addFirst(tempHead);
            tempHead = tempHead.next;
        }

        int i = 1;
        ListNode node = null;
        ListNode current = head;
        deque.removeLast(); // remove the first element;
        while(i < length) {
            if(i % 2 == 0) {
                node = deque.removeLast();
                current.next = node;
            } else {
                node = deque.removeFirst();
                current.next = node;
            }

            current = current.next;
            i += 1;
        }

        current.next = null;
    }

    public void printList(ListNode head) {
        ListNode temp = head;
        while(temp != null) {
            System.out.print(temp.val);
            System.out.print(" ");
            temp = temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        ReorderList reorderList = new ReorderList();
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        reorderList.reorder(head);
        reorderList.printList(head);
    }
}