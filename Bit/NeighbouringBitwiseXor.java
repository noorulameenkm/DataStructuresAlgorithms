package Bit;

import java.util.Arrays;

public class NeighbouringBitwiseXor {
    public boolean doesValidArrayExist(int[] derived) {
        int n = derived.length;
        int[] original = new int[n];

        Arrays.fill(original, 0);
        original[0] = 0;

        fillArray(derived, original);

        if((original[n - 1] ^ original[0]) == derived[n - 1]) {
            return true;
        }

        Arrays.fill(original, 0);
        original[0] = 1;

        fillArray(derived, original);
        if((original[n - 1] ^ original[0]) == derived[n - 1]) {
            return true;
        }

        return false;
    }

    private void fillArray(int[] derived, int[] original) {
        for(int i = 1; i < derived.length; i++) {
            original[i] = derived[i - 1] ^ original[i -1];
        }
    }

    public boolean doesValidArrayExist2(int[] derived) {
        int result = 0;
        int n = derived.length;
        for(int i = 0; i < n; i++) {
            result = result ^ derived[i];
        }

        return result == 0 ? true : false;
    }

    public static void main(String[] args) {
        NeighbouringBitwiseXor solution = new NeighbouringBitwiseXor();
        System.out.println(solution.doesValidArrayExist(new int[]{1,1,0}));
        System.out.println(solution.doesValidArrayExist(new int[]{1,1}));
        System.out.println(solution.doesValidArrayExist(new int[]{1,0}));

        System.out.println(solution.doesValidArrayExist2(new int[]{1,1,0}));
        System.out.println(solution.doesValidArrayExist2(new int[]{1,1}));
        System.out.println(solution.doesValidArrayExist2(new int[]{1,0}));
    }
}
