public class PseudoPalindromicPaths {
    public int pseudoPalindromicPaths(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode root, int path) {
        if(root == null)
            return 0;
        
        path ^= 1 << root.val;

        if(root.left == null && root.right == null) {
            return (path & (path - 1)) == 0 ? 1 : 0;
        }

        int palindromes = 0;
        palindromes += dfs(root.left, path);
        palindromes += dfs(root.right, path);
        return palindromes;
    }

    public static void main(String[] args) {
        PseudoPalindromicPaths sol = new PseudoPalindromicPaths();
        
        // Example 1
        TreeNode root1 = new TreeNode(5);
        root1.left = new TreeNode(4);
        root1.right = new TreeNode(1);
        root1.left.left = new TreeNode(4);
        root1.left.right = new TreeNode(1);
        root1.right.right = new TreeNode(1);
        System.out.println(sol.pseudoPalindromicPaths(root1));  // Output: 2

        // Example 2
        TreeNode root2 = new TreeNode(2);
        root2.left = new TreeNode(3);
        root2.right = new TreeNode(1);
        root2.left.left = new TreeNode(3);
        root2.right.left = new TreeNode(1);
        root2.right.right = new TreeNode(1);
        System.out.println(sol.pseudoPalindromicPaths(root2));  // Output: 3

        // Example 3
        TreeNode root3 = new TreeNode(9);
        root3.left = new TreeNode(5);
        root3.right = new TreeNode(5);
        root3.left.left = new TreeNode(5);
        root3.right.left = new TreeNode(1);
        root3.right.right = new TreeNode(7);
        System.out.println(sol.pseudoPalindromicPaths(root3));  // Output: 1
    }
}
