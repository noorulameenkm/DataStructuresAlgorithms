public class PunishementNumber {

    public int punishmentNumber(int n) {
        int result = 0;

        for(int num = 1; num <= n; num++) {
            int square = num * num;
            String squareString = String.valueOf(square);
            if(checkSumPossible(squareString, num, 0, 0)) {
                result += square;
            }
        }

        return result;
    }

    boolean checkSumPossible(String square, int number, int index, int sum) {
        if(index == square.length()) return sum == number;

        if(sum > number) return false;

        for(int j = index; j < square.length(); j++) {
            String substring = square.substring(index,  j + 1);
            if(checkSumPossible(square, number, j + 1, sum + Integer.valueOf(substring))) {
                return true;
            }
        }

        return false;
    }

    public int punishmentNumberUsingModulo(int n) {
        int result = 0;

        for(int num = 1; num <= n; num++) {
            int square = num * num;

            if(check(square, 0, num)) {
                result += square;
            }

        }

        return result;
    }

    boolean check(int num, int currSum, int lookup) {
        if(lookup == currSum && num == 0) return true;

        if(currSum > lookup || num == 0) return false;

        return check(num / 10, currSum + (num % 10), lookup) || check(num / 100, currSum + (num % 100), lookup) || check(num / 1000, currSum + (num % 1000), lookup) || check(num / 10000, currSum + (num % 10000), lookup);
    }

    public static void main(String[] args) {
        PunishementNumber punishementNumber = new PunishementNumber();
        System.out.println(punishementNumber.punishmentNumber(10));
        System.out.println(punishementNumber.punishmentNumber(36));

        System.out.println(punishementNumber.punishmentNumberUsingModulo(10));
        System.out.println(punishementNumber.punishmentNumberUsingModulo(36));
    }
}