

class DisjointSet:
    def __init__(self, n):
        self.ranks = [0 for _ in range(n + 1)]
        self.parents = [i for i in range(n + 1)]
    

    def find_parent(self, node):
        if node == self.parents[node]:
            return node
        
        self.parents[node] = self.find_parent(self.parents[node])
        return self.parents[node]
    
    def union_by_rank(self, u, v):
        u_ul_parent = self.find_parent(u)
        v_ul_parent = self.find_parent(v)

        if u_ul_parent == v_ul_parent:
            return

        if self.ranks[u_ul_parent] < self.ranks[v_ul_parent]:
            self.parents[u_ul_parent] = v_ul_parent
        elif self.ranks[v_ul_parent] < self.ranks[u_ul_parent]:
            self.parents[v_ul_parent] = u_ul_parent
        else:
            self.parents[v_ul_parent] = u_ul_parent
            self.ranks[u_ul_parent] += 1


if __name__ == "__main__":
    ds = DisjointSet(7)
    ds.union_by_rank(1, 2)
    ds.union_by_rank(2, 3)
    ds.union_by_rank(4, 5)
    ds.union_by_rank(6, 7)
    ds.union_by_rank(5, 6)

    if ds.find_parent(3) == ds.find_parent(7):
        print("Same")
    else:
        print("No Same")

    ds.union_by_rank(3, 7)

    if ds.find_parent(3) == ds.find_parent(7):
        print("Same")
    else:
        print("No Same")