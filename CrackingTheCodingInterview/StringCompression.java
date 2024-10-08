public class StringCompression {
    public static void main(String[] args) {
        StringCompression s = new StringCompression();
        System.out.println(
                s.compressedOrOriginal("aabcccccaaa")
        );
        System.out.println(
                s.compressedOrOriginal("amamam")
        );
    }

    private String compressedOrOriginal(String str) {
        int compressedLength = checkCompressedLength(str);

        if(compressedLength >= str.length()) {
            return str;
        }

        int charCount = 0;
        StringBuilder compressed = new StringBuilder(compressedLength);
        for(int i = 0; i < str.length(); i++) {
            charCount++;
            if(i + 1 >= str.length() || str.charAt(i) != str.charAt(i + 1)) {
                compressed.append(str.charAt(i));
                compressed.append(charCount);
                charCount = 0;
            }
        }

        return compressed.toString();
    }

    private int checkCompressedLength(String string) {
        int count = 0;
        int compressedLength = 0;

        for(int i = 0; i < string.length(); i++) {
            count ++;

            if(i + 1 >= string.length() || string.charAt(i) != string.charAt(i + 1)) {
                compressedLength += 1 + String.valueOf(count).length();
                count = 0;
            }
        }

        return compressedLength;
    }
}
