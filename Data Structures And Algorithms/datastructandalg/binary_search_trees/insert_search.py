from binary_search_tree import BST

print("---Insert and search---")
bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)
print(bst.search(9))
print(bst.search(14))