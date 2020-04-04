class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data
    
    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, node):
        self._left = node
    
    @property
    def right(self):
        return self._right
    
    @right.setter
    def right(self, node):
        self._right = node