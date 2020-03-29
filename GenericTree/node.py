class Node:
    def __init__(self, data):
        self._data = data
        self._firstChild = None
        self._nextSibling = None

    @property
    def data(self):
        return self._data
    
    @data.setter 
    def data(self, data):
        self._data = data
    
    @property 
    def firstChild(self):
        return self._firstChild;

    @firstChild.setter
    def firstChild(self, firstChild):
        self._firstChild = firstChild

    @property
    def nextSibling(self):
        return self._nextSibling;
    
    @nextSibling.setter
    def nextSibling(self, nextSibling):
        self._nextSibling = nextSibling
