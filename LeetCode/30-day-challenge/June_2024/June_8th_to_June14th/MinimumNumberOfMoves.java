import java.util.Arrays;
import java.util.List;


record Input(int[] seats, int[] students) {}

public class MinimumNumberOfMoves {

    public int minMovesToSeat(int[] seats, int[] students) {
        int maxNumber = Math.max(Arrays.stream(seats).max().getAsInt(), Arrays.stream(students).max().getAsInt());
        int[] seatsCount = new int[maxNumber + 1];
        int[] studentsCount = new int[maxNumber + 1];
        Arrays.fill(seatsCount, 0);
        Arrays.fill(studentsCount, 0);

        for(int student : students) {
            studentsCount[student] += 1;
        }

        for(int seat : seats) {
            seatsCount[seat] += 1;
        }

        int i = 0;
        int j = 0;
        int res = 0;
        int remaining = students.length;
        while(remaining > 0) {
            if(studentsCount[i] == 0) {
                i += 1;
            }

            if(seatsCount[j] == 0) {
                j += 1;
            }

            if(seatsCount[j] != 0 && studentsCount[i] != 0) {
                res += Math.abs( i - j);
                seatsCount[j] -= 1;
                studentsCount[i] -= 1;
                remaining -= 1;
            }
        }


        return res;
    }

    public int minMovesToSeat2(int[] seats, int[] students) {
        Arrays.sort(seats);
        Arrays.sort(students);
        int res = 0;
        for(int i = 0; i < seats.length; i++) {
            res += Math.abs(seats[i] - students[i]);
        }

        return res;
    }

    public static void main(String[] args) {
        MinimumNumberOfMoves minimumNumberOfMoves = new MinimumNumberOfMoves();
        List.of(
            new Input(new int[] {3,1,5}, new int[] {2,7,4}),
            new Input(new int[] {4,1,5,9}, new int[] {1,3,2,6}),
            new Input(new int[] {2,2,6,6}, new int[] {1,3,2,6})
        ).forEach((input) -> {
            System.out.println("minMovesToSeat solution: " + minimumNumberOfMoves.minMovesToSeat(input.seats(), input.students()));
            System.out.println("minMovesToSeat2 solution: " + minimumNumberOfMoves.minMovesToSeat2(input.seats(), input.students()));
            System.out.println();
        });
    }
}