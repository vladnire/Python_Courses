import linked_list

print("---Count occurences---")
llist = linked_list.LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist_2 = linked_list.LinkedList()
llist_2.append(1)
llist_2.append(2)
llist_2.append(1)
llist_2.append(3)
llist_2.append(1)
llist_2.append(4)
llist_2.append(1)
print(llist_2.count_occurences_iterative(1))
print(llist_2.count_occurences_recursive(llist_2.head, 1))