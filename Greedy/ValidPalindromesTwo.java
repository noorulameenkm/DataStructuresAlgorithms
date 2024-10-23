package Greedy;

public class ValidPalindromesTwo {

    public static void main(String[] args) {
        
        System.out.println(
            isPalindromePossible("racecar")
        );

        System.out.println(
            isPalindromePossible(
                "abccdba"
            )
        );

        System.out.println(
            isPalindromePossible(
                "abcdef"
            )
        );
    }

    private static boolean isPalindromePossible(String str) {
        // ToDo: Write Your Code Here.
        int i = 0;
        int j = str.length() - 1;
        int countDiff = 0;
        while(i < j) {
            if(str.charAt(i) != str.charAt(j)) {
                return isPalindrome(str, i, j - 1) || isPalindrome(str, i + 1, j);
            }

            i ++;
            j --;
        }

        return countDiff <= 1; 
    }

    static boolean isPalindrome(String str, int start, int end) {
        while (start < end) {
            if(str.charAt(start) != str.charAt(end)) {
                return false;
            }

            start ++;
            end --;
        }

        return true;
    }
    
}
