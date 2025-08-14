import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

record Interval(int start, int end) {}
public class ConflictingAppointments {
    public static boolean canAttendAllAppointments(Interval[] intervals) {
    List<Interval> allIntervals = 
        new ArrayList<>(Arrays.stream(intervals).toList());

    Collections.sort(allIntervals, (a, b) -> a.start() - b.start());
    Interval prev = new Interval(-1, -1);
    for(Interval interval: allIntervals) {
      if(interval.start() < prev.end()) return false;

      prev = interval;
    }

    return true;
  }

  public static void main(String[] args) {
    Interval[] intervals = new Interval[] {
      new Interval(1, 4),
      new Interval(2, 5),
      new Interval(7, 9)
    };
    System.out.println("Can attend all appointments: " + canAttendAllAppointments(intervals));
  }
}
