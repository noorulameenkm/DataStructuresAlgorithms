import java.util.Queue;
import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.List;


record Input(int k, int w, int[] profits, int[] capital) {}

class Project {
    int capital;
    int profit;

    public Project(int profit, int capital) {
        this.capital = capital;
        this.profit = profit;
    } 
}


public class IPO {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {

        Comparator<Project> capitalComparator = (project1, project2) -> {
            if(project1.capital == project2.capital) {
                return 0;
            } else if(project1.capital > project2.capital) {
                return 1;
            }

            return -1;
        };

        Comparator<Project> profitComparator = (project1, project2) -> {
            if(project1.profit == project2.profit) {
                return 0;
            } else if(project1.profit < project2.profit) {
                return 1;
            }

            return -1;
        };
        

        Queue<Project> minPq = new PriorityQueue<>(capitalComparator);
        Queue<Project> maxPq = new PriorityQueue<>(profitComparator);
        int length = profits.length;
        for(int i = 0; i < length; i++) {
            minPq.add(new Project(profits[i], capital[i]));
        }

        for(int j = 0; j < k; j++) {
            while(minPq.size() > 0 && minPq.peek().capital <= w) {
                maxPq.add(minPq.poll());
            }

            if(maxPq.size() == 0) {
                break;
            }

            w += maxPq.poll().profit;
        }
        
        return w;
    }

    public static void main(String[] args) {
        IPO ipo = new IPO();
        List.of(
            new Input(2, 0, new int[] {1,2,3}, new int[] {0,1,1}),
            new Input(3, 0, new int[] {1,2,3}, new int[] {0,1,1})
        ).forEach(input -> {
            System.out.println(ipo.findMaximizedCapital(input.k(), input.w(), input.profits(), input.capital()));
        });
    }
}
