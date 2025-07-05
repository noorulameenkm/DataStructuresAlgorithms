public class RemoveElementExceptKey {

    private static int removeExceptKey(int[] nums, int key) {
        int replaceAt = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != key) {
                nums[replaceAt] = nums[i];
                replaceAt++;
            }
        }

        return replaceAt;
    }

    public static void main(String[] args) {
        System.out.println(
            removeExceptKey(new int[]{3, 2, 3, 6, 3, 10, 9, 3}, 3)
        );

        System.out.println(
            removeExceptKey(new int[]{2, 11, 2, 2, 1}, 2)
        );
    }
}
