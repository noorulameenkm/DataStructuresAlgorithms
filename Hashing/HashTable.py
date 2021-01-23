class HashEntry:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None # reference to new Entry     


class HashTable:
    def __init__(self):
        self.slots = 10
        self.size = 0
        self.threshold = 0.6
        self.bucket = [None] * self.slots
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.get_size() == 0
    
    def get_index(self, key):
        hash_code = hash(key)
        return hash_code % self.slots

    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots

        for i in range(len(self.bucket)):
            head = self.bucket[i]

            while head is not None:
                new_index = hash(head.key) % new_slots

                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key is head.key:
                            node.value = head.value
                            # node = None
                            break
                        if node.next is None:
                            node.next = HashEntry(head.key, head.value)
                            # node = None
                            break
                        
                        node = node.next

                head = head.next
        
        self.slots = new_slots
        self.bucket = new_bucket

    def insert(self, key, value):
        index = self.get_index(key)

        if self.bucket[index] is None:
            self.bucket[index] = HashEntry(key, value)
            self.size += 1
        else:
            head = self.bucket[index]
            while head is not None:
                if head.key == key:
                    head.value = value
                    break
                
                if head.next is None:
                    head.next = HashEntry(key, value)
                    self.size += 1
                    break
                
                head = head.next

        load_factor = float(self.size) / float(self.slots)
        if load_factor >= self.threshold:
            self.resize()

    
    def search(self, key):
        index = self.get_index(key)
        head = self.bucket[index]

        while head is not None:
            if head.key == key:
                return head.value
            
            head = head.next
        
        return None

    def delete(self, key):
        index = self.get_index(key)
        head = self.bucket[index]
        previous = None

        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket[index] = head.next
                else:
                    previous.next = head.next
                
                self.size -= 1
                
            previous = head
            head = head.next

         
            
            

                


    