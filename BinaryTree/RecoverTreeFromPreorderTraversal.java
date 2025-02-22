public class RecoverTreeFromPreorderTraversal {
    int index;

    public TreeNode recoverFromPreorder(String traversal) {
        index = 0;

        int number = getNumber(traversal);
        TreeNode root = new TreeNode(number);

        buildTree(root, traversal, 1);

        return root;

    }

    private boolean buildTree(TreeNode node, String traversal, int currentLevel) {
        if (index == traversal.length())
            return true;
        int level = getLevel(traversal);
        if (level == currentLevel) {
            node.left = new TreeNode(getNumber(traversal));
            if (!buildTree(node.left, traversal, currentLevel + 1)) {
                int level2 = getLevel(traversal);
                if (level2 == currentLevel) {
                    node.right = new TreeNode(getNumber(traversal));
                    return buildTree(node.right, traversal, currentLevel + 1);
                } else {
                    index = index - level2;
                    return false;
                }
            }

            return true;
        } else {
            index = index - level;
            return false;
        }
    }

    private int getLevel(String traversal) {
        int count = 0;
        while (index < traversal.length() && traversal.charAt(index) == '-') {
            count++;
            index++;
        }

        return count;
    }

    private int getNumber(String traversal) {
        StringBuilder builder = new StringBuilder();
        while (index < traversal.length() && traversal.charAt(index) != '-') {
            builder.append(traversal.charAt(index));
            index++;
        }

        return Integer.parseInt(builder.toString());
    }
}
