from disjoint_sets import DisjointSet


class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        
        ds = DisjointSet(V)
        sum_ = 0
        edges = []
        for i in range(V):
            arr = adj[i]
            for node, weight in arr:
                edges.append([i, node, weight])
                
        edges.sort(key = lambda x: x[2])
        for node1, node2, weight in edges:
            if ds.find_parent(node1) != ds.find_parent(node2):
                ds.union_by_rank(node1, node2)
                sum_ += weight
        
        return sum_
    

if __name__ == "__main__":
    adj_list = [
        [[1, 5], [2, 1]],
        [[2, 3], [0, 5]],
        [[0, 1], [1, 3]]
    ]

    V = 3
    print(Solution().spanningTree(V, adj_list))