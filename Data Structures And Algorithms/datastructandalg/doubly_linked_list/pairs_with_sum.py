import doubly_list

print("---Pairs with sum---")
dllist = doubly_list.DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
dllist.print_list()
print(dllist.pairs_with_sum(5))