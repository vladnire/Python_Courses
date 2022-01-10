from binary_tree import BinaryTree, Node

print("---Level Order Traversal---")
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.print_tree("levelorder", tree.root))