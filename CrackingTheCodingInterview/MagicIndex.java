public class MagicIndex {
    
    public int magicIndexDisctinct(int[] nums) {
        return recurseDisctinct(nums, 0, nums.length - 1);
    }

    private int recurseDisctinct(int[] nums, int start, int end) {
        if(end < start) return -1;

        int mid = start + (end - start) / 2;
        if(mid == nums[mid]) return mid;
        else if(nums[mid] > mid) return recurseDisctinct(nums, start, mid - 1);
        else return recurseDisctinct(nums, mid + 1, end);
    }

    public int magicIndex(int[] nums) {
        return recurse(nums, 0, nums.length - 1);
    }

    private int recurse(int[] nums, int start, int end) {
        if(end < start) return -1;

        int mid = start + (end - start) / 2;
        if(mid == nums[mid]) return mid;

        int left = recurse(nums, start, Math.min(mid - 1, nums[mid]));
        if(left >= 0) return left;
        return recurse(nums, Math.max(mid + 1, nums[mid]), end);
    }

    public static void main(String[] args) {
        MagicIndex magicIndex = new MagicIndex();
        int[] nums = new int[] {-40, -20, -1, 1, 2, 3, 5, 7, 9, 12};
        System.out.println(magicIndex.magicIndexDisctinct(nums));
        nums = new int[] {-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13};
        System.out.println(magicIndex.magicIndex(nums));
    }
}
