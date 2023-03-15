class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, node):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)

    def delete(self, key):
        if self.root is None:
            return None
        else:
            return self._delete(key, self.root)

    def _delete(self, key, node):
        if key < node.val:
            node.left = self._delete(key, node.left)
        elif key > node.val:
            node.right = self._delete(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._find_min(node.right)
                node.val = temp.val
                node.right = self._delete(temp.val, node.right)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, key):
        return self._search(key, self.root)

    def _search(self, key, node):
        if node is None:
            return False
        elif key == node.val:
            return True
        elif key < node.val:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)
