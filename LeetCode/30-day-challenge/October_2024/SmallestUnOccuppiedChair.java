import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.stream.IntStream;

record TimeInterval(int start, int end) implements Comparable<TimeInterval> {

    @Override
    public int compareTo(TimeInterval other) {
        return Integer.compare(this.start, other.start);
    }
}

record EndAndSeat(int end, int seat) implements Comparable<EndAndSeat> {

    @Override
    public int compareTo(EndAndSeat other) {
        return Integer.compare(this.end, other.end);
    }
}

public class SmallestUnOccuppiedChair {

    public static void main(String[] args) {
        SmallestUnOccuppiedChair s = new SmallestUnOccuppiedChair();
        System.out.println(
                s.smallestUnOccupiedChair(
                        new int[][] {{1, 4}, {2, 3}, {4, 6}}, 1
                )
        );

        System.out.println(
                s.smallestUnOccupiedChair(
                        new int[][] {{3, 10}, {1, 5}, {2, 6}}, 0
                )
        );
    }

    public int smallestUnOccupiedChair(int[][] times, int targetFriend) {
        List<TimeInterval> intervals = new ArrayList<>();
        int targetStartTime = times[targetFriend][0];
        for(int[] time : times) {
            intervals.add(new TimeInterval(time[0], time[1]));
        }

        Collections.sort(intervals);

        Queue<Integer> seats = new PriorityQueue<>();
        seats.addAll(IntStream.range(0, intervals.size()).boxed().toList());

        Queue<EndAndSeat> occuppiedSeats = new PriorityQueue<>();
        int allocatedSeat = -1;
        for(TimeInterval interval : intervals) {
            while(!occuppiedSeats.isEmpty() && interval.start() >= occuppiedSeats.peek().end()) {
                EndAndSeat polledEndAndSeat = occuppiedSeats.poll();
                seats.offer(polledEndAndSeat.seat());
            }

            allocatedSeat = seats.poll();
            occuppiedSeats.offer(new EndAndSeat(interval.end(), allocatedSeat));
            if(interval.start() == targetStartTime) {
                break;
            }
        }

        return allocatedSeat;

    }
}

