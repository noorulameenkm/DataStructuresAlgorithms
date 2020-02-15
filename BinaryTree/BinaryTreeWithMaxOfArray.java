public class BinaryTreeWithMaxOfArray {
    public static void main(String[] args) {
        int[] nodes = {1, 2, 5, 9, 6, 3 };
        int length = nodes.length;
        Node head;
        int i, max_ = 0, max_index = 0;
        for(i = 0; i < length; i++){
            if(nodes[i] > max_){
                max_ = nodes[i];
                max_index = i;
            }
        }

        head = new Node(max_);
        head.left = constructTreeFromArray(nodes, 0, max_index);
        head.right = constructTreeFromArray(nodes, max_index + 1, length);
        printTree(head);
        System.out.print("\n");
    }

    static Node constructTreeFromArray(int[] nodes, int start, int end){
        int length = nodes.length;
        if(start > length || end > length || start < 0 || end < 0 || start == end){
            return null;
        }

        Node head;
        int i, max_ = -1, max_index = -1;
        for(i = start; i < end; i++){
            if(nodes[i] > max_){
                max_ = nodes[i];
                max_index = i;
            }
        }

        head = new Node(max_);
        head.left = constructTreeFromArray(nodes,start, max_index);
        head.right = constructTreeFromArray(nodes, max_index + 1, end);
        
        return head;
    }

    static void printTree(Node head){
        if(head != null){
            System.out.print(head.data + " ");
            printTree(head.left);
            printTree(head.right);
        }
    }
}



class Node {

    int data;
    Node left;
    Node right;

    Node(int n){
        this.data = n;
        this.left = null;
        this.right = null;
    }
}