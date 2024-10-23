package Greedy;

import java.util.Arrays;

public class LongestChain {

    public static void main(String[] args) {

        System.out.println(
            findLongestChain(
                new int[][] {
                    {1, 2},
                    {3, 4},
                    {2, 3}
                }
            )
        );

        System.out.println(
            findLongestChain(
                new int[][] {
                    {5, 6},
                    {1, 2},
                    {8, 9},
                    {2, 3}
                }
            )
        );

        System.out.println(
            findLongestChain(
                new int[][] {
                    {7, 8},
                    {5, 6},
                    {1, 2},
                    {3, 5},
                    {4, 5},
                    {2, 3}
                }
            )
        );
    }

    private static int findLongestChain(int[][] pairs) {
         Arrays.sort(pairs, (a, b) -> a[1] - b[1]);
        int chainCount = 0;
        int currentEnd = Integer.MIN_VALUE;

        for(int[] pair : pairs) {
            if(pair[0] > currentEnd) {
                chainCount ++;
                currentEnd = pair[1];
            }
        }

        return chainCount;
    }
    
}