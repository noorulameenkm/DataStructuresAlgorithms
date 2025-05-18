package SortedSet;

import java.util.Stack;
import java.util.TreeSet;


public class OneThreeTwoPattern {

    
    // Time Complexity: O(nlogn)
    // Space Complexity: O(n) 
    // Sorted set insertion takes O(logn) time and we are inserting n elements in the set.
    public boolean find132pattern(int[] nums) {
        int n = nums.length;
        TreeSet<Integer> second = new TreeSet<>();
        Stack<Integer> st = new Stack<>();

        for(int i = n - 1; i >= 0; i--) {
            while(!st.isEmpty() && nums[i] > st.peek()) {
                second.add(st.pop());
            }

            if(!st.isEmpty() && !second.isEmpty()) {
                Integer num = second.higher(nums[i]);
                if(num != null) return true;
            }

            st.push(nums[i]);
        }

        return false; 
    }

    // Time Complexity: O(n)
    public boolean find132patternApproachTwo(int[] nums) {
        int n = nums.length;

        int z = Integer.MIN_VALUE;
        Stack<Integer> st = new Stack<>();

        for(int i = n - 1; i >= 0; i--) {
            if(nums[i] < z) return true;

            while(!st.isEmpty() && nums[i] > st.peek()) {
                z = st.pop();
            }

            st.push(nums[i]);
        }

        return false;
    }

    public static void main(String[] args) {
        OneThreeTwoPattern obj = new OneThreeTwoPattern();

        System.out.println(obj.find132pattern(new int[]{3, 5, 0, 3, 4})); // false
        System.out.println(obj.find132pattern(new int[]{1, 2, 3, 4})); // false
        System.out.println(obj.find132pattern(new int[]{9, 11, 8, 9, 10, 7, 9})); // true

        System.out.println(obj.find132patternApproachTwo(new int[]{3, 5, 0, 3, 4})); // false
        System.out.println(obj.find132patternApproachTwo(new int[]{1, 2, 3, 4})); // false
        System.out.println(obj.find132patternApproachTwo(new int[]{9, 11, 8, 9, 10, 7, 9})); // true
    }
}