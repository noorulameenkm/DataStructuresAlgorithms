

class Snapshot:
    def __init__(self, n):
        self.number_of_nodes = n
        self.snapshots = dict()
        self.nodes = [0] * n
    

    def set_state(self, idx, state):
        if idx < self.number_of_nodes:
            self.nodes[idx] = state
    

    def snap(self):
        length = len(self.snapshots)
        self.snapshots[length] = list(self.nodes)
        return length
    

    def fetch_state(self, idx, snapshot_id):
        if snapshot_id <= len(self.snapshots) and idx < self.number_of_nodes:
            return self.snapshots[snapshot_id][idx]
        
        return None
    
    @classmethod
    def classname(cls):
        return cls.__name__



""""
    function        Time complexity         Space complexity
    ------------------------------------------------
    snap            O(n)
    fetch_state     O(1)                     O(n * m)
    set_state       O(1)                         
"""
class Snapshot2:
    def __init__(self, length):
        self.snapshot_id = 0
        self.node_state = dict()
        self.node_state[0] = dict()
        self.ncount = length
    
    def set_state(self, idx, val):
        if idx < self.ncount:
            self.node_state[self.snapshot_id][idx] = val
    
    def snap(self):
        self.snapshot_id += 1
        self.node_state[self.snapshot_id] = (self.node_state[self.snapshot_id - 1]).copy()
        return self.snapshot_id - 1

    def fetch_state(self, idx, snapshot_id):
        if snapshot_id < self.snapshot_id and snapshot_id >= 0 and idx < self.ncount:
            return self.node_state[snapshot_id][idx] if idx in self.node_state[snapshot_id] else 0 
        else:
            return None
    
    @classmethod
    def classname(cls):
        return cls.__name__



for snapshot_class in [Snapshot, Snapshot2]:
    print(f"-----Example 1:----- {snapshot_class.classname()}")
    print()
    snapshotArr = snapshot_class(3)  
    print("Initializing the data structure with three nodes") 
    print("Setting the state of node 0 to 5") 
    snapshotArr.set_state(0,5)  
    print("Snap id:",snapshotArr.snap())  
    snapshotArr.set_state(0,1)
    print("Setting the state of node 0 to 1") 
    snapshotArr.set_state(2,3)
    print("Setting the state of node 2 to 3") 
    snapshotArr.set_state(1,10)
    print("Setting the state of node 1 to 10") 
    print("Node state at index 0 with Snap id 0 is:", snapshotArr.fetch_state(0,0))
    print("Snap id:",snapshotArr.snap())
    print("Node state at index 0 with Snap id 1 is:",snapshotArr.fetch_state(0,1))
    print("Node state at index 1 with Snap id 1 is:",snapshotArr.fetch_state(1,1))

    print()

    print(f"-----Example 2:----- for {snapshot_class.classname()}")
    snapshotArr2 = snapshot_class(5)  
    print("Initializing the data structure with five nodes") 
    print("Setting the state of node 4 to 1)") 
    snapshotArr2.set_state(4,1)  
    print("Snap id:",snapshotArr2.snap())  
    print("Setting the state of node 2 to 21") 
    snapshotArr2.set_state(2,21)
    print("Snap id:",snapshotArr2.snap())
    print("Node state at index 4 with Snap id 1 is::", snapshotArr2.fetch_state(4,1))
    print("Node state at index 2 with Snap id 1 is::",snapshotArr2.fetch_state(2,1))
    print("Node state at index 3 with Snap id 1 is::",snapshotArr2.fetch_state(3,1))
        
