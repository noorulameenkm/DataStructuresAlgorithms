public class BestTimeToSellStock {

    public static void main(String[] args) {
        System.out.println(
            maxProfit(
                new int[] {3, 2, 6, 5, 0, 3}
            )
        );

        System.out.println(
            maxProfit(
                new int[] {8, 6, 5, 2, 1}
            )
        );

        System.out.println(
            maxProfit(
                new int[] {1, 2}
            )
        );
    }

    public static int maxProfit(int[] prices) {
        int maxProfit = 0;
        int min = Integer.MAX_VALUE;
        for(int i = 0; i < prices.length; i++) {
            min = Math.min(min, prices[i]);
            int profit = prices[i] - min;
            if(profit > maxProfit) {
                maxProfit = profit;
            }
        }
        
        return maxProfit;
    }
    
}
