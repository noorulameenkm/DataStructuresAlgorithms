public class NumberOFSubArraysWithOddSum {
    public int numOfSubarrays(int[] arr) {
        int[] prefixSum = new int[arr.length];

        int sum = 0;
        final int MOD = 1000000007;

        for(int i = 0; i < arr.length; i++) {
            sum += arr[i];
            prefixSum[i] = sum;
        }

        int oddCount = 0;
        int evenCount = 1;

        int totalCount = 0;

        for(int i = 0; i < arr.length; i++) {
            if(prefixSum[i] % 2 == 1) {
                totalCount = (totalCount + evenCount) % MOD;
                oddCount++;
            } else {
                totalCount = (totalCount + oddCount) % MOD;
                evenCount++;
            }
        }

        return totalCount;
    }

    public static void main(String[] args) {
        NumberOFSubArraysWithOddSum obj = new NumberOFSubArraysWithOddSum();
        System.out.println(obj.numOfSubarrays(new int[]{1, 3, 5}));
        System.out.println(obj.numOfSubarrays(new int[]{2, 4, 6}));
        System.out.println(obj.numOfSubarrays(new int[]{1, 2, 3, 4, 5, 6, 7}));
    }
}
