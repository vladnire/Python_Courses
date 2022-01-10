class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def _insert(self, current, new_val):
        if current.data < new_val:
            if current.right:
                self._insert(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self._insert(current.left, new_val)
            else:
                current.left = Node(new_val)

    def insert(self, new_val):
        self._insert(self.root, new_val)

    def _search(self, current, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self._search(current.right, find_val)
            else:
                return self._search(current.left, find_val)

    def search(self, find_val):
        return self._search(self.root, find_val)

    def is_bst_satisfied(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.data
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(self.root)

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)