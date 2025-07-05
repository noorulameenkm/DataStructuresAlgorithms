public class FindNonDuplicateArrayLength {

    public static int moveElements(int[] arr) {
        int replaceElemenAt = 1;
        for(int i = 1; i < arr.length; i++) {
          if(arr[i] != arr[replaceElemenAt - 1]) {
            arr[replaceElemenAt] = arr[i];
            replaceElemenAt++;
          }
        }
    
        return replaceElemenAt;
      }

    public static void main(String[] args) {
        System.out.println(
            moveElements(new int[]{2, 3, 3, 3, 6, 9, 9})
        );

        System.out.println(
            moveElements(new int[]{2, 2, 2, 11})
        );
    }
}
