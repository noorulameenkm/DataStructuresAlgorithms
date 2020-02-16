import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;


/*
Question:-
Given a 2D grid, each cell is either a zombie 1 or a human 0. 
Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. 
Find out how many hours does it take to infect all humans?
*/
public class zoombieHumanProblem {
    public static void main(String[] args) {
        int[][] grid = {{0, 0, 1, 0, 1},{0, 0, 0, 1, 0},{0, 0, 0, 0, 1},{0, 1, 0, 0, 0}};
        int hours = findNumberOfHours(grid);
        System.out.println(hours);
    }

    static int findNumberOfHours(int[][] grid){
        int row = grid.length,col = grid[0].length,i, j;
        Deque<Location> humans = new ArrayDeque<>();
        HashMap<String, Location> zombies = new HashMap<>();
        for(i = 0; i < row; i++){
            for(j = 0; j < col; j++){
                if(grid[i][j] == 0){
                    // Human
                    humans.add(new Location(i, j));
                } else {
                    // Zombie
                    Location loc = new Location(i,j);
                    String key = i + "" + j;
                    zombies.put(key, loc);
                }
            }
        }

        Queue<Location> selected = new LinkedList<>();
        int hours;
        for(hours = 0; hours >= 0 && humans.size() > 0; hours++){
            int qSize = humans.size();
            for(int s = 0; s < qSize; s++){
                Location loc = humans.remove();
                Boolean visited = false;
                String key;
                if(!visited && isValid(loc.row + 1, loc.col, row, col)){
                    int temp = loc.row + 1;
                    key = temp + "" + loc.col;
                    if(zombies.containsKey(key)){
                        selected.add(loc);
                        visited = true;
                    }
                }
                if(!visited && isValid(loc.row - 1, loc.col, row, col)){
                    int temp = loc.row - 1;
                    key = temp + "" + loc.col;
                    if(zombies.containsKey(key)){
                        selected.add(loc);
                        visited = true;
                    }
                }
                if(!visited && isValid(loc.row, loc.col + 1, row, col)){
                    int temp = loc.col + 1;
                    key = loc.row + "" + temp;
                    if(zombies.containsKey(key)){
                        selected.add(loc);
                        visited = true;
                    }
                }
                if(!visited && isValid(loc.row, loc.col - 1, row, col)){
                    int temp = loc.col - 1;
                    key = loc.row + "" + temp;
                    if(zombies.containsKey(key)){
                        selected.add(loc);
                        visited = true;
                    }
                }

                if(!visited){
                    humans.addLast(loc);
                }
                
            }

            while(!selected.isEmpty()){
                Location head = selected.remove();
                String key = head.row + "" + head.col;
                zombies.put(key, head);
            }
        }
        return hours;
    }

    static Boolean isValid(int locRow, int locCol, int row, int col){
        if(
            locRow < 0 ||
            locCol < 0 ||
            locRow >= row ||
            locCol >= col
        ){
            return false;
        }

        return true;
    }
}


class Location {
    int row;
    int col;
    Location(int row, int col){
        this.row = row;
        this.col = col;
    }
}