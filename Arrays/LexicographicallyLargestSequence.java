import java.util.Arrays;

public class LexicographicallyLargestSequence {
    public int[] constructDistancedSequence(int n) {
        if(n == 1) return new int[]{1};

        int numberOfElements = n * 2 - 1;
        int[] results = new int[numberOfElements];
        int[] counter = new int[n + 1];
        Arrays.fill(counter, 2);
        counter[1] = 1;
        Arrays.fill(results, -1);

        int currentIndex = 0;

        fill(results, n, currentIndex, counter);

        return results;
    }

    boolean fill(int[] results, int n, int currentIndex, int[] counter) {
        if(currentIndex == results.length) return true;

        if(results[currentIndex] != -1) {
            return fill(results, n, currentIndex + 1, counter);
        }

        for(int k = n; k > 0; k--) {
            if(counter[k] > 0) {
                results[currentIndex] = k;
                counter[k]--;

                if(k == 1) {
                    if(fill(results, n, currentIndex + 1, counter)) {
                        return true;
                    }
                } else {
                    int nextIndex = results[currentIndex] + currentIndex;
                    if(nextIndex < results.length && results[nextIndex] == -1) {
                        results[nextIndex] = k;
                        counter[k]--;
                        if(fill(results, n, currentIndex + 1, counter)) {
                            return true;
                        }

                        results[nextIndex] = -1;
                        counter[k]++;
                    }
                }

                results[currentIndex] = -1;
                counter[k]++;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        LexicographicallyLargestSequence obj = new LexicographicallyLargestSequence();
        System.out.println(
            Arrays.toString(obj.constructDistancedSequence(3))
        );

        System.out.println(
            Arrays.toString(obj.constructDistancedSequence(20))
        );
    }
}
