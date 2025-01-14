import java.util.Arrays;

public class PrefixCommonArrayOfTwoArrays {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] frequency = new int[n + 1];
        int[] result = new int[n];
        Arrays.fill(frequency, 0);
        Arrays.fill(result, 0);

        int previousCount = 0;
        for(int i = 0; i < n; i++) {
            int currentCount = 0;

            frequency[A[i]]++;

            if(frequency[A[i]] == 2) {
                currentCount++;
            }

            frequency[B[i]]++;
            if(frequency[B[i]] == 2) {
                currentCount++;
            }
            
            result[i] = previousCount + currentCount;
            previousCount = result[i];
        }

        return result;
    }

    public static void main(String[] args) {
        PrefixCommonArrayOfTwoArrays solution = new PrefixCommonArrayOfTwoArrays();
        System.out.println(Arrays.toString(solution.findThePrefixCommonArray(new int[]{1,3,2,4}, new int[]{3,1,2,4})));
        System.out.println(Arrays.toString(solution.findThePrefixCommonArray(new int[]{2,3,1}, new int[]{3,1,2})));
    }
}