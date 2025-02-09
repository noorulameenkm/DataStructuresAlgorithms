package Design;

import java.util.HashMap;
import java.util.Map;
import java.util.SortedSet;
import java.util.TreeSet;

class NumberContainers {
    Map<Integer, Integer> indexToNumber;
    Map<Integer, SortedSet<Integer>> numberToIndices;

    public NumberContainers() {
        indexToNumber = new HashMap<>();
        numberToIndices = new HashMap<>();
    }
    
    public void change(int index, int number) {
        if(indexToNumber.containsKey(index)) { // index has a number already
            int previousNumber = indexToNumber.get(index);
            numberToIndices.get(previousNumber).remove(index);
        }

        indexToNumber.put(index, number);
        numberToIndices.computeIfAbsent(number, k -> new TreeSet<>()).add(index);
    }
    
    public int find(int number) {
        SortedSet<Integer> indices = numberToIndices.getOrDefault(number, new TreeSet<>());
        return indices.size() > 0 ? indices.first() : -1;
    }

    public static void main(String[] args) {
        NumberContainers nc = new NumberContainers();
        System.out.println(nc.find(10));; // There is no index that is filled with number 10. Therefore, we return -1.
        nc.change(2, 10); // Your container at index 2 will be filled with number 10.
        nc.change(1, 10); // Your container at index 1 will be filled with number 10.
        nc.change(3, 10); // Your container at index 3 will be filled with number 10.
        nc.change(5, 10); // Your container at index 5 will be filled with number 10.
        System.out.println(nc.find(10));; // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
        nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
        System.out.println(nc.find(10));; // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
    }
}
