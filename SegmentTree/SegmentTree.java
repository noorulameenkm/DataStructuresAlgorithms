package SegmentTree;

public class SegmentTree {
    
    int[] originalArray;
    int[] tree;
    public SegmentTree(int[] originalArray) {
        this.originalArray =  originalArray;
        tree = new int[4 * originalArray.length];
    }

    public void buildTree() {
        buildTree(0, 0, originalArray.length - 1);
    }

    private void buildTree(int treeIndex, int start, int end) {
        if(start == end) {
            tree[treeIndex] = originalArray[start];
            return;
        }

        int mid = start + (end - start) / 2;
        buildTree(2 * treeIndex + 1, start, mid);
        buildTree(2 * treeIndex + 2, mid + 1, end);

        tree[treeIndex] = tree[2 * treeIndex + 1] + tree[2 * treeIndex + 2];
    }

    public int getRangeSum(int left, int right) {
        return getRangeSum(0, originalArray.length - 1, left, right, 0);
    }

    private int getRangeSum(int start, int end, int left, int right, int treeIndex) {
        // I represent ths sum for the index [start, end]
        // If current node's end is less than start of search or
        // if the current node's start is greater than the end
        // the current node is out of range
        if(end < left || start > right) return 0;

        if(start >= left && end <= right) return tree[treeIndex];

        int mid = start + (end - start) / 2;
        return getRangeSum(start, mid, left, right, 2 * treeIndex + 1) +
                getRangeSum(mid + 1, end, left, right, 2 * treeIndex + 2);
    }

    public static void main(String[] args) {
        SegmentTree segmentTree = new SegmentTree(new int[]{1, 2, 3, 4});
        segmentTree.buildTree();

        System.out.println(segmentTree.getRangeSum(0, 3));
        System.out.println(segmentTree.getRangeSum(1, 2));
        System.out.println(segmentTree.getRangeSum(2, 2));
        System.out.println(segmentTree.getRangeSum(2, 3));
    }
}
