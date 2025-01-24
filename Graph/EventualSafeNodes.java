package Graph;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class EventualSafeNodes {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        Map<Integer, Integer> outDegrees = new HashMap<>();
        Map<Integer, List<Integer>> ancestors = new HashMap<>();

        List<Integer> results = new ArrayList<>();
        Queue<Integer> queue = new ArrayDeque<>();

        for(int i = 0; i < graph.length; i++) {
            int[] nodes = graph[i];
            outDegrees.put(i, nodes.length);
            for(int node : nodes) {
                ancestors.computeIfAbsent(node, k -> new ArrayList<>())
                    .add(i);
            }

            if(nodes.length == 0) {
                results.add(i);
                queue.offer(i);
            }
        }

        while(!queue.isEmpty()) {
            int node = queue.poll();
            if(ancestors.get(node) == null) continue;
            List<Integer> ancestorsOfNode = ancestors.get(node);
            for(int ancestor : ancestorsOfNode) {
                outDegrees.put(ancestor, outDegrees.get(ancestor) - 1);
                if(outDegrees.get(ancestor) == 0) {
                    results.add(ancestor);
                    queue.offer(ancestor);
                }
            }
        }

        Collections.sort(results);
        return results;
    }

    public static void main(String[] args) {
        EventualSafeNodes sol = new EventualSafeNodes();
        System.out.println(
            sol.eventualSafeNodes(
                new int[][]{
                    {1, 2},
                    {2, 3},
                    {5},
                    {0},
                    {5},
                    {},
                    {}
                }
            )
        );

        System.out.println(
            sol.eventualSafeNodes(
                new int[][]{
                    {1, 2, 3, 4},
                    {1, 2},
                    {3, 4},
                    {0, 4},
                    {}
                }
            )
        );
    }
}
