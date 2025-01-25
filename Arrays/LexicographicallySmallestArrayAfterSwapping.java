import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;

public class LexicographicallySmallestArrayAfterSwapping {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int[] sortedArray = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sortedArray);
        Map<Integer, Integer> numToGroup = new HashMap<>();
        Map<Integer, Queue<Integer>> groupToNums = new HashMap<>();

        int groupNum = 0;
        numToGroup.put(sortedArray[0], groupNum);
        groupToNums.computeIfAbsent(groupNum, k -> new ArrayDeque<>())
            .offer(sortedArray[0]);

        for(int i = 1; i < sortedArray.length; i++) {
            if(Math.abs(sortedArray[i] - sortedArray[i - 1]) > limit) groupNum++;

            numToGroup.put(sortedArray[i], groupNum);
            groupToNums.computeIfAbsent(groupNum, k -> new ArrayDeque<>())
                .offer(sortedArray[i]);
        }

        int[] result = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int group = numToGroup.get(num);
            result[i] = groupToNums.get(group).poll();
        }

        return result;
    }

    public static void main(String[] args) {
        LexicographicallySmallestArrayAfterSwapping sol = new LexicographicallySmallestArrayAfterSwapping();

        System.out.println(
            Arrays.toString(
                sol.lexicographicallySmallestArray(
                    new int[]{1,5,3,9,8},
                    2
                )
            )
        );

        System.out.println(
            Arrays.toString(
                sol.lexicographicallySmallestArray(
                    new int[]{1,7,6,18,2,1},
                    3
                )
            )
        );

        System.out.println(
            Arrays.toString(
                sol.lexicographicallySmallestArray(
                    new int[]{1,7,28,19,10},
                    3
                )
            )
        );
    }
}
