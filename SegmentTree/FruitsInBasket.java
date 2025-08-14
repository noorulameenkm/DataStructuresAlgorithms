class SegmentTree {
    int[] array;
    int[] tree;

    public SegmentTree(int[] array) {
        this.array = array;
        this.tree = new int[4 * array.length];
        this.buildTree(0, 0, array.length - 1);
    }

    private void buildTree(int index, int start, int end) {
        if(start == end) {
            tree[index] = array[start];
            return;
        }

        int mid = start + (end - start) / 2;
        buildTree(2 * index + 1, start, mid);
        buildTree(2 * index + 2, mid + 1, end);
        tree[index] = Math.max(tree[2 * index + 1], tree[2 * index + 2]);
    }

    public boolean canPlaceInBasket(int element) {
        return search(0, 0, array.length - 1, element);
    }

    private boolean search(int index, int start, int end, int element) {
        if(start == end) {
            if(tree[index] >= element) {
                tree[index] = -1;
                return true;
            }

            return false;
        }

        if(tree[index] < element) return false;
        
        int mid = start + (end - start) / 2;
        boolean isPresentInLeft = search(2 * index + 1, start, mid, element);
        boolean isPresentInRight = false;
        if(!isPresentInLeft) {
            isPresentInRight = search(2 * index + 2, mid + 1, end, element);
        }

        boolean isPresent = isPresentInLeft || isPresentInRight;
        if(isPresent) {
            tree[index] = Math.max(tree[2 * index + 1], tree[2 * index + 2]);
        }

        return isPresent;
    }
}


public class FruitsInBasket {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        SegmentTree segTree = new SegmentTree(baskets);
        int unplacedFruits = 0;
        for(int fruit : fruits) {
            if(!segTree.canPlaceInBasket(fruit)) {
                unplacedFruits++;
            }
        }

        return unplacedFruits;
    }

    public static void main(String[] args) {
        FruitsInBasket fruitsInBasket = new FruitsInBasket();
        System.out.println(fruitsInBasket.numOfUnplacedFruits(new int[]{4,2,5}, new int[] {3,5,4}));
        System.out.println(fruitsInBasket.numOfUnplacedFruits(new int[]{3,6,1}, new int[] {6,4,7}));
    }
}
