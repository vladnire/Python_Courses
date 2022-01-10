from binary_tree import BinaryTree, Node

print("---Calculate height of binary tree---")
# Calculate height of binary tree:
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
print(tree.height(tree.root))