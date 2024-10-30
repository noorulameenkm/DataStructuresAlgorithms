
/**
 * Patter:- Divide and Conquore
 */
public class MajorityElement {

    public static int findMajority(int[] arr) {
        return majorityElement(arr, 0, arr.length - 1);
    }

    private static int majorityElement(int[] arr, int start, int end) {

        if(start == end) {
            return arr[start];
        }

        int mid = start + (end - start) / 2;

        int leftMajority = majorityElement(arr, start, mid);
        int rightMajority = majorityElement(arr, mid + 1, end);

        if(leftMajority == rightMajority) return leftMajority;

        int leftMajorityCount = countOccurence(arr, leftMajority, start, end);
        int rightMajorityCount = countOccurence(arr, rightMajority, start, end);

        return leftMajorityCount > rightMajorityCount ? leftMajority : rightMajority;

    }


    private static int countOccurence(int[] arr, int element, int start, int end) {
        int count = 0;
        for(int i = start; i <= end; i++) {
            count += arr[i] == element ? 1 : 0;
        }

        return count;
    }


    public static void main(String[] args) {
        System.out.println(
            findMajority(new int[]{1, 2, 2, 3, 2})
        );

        System.out.println(
            findMajority(new int[]{4, 4, 4, 4, 7, 4, 4})
        );

        System.out.println(
            findMajority(new int[]{9, 9, 1, 1, 9, 1, 9, 9})
        );
    }
}