from binary_search_tree import BST, Node

print("---Check BST property---")
"""
The BST property states that every node on the right subtree 
has to be larger than the current node, and every node on the left 
subtree has to be smaller than the current node.
"""
bst = BST(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
tree = BST(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
print(bst.inorder_print_tree())
print(bst.is_bst_satisfied())
print(tree.inorder_print_tree())
print(tree.is_bst_satisfied())