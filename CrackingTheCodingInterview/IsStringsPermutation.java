public class IsStringsPermutation {

    public boolean isPermutation(String s, String t) {
        // Assume only ascii characters are there
        if(s.length() != t.length()) {
            return false;
        }

        int[] map = new int[128];
        for(int i = 0; i < s.length(); i++){
            map[s.charAt(i)]++;
        }

        for(int i = 0; i < t.length(); i++){
            map[t.charAt(i)]--;
            if(map[t.charAt(i)] < 0){
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(
                new IsStringsPermutation().isPermutation("abcd", "bcad")
        );

        System.out.println(
                new IsStringsPermutation().isPermutation("ameen", "Ameen")
        );
    }
}
