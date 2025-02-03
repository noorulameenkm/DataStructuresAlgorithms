import java.util.Arrays;

public class CheckArraySortedRotated {
    public boolean check(int[] nums) {
        int[] sorted = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sorted);

        for(int i = 0; i < nums.length; i++) {
            if(checkEqual(sorted, nums, i)) return true;
        }

        return false;
    }

    private boolean checkEqual(int[] sorted, int[] original, int i) {
        for(int j = 0; j < sorted.length; j++) {
            int originalIndex = (j + i) % sorted.length;
            if(sorted[j] != original[originalIndex]) return false;
        }

        return true;
    }

    public boolean checkArraySortedAndRotated(int[] nums) {
        int points = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] > nums[(i + 1) % nums.length]) points++;
        }

        return points <= 1;
    }

    public static void main(String[] args) {
        CheckArraySortedRotated solution = new CheckArraySortedRotated();
        System.out.println(
            solution.check(new int[]{3, 4, 5, 1, 2})
        );

        System.out.println(
            solution.check(new int[]{2, 1, 3, 4})
        );

        System.out.println(
            solution
            .check(new int[]{1,2,3})
        );

        System.out.println(
            solution.checkArraySortedAndRotated(new int[]{3, 4, 5, 1, 2})
        );

        System.out.println(
            solution.checkArraySortedAndRotated(new int[]{2, 1, 3, 4})
        );

        System.out.println(
            solution
            .checkArraySortedAndRotated(new int[]{1,2,3})
        );
    }
}
