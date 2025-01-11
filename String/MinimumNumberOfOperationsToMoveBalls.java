import java.util.Arrays;

public class MinimumNumberOfOperationsToMoveBalls {
    public int[] minOperations(String boxes) {
        int n = boxes.length();
        int[] answer = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        Arrays.fill(answer, 0);
        Arrays.fill(left, 0);
        Arrays.fill(right, 0);

        int numberOfOnes = boxes.charAt(0) == '1' ? 1 : 0;
        for(int i = 1; i < n; i++) {
            left[i] = numberOfOnes + left[i - 1];

            char c = boxes.charAt(i);
            if(c == '1') numberOfOnes++;
        }

        numberOfOnes = boxes.charAt(n - 1) == '1' ? 1 : 0;
        for(int i = n - 2; i >= 0; i--) {
            right[i] = numberOfOnes + right[i + 1];

            char c = boxes.charAt(i);
            if(c == '1') numberOfOnes++;
        }

        for(int i = 0; i < n; i++) {
            answer[i] = left[i] + right[i];
        }

        return answer;
    }

    public static void main(String[] args) {
        MinimumNumberOfOperationsToMoveBalls obj = new MinimumNumberOfOperationsToMoveBalls();
        int[] answer = obj.minOperations("110");
        System.out.println(Arrays.toString(answer));
        System.out.println(Arrays.toString(obj.minOperations("001011")));
    }
}
