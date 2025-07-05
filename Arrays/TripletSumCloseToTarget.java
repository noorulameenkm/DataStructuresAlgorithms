import java.util.Arrays;

public class TripletSumCloseToTarget {
    public int searchTriplet(int[] arr, int targetSum) {
        if (arr == null || arr.length < 3)
            throw new IllegalArgumentException("Array is null or array size is less than 3");
        Arrays.sort(arr);
        int smallDifference = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length - 2; i++) {
            if (i > 0 && arr[i] == arr[i - 1])
                continue;

            int left = i + 1, right = arr.length - 1;
            while (left < right) {
                int sum = arr[i] + arr[left] + arr[right];
                int targetDifference = targetSum - sum;
                if (targetDifference == 0)
                    return sum;

                if (Math.abs(targetDifference) < Math.abs(smallDifference)) {
                    smallDifference = targetDifference;
                } else if (Math.abs(targetDifference) == Math.abs(smallDifference)
                        && targetDifference > smallDifference) {
                    smallDifference = targetDifference;
                }

                if (targetDifference > 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return targetSum - smallDifference;
    }

    public static void main(String[] args) {
        TripletSumCloseToTarget obj = new TripletSumCloseToTarget();
        System.out.println(obj.searchTriplet(new int[] { -1, 0, 2, 3 }, 3));
        System.out.println(obj.searchTriplet(new int[] { -3, -1, 1, 2 }, 1));
        System.out.println(obj.searchTriplet(new int[] { 1, 0, 1, 1 }, 100));
        System.out.println(obj.searchTriplet(new int[] { 0, 0, 1, 1, 2, 6 }, 5));
    }
}
