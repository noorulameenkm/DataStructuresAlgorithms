public class MinimumOneEditAway {
    public static void main(String[] args) {

        MinimumOneEditAway obj = new MinimumOneEditAway();
        System.out.println(obj.isOneEditAway("pale", "ple"));
        System.out.println(obj.isOneEditAway("pale", "bale"));
        System.out.println(obj.isOneEditAway("pae", "bble"));
    }

    private boolean isOneEditAway(String s1, String s2) {
        if(Math.abs(s1.length() - s2.length()) > 1)
            return false;

        final String string1 = s1.length() < s2.length() ? s1 : s2;
        final String string2 = s1.length() < s2.length() ? s2 : s1;

        int index1 = 0, index2 = 0;
        boolean flag = false;
        while(index1 < string1.length() && index2 < string2.length()) {
            if(string1.charAt(index1) != string2.charAt(index2)) {
                if(flag)
                    return false;
                flag = true;

                if(string1.length() == string2.length()) {
                    index1++;
                }

            } else {
                index1++;
            }

            index2++;
        }

        return true;
    }
}
