class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(node.left, value)
    else:
        if node.right is None:
            node.right = Node(value)
        else:
            self._insert_recursive(node.right, value)

bst = BinarySearchTree
for value in [3,7,6,3,4,8,9]:
    bst.insert(value)

    def search(self,value):
        return self._insert_recursive(self.root,value)
    def _search_recursive(self,node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            
