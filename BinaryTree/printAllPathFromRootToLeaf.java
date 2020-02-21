import java.util.ArrayList;
import java.util.List;

public class printAllPathFromRootToLeaf {
    public static void main(String[] args) {
        Node root = new Node(10);
        root.left = new Node(2);
        root.right = new Node(4);
        root.left.left = new Node(5);
        root.left.right = new Node(6);
        root.right.left = new Node(11);
        root.right.right = new Node(12);
        root.left.left.left = new Node(21);
        root.left.left.right = new Node(20);

        LinkedList list = new LinkedList();
        list.root = root;

        int[] path = new int[50];
        List<Integer> pathList = new ArrayList<>();

        list.rootToLeafPath(list.root, path, 0);
        System.out.println("Paths From ArrayList");
        list.rootToLeafPathsList(list.root, pathList, 0);
    }

}


class LinkedList {
    Node root;
    LinkedList(){
        this.root = null;
    }

    public void rootToLeafPath(Node root, int[] path, int pathLength){
        if(root == null){
            return;
        }
        
        
        path[pathLength] = root.data;
        pathLength++;

        if(root.left == null && root.right == null){
            printPath(path, pathLength);
        } else {
            if(root.left != null)
            rootToLeafPath(root.left, path, pathLength);
            if(root.right != null)
            rootToLeafPath(root.right, path, pathLength);
        }
    }

    public void rootToLeafPathsList(Node root, List<Integer> path, int pathLength){
        if(root == null){
            return;
        }

        path.add(pathLength, root.data);
        pathLength++;

        if(root.left == null && root.right == null){
            printAllPathFromRootToLeafList(path, pathLength);
        }
        else{
            if(root.left != null){
                rootToLeafPathsList(root.left, path, pathLength);
            }
    
            if(root.right != null){
                rootToLeafPathsList(root.right, path, pathLength);
            }
        }
        
    }

    private static void printAllPathFromRootToLeafList(List<Integer> path, int length) {
        System.out.println("New Path List");
        int i = 0;
        for(;i < length; i++){
            System.out.print(path.get(i) + " ");
        }

        System.out.print("\n");
    }

    private static void printPath(int[] path, int pathLength){
        System.out.println("New Path");
        for(int i = 0; i < pathLength; i++){
            System.out.print(path[i] + " ");
        }

        System.out.print("\n");
    }
}

class Node {
    int data;
    Node left, right;

    Node(int data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
}