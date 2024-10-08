public class IsStringCharactersUnique {

    public boolean isUniqueCharacters(String str) {
        int bitValue = 0;

        for(int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            final int position = c - 'a';
            if((bitValue & (1 << position)) > 0) {
                return false;
            }

            bitValue |= (1 << position);
        }

        return true;
    }
    public static void main(String[] args) {
        IsStringCharactersUnique obj = new IsStringCharactersUnique();
        System.out.println(obj.isUniqueCharacters("abcd"));
        System.out.println(obj.isUniqueCharacters("abbc"));
    }
}
