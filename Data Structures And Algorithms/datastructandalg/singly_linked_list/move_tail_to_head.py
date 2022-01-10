import linked_list

print("---Move Tail to Head---")
llist = linked_list.LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.print_list()
llist.move_tail_to_head()
print("\n")
llist.print_list()