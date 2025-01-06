import java.util.Arrays;

public class ShiftLettersTwo {
    public String shiftingLetters(String s, int[][] shifts) {
        int n = s.length();
        int[] diff = new int[n];

        Arrays.fill(diff, 0);

        for(int[] shift : shifts) {
            int startIndex = shift[0];
            int endIndex = shift[1];
            int shiftDirection = shift[2];

            int shiftValue = shiftDirection == 1 ? 1 : -1;

            diff[startIndex] += shiftValue;

            if(endIndex + 1 < n) {
                diff[endIndex + 1] += -1 * shiftValue; 
            }
        }

        for(int i = 1; i < n; i++) {
            diff[i] += diff[i - 1];
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++) {
            int shift = diff[i] % 26;
            if(shift < 0) shift += 26;

            char c = (char) (((s.charAt(i) - 'a') + shift) % 26 + 'a');
            sb.append(c);
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        ShiftLettersTwo shiftLettersTwo = new ShiftLettersTwo();
        String s = "abc";
        int[][] shifts = {{0,1,0}, {1,2,1}, {0,2,1}};
        System.out.println(shiftLettersTwo.shiftingLetters(s, shifts));

        s = "dztz";
        System.out.println(shiftLettersTwo.shiftingLetters(s, new int[][]{{0,0,0}, {1,1,1}}));
    }
}
