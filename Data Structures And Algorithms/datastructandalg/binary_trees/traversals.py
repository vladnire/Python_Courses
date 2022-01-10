from binary_tree import BinaryTree, Node

print("---Traversals---")
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder", tree.root))
print(tree.print_tree("inorder", tree.root))
print(tree.print_tree("postorder", tree.root))