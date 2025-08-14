public class MaximumFruitHarvested {
    public int maxTotalFruits(int[][] fruits, int startPos, int k) {
        int[] prefixSum = new int[fruits.length];
        int sum = 0;
        for(int i = 0; i < fruits.length; i++) {
            sum += fruits[i][1];
            prefixSum[i] = sum;
        }

        int maxFruitsHarvested = 0;
        for(int d = 0; d <= k / 2; d++) {
            // travel d distance to the left
            int i = startPos - d;
            int j = startPos + (k - 2 * d);

            int left = lowerBound(fruits, i);
            int right = upperBound(fruits, j) - 1;

            if(left <= right) {
                int totalFruits = prefixSum[right] - (left > 0 ? prefixSum[left - 1] : 0);
                maxFruitsHarvested = Math.max(maxFruitsHarvested, totalFruits);
            }

            i = startPos - (k - 2 * d);
            j = startPos + d;

            left = lowerBound(fruits, i);
            right = upperBound(fruits, j) - 1;

            if(left <= right) {
                int totalFruits = prefixSum[right] - (left > 0 ? prefixSum[left - 1] : 0);
                maxFruitsHarvested = Math.max(maxFruitsHarvested, totalFruits);
            }
        }

        return maxFruitsHarvested;
    }

    private int lowerBound(int[][] fruits, int target) {
        int start = 0;
        int end = fruits.length - 1;

        while(start <= end) {
            int mid = start + (end - start) / 2;

            if(target > fruits[mid][0]) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }

        }

        return start;
    }

    private int upperBound(int[][] fruits, int target) {
        int start = 0;
        int end = fruits.length - 1;

        while(start <= end) {
            int mid = start + (end - start) / 2;

            if(target >= fruits[mid][0]) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return start;
    }
}