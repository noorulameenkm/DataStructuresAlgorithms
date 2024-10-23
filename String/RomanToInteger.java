
import java.util.Map;

public class RomanToInteger {

    public static void main(String[] args) {
        System.out.println(
            romanToInt("XLII")
        );

        System.out.println(
            romanToInt("CXCIV")
        );

        System.out.println(
            romanToInt("MMMCDXLIV")
        );
    }

    public static int romanToInt(String s) {
        Map<Character, Integer> romanMapper = 
            Map.ofEntries(
                Map.entry('I', 1),
                Map.entry('V', 5),
                Map.entry('X', 10),
                Map.entry('L', 50),
                Map.entry('C', 100),
                Map.entry('D', 500),
                Map.entry('M', 1000)
            );
    
        int total = 0;
        int n = s.length();
        for(int i = 0; i < n; i++) {
            int value = romanMapper.get(s.charAt(i));

            if(i < n - 1 && value < romanMapper.get(s.charAt(i + 1))) {
                total -= value;
            } else {
                total += value;
            }
        }

        return total;
    }
}