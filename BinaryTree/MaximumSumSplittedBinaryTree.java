/**
 * MaximumSumSplittedBinaryTree
 * 
 * problem Link -
 * https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class MaximumSumSplittedBinaryTree {

    public int maxProduct(TreeNode root) {
        long total = totalSum(root);
        int mod = 1_000_000_007;

        long[] answer = { 0 };

        findMaxProd(root, total, answer);

        return (int) (answer[0] % mod);
    }

    private static long totalSum(TreeNode root) {
        if (root == null)
            return 0;

        return root.val + totalSum(root.left) + totalSum(root.right);
    }

    private static long findMaxProd(TreeNode root, long totalSum, long[] answer) {
        if (root == null)
            return 0;

        long left = findMaxProd(root.left, totalSum, answer);
        long right = findMaxProd(root.right, totalSum, answer);

        long currentTreeSum = left + right + root.val;

        answer[0] = Math.max(answer[0], currentTreeSum * (totalSum - currentTreeSum));

        return currentTreeSum;
    }

    public static void main(String[] args) {
        MaximumSumSplittedBinaryTree soln = new MaximumSumSplittedBinaryTree();

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        root.right = new TreeNode(3);
        root.right.left = new TreeNode(6);

        int result = soln.maxProduct(root);

        System.out.println("Answer is " + result);
    }
}