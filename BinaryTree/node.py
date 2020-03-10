class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None
        self._nextsibling = None

    @property
    def data(self):
        return self._data
    
    @data.setter 
    def data(self, data):
        self._data = data

    @data.deleter 
    def data(self):
        del self._data
    
    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, value):
        self._left = value
    
    @left.deleter
    def left(self):
        del self._left

    @property
    def right(self):
        return self._right
    
    @right.setter
    def right(self, value):
        self._right = value
    
    @right.deleter
    def right(self):
        del self._right
    
    @property
    def nextsibling(self):
        return self._nextsibling
    
    @nextsibling.setter
    def nextsibling(self, val):
        self._nextsibling = val
    
    @nextsibling.deleter
    def nextsibling(self):
        del self._nextsibling