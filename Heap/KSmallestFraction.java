package Heap;

import java.util.Arrays;
import java.util.PriorityQueue;

public class KSmallestFraction {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> {
                double fractionA = (double) a[0] / a[1];
                double fractionB = (double) b[0] / b[1];

                if(fractionA > fractionB) return -1;
                if(fractionA < fractionB) return 1;
                return 0;
            }
        );

        int n = arr.length;
        for(int i = 0; i < n - 1; i++) {
            for(int j = i + 1; j < n; j++) {
                pq.offer(new int[]{arr[i], arr[j]});

                if(pq.size() > k) {
                    pq.poll();
                }
            }
        }

        return pq.size() > 0 ? pq.poll() : new int[]{-1, -1};
    }

    public int[] kthSmallestPrimeFractionUsingMinHeap(int[] arr, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> {
                double fractionA = (double) arr[a[0]] / arr[a[1]];
                double fractionB = (double) arr[b[0]] / arr[b[1]];

                if(fractionA < fractionB) return -1;
                if(fractionA > fractionB) return 1;
                return 0;
            }
        );

        for(int i = 0; i < arr.length - 1; i++) {
            pq.offer(new int[]{i, arr.length - 1});
        }

        for(int i = 0; i < k - 1; i++) {
            int[] top = pq.poll();
            int ni = top[0];
            int di = top[1];

            if(di - 1 > ni) {
                pq.offer(new int[]{ni, di - 1});
            }
        }

        return new int[]{arr[pq.peek()[0]], arr[pq.peek()[1]]};
    }

    public static void main(String[] args) {
        KSmallestFraction ksf = new KSmallestFraction();
        System.out.println(
            Arrays.toString(
                ksf.kthSmallestPrimeFraction(new int[]{1, 3, 5}, 3)
            )
        );

        System.out.println(
            Arrays.toString(
                ksf.kthSmallestPrimeFraction(new int[]{1, 3, 7, 11, 13}, 5)
            )
        );

        System.out.println(
            Arrays.toString(
                ksf.kthSmallestPrimeFraction(new int[]{1, 5, 7, 23}, 2)
            )
        );

        System.out.println(
            Arrays.toString(
                ksf.kthSmallestPrimeFractionUsingMinHeap(new int[]{1, 3, 5}, 3)
            )
        );

        System.out.println(
            Arrays.toString(
                ksf.kthSmallestPrimeFractionUsingMinHeap(new int[]{1, 3, 7, 11, 13}, 5)
            )
        );

        System.out.println(
            Arrays.toString(
                ksf.kthSmallestPrimeFractionUsingMinHeap(new int[]{1, 5, 7, 23}, 2)
            )
        );
    }
}
