import java.util.List;

record Input(int[] nums, int k) {}

public class CountNiceSubArrays {
    public int numberOfSubarrays(int[] nums, int k) {
        int count = 0, start = 0, kCount = 0, middle = 0;
        for(int end = 0; end < nums.length; end++) {
            if(nums[end] % 2 == 1){
                kCount += 1;
            }

            while(kCount > k) {
                if(nums[start] % 2 == 1) {
                    kCount -= 1;
                }

                start += 1;
                middle = start;
            }

            if(kCount == k){
                while(nums[middle] % 2 == 0) {
                    middle += 1;
                }

                count += (middle - start + 1);
            }
        }

        return count;
    }


    public static void main(String[] args) {
        CountNiceSubArrays countNiceSubArrays = new CountNiceSubArrays();
        List.of(
            new Input(new int[] {1,1,2,1,1}, 3),
            new Input(new int[] {2,4,6}, 1),
            new Input(new int[] {2,2,2,1,2,2,1,2,2,2}, 2)
        ).forEach((input) -> {
            System.out.println(countNiceSubArrays.numberOfSubarrays(input.nums(), input.k()));
        });
    }
}
