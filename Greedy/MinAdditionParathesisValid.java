package Greedy;

public class MinAdditionParathesisValid {

    public static void main(String[] args) {
        System.out.println(
            minAddToMakeValid(
              "(()"  
            )
        );

        System.out.println(
            minAddToMakeValid(
              "))(("
            )
        );

        System.out.println(
            minAddToMakeValid(
              "(()())("
            )
        );
    }

    private static int minAddToMakeValid(String S) {
        // ToDO: Write Your Code Here.
        int counter = 0, balance = 0;
        for(char c: S.toCharArray()) {
            balance += c == '(' ? 1 : -1;
            if(balance == -1) {
                balance++;
                counter++;
            }
        }

        return counter + balance;
    }
}
