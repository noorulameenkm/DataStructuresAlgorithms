import java.util.Arrays;

public class MinimumLengthStringAfterOperations {
    public int minimumLength(String s) {
        int[] frequency = new int[26];
        Arrays.fill(frequency, 0);
        for(char c : s.toCharArray()) {
            int index = c - 'a';
            frequency[index]++;
        }

        int length = s.length();

        for(int i = 0; i < 26; i++) {
            if(frequency[i] >= 3) {
                int deleteCount = frequency[i] % 2 == 0 ? frequency[i] - 2 : frequency[i] - 1;
                length -= deleteCount;
            } 
        }

        return length;
    }

    public static void main(String[] args) {
        MinimumLengthStringAfterOperations obj = new MinimumLengthStringAfterOperations();
        System.out.println(obj.minimumLength("abaacbcbb"));
        System.out.println(obj.minimumLength("aa"));
    }
}
