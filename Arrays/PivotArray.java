import java.util.Arrays;

public class PivotArray {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] result = new int[nums.length];

        int i = 0, j = nums.length - 1;

        int i_ = 0, j_ = nums.length - 1;

        while(i < nums.length && j >= 0) {
            if(nums[i] < pivot) {
                result[i_] = nums[i];
                i_++;
            }

            if(nums[j] > pivot) {
                result[j_] = nums[j];
                j_--;
            }

            i++;
            j--;
        }

        while(i_ <= j_) {
            result[i_] = pivot;
            i_++;
        }

        return result;
    }

    public static void main(String[] args) {
        PivotArray obj = new PivotArray();

        System.out.println(Arrays.toString(obj.pivotArray(new int[]{9, 12, 3, 5, 14, 10, 10}, 10)));
        System.out.println(Arrays.toString(obj.pivotArray(new int[]{-3,4,3,2}, 2)));
    }
}
