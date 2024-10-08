import java.util.Arrays;

public class URLify {
    
    public static void main(String[] args) {
        URLify urLify = new URLify();

        System.out.println(urLify.urlifyString("Mr John Smith    ", 13));
        System.out.println(urLify.urlifyString("my name is Khan      ", 15));
    }

    private String urlifyString(String str, int trueLength) {
        
        char[] charArray = str.toCharArray();
        int spaceCount = 0;
        for(int i = 0; i < trueLength; i++) {
            if(charArray[i] == ' ') spaceCount += 1;
        }

        int index = trueLength + spaceCount * 2;
        if(trueLength < str.length()) {
            charArray[trueLength] = '\0';
        }

        for(int j = trueLength - 1; j >= 0; j--) {
            if(charArray[j] == ' ') {
                charArray[index - 1] = '0';
                charArray[index - 2] = '2';
                charArray[index - 3] = '%';
                index -= 3;
            } else {
                charArray[index - 1] = charArray[j];
                index -= 1;
            }
        }

        return Arrays.toString(charArray);
    }
}
