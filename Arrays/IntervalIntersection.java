import java.util.ArrayList;
import java.util.List;

record Interval(int start, int end) {}

public class IntervalIntersection {
    public List<Interval> merge(Interval[] arr1, Interval[] arr2) {
    List<Interval> result = new ArrayList<Interval>();
    int i = 0, j = 0;
    while(i < arr1.length && j < arr2.length) {
      Interval first = arr1[i];
      Interval second = arr2[j];
      if(first.start() >= second.start() && first.start() <= second.end() || second.start() >= first.start() && second.start() <= first.end()) {
        result.add(new Interval(Math.max(first.start(), second.start()), Math.min(first.end(), second.end())));
      }

      if(first.end() <= second.end()) i++; else j++;
    }
    
    return result;
  }

  public static void main(String[] args) {
    Interval[] arr1 = {new Interval(1, 3), new Interval(5, 7), new Interval(9, 11)};
    Interval[] arr2 = {new Interval(2, 4), new Interval(6, 8), new Interval(10, 12)};
    
    IntervalIntersection ii = new IntervalIntersection();
    List<Interval> result = ii.merge(arr1, arr2);
    
    for (Interval interval : result) {
      System.out.println("[" + interval.start() + ", " + interval.end() + "]");
    }
  }
}