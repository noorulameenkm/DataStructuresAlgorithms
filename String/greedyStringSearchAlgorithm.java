public class greedyStringSearchAlgorithm {
    public static void main(String[] args) {
        String s = "geeksforgeeks";
        String pattern = "geeks";
        greedyStringSearchAlgorithm ga = new greedyStringSearchAlgorithm();
        int search = ga.findStringPresent(s, pattern);
        
        if(search == 1){
            System.out.println("Found");
        } else {
            System.out.println("Not Found");
        }
    }

    private int findStringPresent(String s, String pattern){
        int n = s.length(), m = pattern.length();
        for(int i = 0; i <= (n - m); i++){
            int k = 0;
            while(k < m && s.charAt(i) == pattern.charAt(k)){
                k++;
                i++;
            }

            if(k == m){
                return 1;
            }
        }

        return 0;
    }
}