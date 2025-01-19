package Graph;

public class IsBiPartiteGraph {
    private int[] parent;
    private int[] ranks;

    public boolean isBipartite(int[][] graph) {
        parent = new int[graph.length];
        ranks = new int[graph.length];

        for(int node = 0; node < graph.length; node++) {
            parent[node] = node;
            ranks[node] = 0;
        }

        for(int node = 0; node < graph.length; node++) {
            if(graph[node].length == 0) continue;

            int parentOfNode = find(node);
            int firstNeighbour = graph[node][0];

            for(int adj: graph[node]) {
                if(parentOfNode == find(adj)) {
                    return false;
                }

                union(firstNeighbour, adj);
            }
        }

        return true;
    }

    private int find(int node) {
        if (parent[node] != node) {
            parent[node] = find(parent[node]); // Path compression
        }
        return parent[node];
    }

    private void union(int node1, int node2) {
        int root1 = find(node1);
        int root2 = find(node2);

        if (root1 != root2) {
            // Union by rank
            if (ranks[root1] > ranks[root2]) {
                parent[root2] = root1;
            } else if (ranks[root1] < ranks[root2]) {
                parent[root1] = root2;
            } else {
                parent[root2] = root1;
                ranks[root1]++;
            }
        }
    }

    public static void main(String[] args) {
        IsBiPartiteGraph solution = new IsBiPartiteGraph();
        // Example 1
        System.out.println(solution.isBipartite(new int[][]{{1,3},{0,2},{1,3},{0,2}})); // true
        // Example 2
        System.out.println(solution.isBipartite(new int[][]{{1},{0},{3},{2}})); // true
        // Example 3
        System.out.println(solution.isBipartite(new int[][]{{1,2,3},{0,2},{0,1,3},{0,2}})); // false
    }
}

