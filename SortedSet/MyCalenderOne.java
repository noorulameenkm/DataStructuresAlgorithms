package SortedSet;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

public class MyCalenderOne {
    public static List<Boolean> book(int[][] nums) {
        List<Boolean> results = new ArrayList<>();
        if(nums.length == 0) return results;
        TreeSet<int[]> sortedSet = new TreeSet<>((a, b) -> a[0] - b[0]);
        
        for(int[] num: nums) {
            int start = num[0];
            int end = num[1];
            int[] event = new int[]{start, end};
            int[] lower = sortedSet.lower(event);
            int[] higher = sortedSet.higher(event);

            if((lower == null || start >= lower[1]) && (higher == null || end <= higher[0])) {
                results.add(true);
                sortedSet.add(event);
            } else {
                results.add(false);
            }
        }
        return results;
    }

    public static void main(String[] args) {
       int[][] nums = new int[][]{{15, 20}, {10, 15}, {20, 25}};
       System.out.println(book(nums)); // [true, true, true]
    }
}
