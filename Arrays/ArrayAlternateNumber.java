import java.util.Scanner;

public class ArrayAlternateNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] result = new int[N];
        result = fillTheArray(N);
        for(int k : result){
            System.out.print(k + " ");
        }
        System.out.print("\n");
        sc.close();
    }

    static int[] fillTheArray(int N){
        
        /*
            intput N = 9
            values = 1 2 3 4 5 6 7 8 9
            output = 1 3 5 7 9 8 6 4 2
        */
        int[] result = new int[N];
        int i = 1, length = result.length, k = 0, m = length - 1;
        while(k <= m) {
            if(i % 2 == 0){
                result[m] = i;
                m--;
            } else {
                result[k] = i;
                k++;
            }

            i++;
        }

        return result;
    }
}