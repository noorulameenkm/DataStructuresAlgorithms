public class PalindromePermutation {

    public static void main(String[] args) {
        final PalindromePermutation p = new PalindromePermutation();
        System.out.println(p.isPermutationPalindrome("me me"));
        System.out.println(p.isPermutationPalindrome("me mea"));
    }

    private boolean isPermutationPalindrome(String str) {
        int bitVector = createBitVector(str);
        return bitVector == 0 || (bitVector & (bitVector - 1)) == 0;
    }

    private int createBitVector(String str) {
        int bitVector = 0;
        for(int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            bitVector = setUnsetBit(bitVector, c);
        }
        return bitVector;
    }

    private int setUnsetBit(int bitVector, char character) {
        int characterValue = getCharacterValue(character);
        if(characterValue == -1)
            return bitVector;

        int mask = 1 << characterValue;
        if((bitVector & mask) == 0) {
            bitVector |= mask;
        } else {
            bitVector &= ~mask;
        }

        return bitVector;
    }

    private int getCharacterValue(char character) {
        int a = Character.getNumericValue('a');
        int z = Character.getNumericValue('z');
        int c = Character.getNumericValue(character);
        if(c >= a && c <= z) {
            return c - a;
        }

        return -1;
    }
}
