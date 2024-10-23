public class MinimumSwapToBalanceParanthesis {
    public static void main(String[] args) {
        MinimumSwapToBalanceParanthesis minimumSwapToBalanceParanthesis =
        new MinimumSwapToBalanceParanthesis();

        System.out.println(
            minimumSwapToBalanceParanthesis.minimumToMakeBalancedParanthesis("][][")
        );
        System.out.println(
            minimumSwapToBalanceParanthesis.minimumToMakeBalancedParanthesis("]]][[[")
        );
        System.out.println(
            minimumSwapToBalanceParanthesis.minimumToMakeBalancedParanthesis("[]")
        );
    }

    private int minimumToMakeBalancedParanthesis(String str) {
        int unmatchedOpeningBracket = 0;

        for(int i = 0; i < str.length(); i++) {
            if(str.charAt(i) =='[')
                unmatchedOpeningBracket ++;
            else if(unmatchedOpeningBracket > 0)
                unmatchedOpeningBracket -= 1;
        }

        return (unmatchedOpeningBracket + 1) / 2;
    }
}
