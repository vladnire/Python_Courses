import linked_list

print("---N-th to last---")
llist = linked_list.LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
print(llist.print_nth_from_last1(4))
print(llist.print_nth_from_last2(4))