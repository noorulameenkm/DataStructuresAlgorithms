public class SubArraysWithOnesAfterReplacement {

    public static int findLength(int[] arr, int k) {
        int maxLength = 0;
        int zeros = 0;
        int start = 0;
        for(int end = 0; end < arr.length; end++) {
          zeros += arr[end] == 0 ? 1 : 0;
  
          while(zeros > k) {
            if(arr[start] == 0) {
              zeros --;
            }
  
            start++;
          }
  
          maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength;
      }


      public static void main(String[] args) {
        System.out.println(
            findLength(new int[]{0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1}, 2)
        );

        System.out.println(
            findLength(new int[]{0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1}, 3)
        );

        System.out.println(
            findLength(new int[]{1, 0, 0, 1, 1, 0, 1, 1}, 2)
        );
      }
}