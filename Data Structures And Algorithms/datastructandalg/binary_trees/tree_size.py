from binary_tree import BinaryTree, Node

# Calculate size of binary tree:
#     1
#    / \
#   2  3
#  / \
# 4  5
# 
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("---Calculate size of binary tree iterative---")
print(tree.size_iterative())

print("---Calculate size of binary tree recursive---")
print(tree.size_recursive(tree.root))