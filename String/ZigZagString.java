public class ZigZagString {
    public static void main(String[] args) {
        System.out.println(
            convert("HELLOPROGRAMMING", 4)
        );
        
        System.out.println(
            convert("PROBLEMCHALLENGE", 5)
        );

        System.out.println(
            convert("ABCDE", 2)
        );
    }

    public static String convert(String s, int numRows) {

        if(numRows == 1) {
            return s;
        }

        final StringBuilder[] rows = new StringBuilder[numRows];
        for(int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }

        int currentRow = 0; // point to the row
        boolean moveDown = false; // use to decide whether to move up or down
        for(char c: s.toCharArray()) {
            rows[currentRow].append(c);

            if(currentRow == 0 || currentRow == numRows - 1) {
                moveDown = !moveDown;
            }

            currentRow += moveDown ? 1 : -1;
        }

        final StringBuilder result = new StringBuilder();
        for(StringBuilder row : rows) {
            result.append(row.toString());
        }

        return result.toString();
    }
}
