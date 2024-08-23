import java.util.Arrays;
import java.lang.Comparable;

class Work implements Comparable<Work> {
    public int difficulty;
    public int profit;

    public Work(int p, int d) {
        difficulty = d;
        profit = p;
    }

    @Override
    public int compareTo(Work other) {
        if(difficulty > other.difficulty) {
            return 1;
        } else if(difficulty < other.difficulty) {
            return -1;
        }

        if(profit > other.profit) {
            return 1;
        }
    }

}

public class MostProfitAssigningWork {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        Arrays.sort();
        return 0;
    }
}
