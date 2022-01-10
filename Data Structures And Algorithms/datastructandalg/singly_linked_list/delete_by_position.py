import linked_list

print("---Delete by position---")
llist = linked_list.LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.delete_node_at_pos(0)
llist.print_list()