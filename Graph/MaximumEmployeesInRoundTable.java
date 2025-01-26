package Graph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class MaximumEmployeesInRoundTable {

    public int maximumInvitations(int[] favorite) {
        int n = favorite.length;

        Map<Integer, List<Integer>> adjacencyList  = new HashMap<>();
        for(int i = 0; i < n; i++) {
            adjacencyList.computeIfAbsent(favorite[i], k -> new ArrayList<>()).add(i);
        }


        int biggestCycleLength = 0;
        int cyleAndChainlength = 0;

        boolean[] visited = new boolean[n];

        for(int node = 0; node < n; node++) {
            if(!visited[node]) {
                int currentNode = node;
                int currentNodeCount = 0;

                Map<Integer, Integer> nodeCounter = new HashMap<>();
                while(!visited[currentNode]) {
                    visited[currentNode] = true;
                    nodeCounter.put(currentNode, currentNodeCount);

                    int favouriteEmployee = favorite[currentNode];
                    currentNodeCount++;
                    if(nodeCounter.containsKey(favouriteEmployee)) {
                        int currentCycleLength = currentNodeCount - nodeCounter.get(favouriteEmployee);
                        biggestCycleLength = Math.max(biggestCycleLength, currentCycleLength);

                        if(currentCycleLength == 2) {
                            boolean[] visitedNodes = new boolean[n];
                            visitedNodes[currentNode] = true;
                            visitedNodes[favouriteEmployee] = true;
                            cyleAndChainlength += 2 + Bfs(currentNode, adjacencyList, visitedNodes) + Bfs(favouriteEmployee, adjacencyList, visitedNodes);
                        }

                        break;
                    }

                    currentNode = favouriteEmployee;
                }
            }
        }

        return Math.max(biggestCycleLength, cyleAndChainlength);
    }


    private int Bfs(int node, Map<Integer, List<Integer>> adj, boolean[] visited) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{node, 0});
        int maxDistance = 0;
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int currNode = current[0];
            int dist = current[1];

            for (int neighbor : adj.getOrDefault(currNode, new ArrayList<>())) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(new int[]{neighbor, dist + 1});
                    maxDistance = Math.max(maxDistance, dist + 1);
                }
            }
        }

        return maxDistance;
    }


    public static void main(String[] args) {
        MaximumEmployeesInRoundTable maximumEmployeesInRoundTable = new MaximumEmployeesInRoundTable();
        System.out.println(
                maximumEmployeesInRoundTable.maximumInvitations(new int[]{2,2,1,2})
        );

        System.out.println(
                maximumEmployeesInRoundTable.maximumInvitations(new int[]{1,2,0})
        );

        System.out.println(
                maximumEmployeesInRoundTable.maximumInvitations(new int[]{3,0,1,4,1})
        );
    }
}