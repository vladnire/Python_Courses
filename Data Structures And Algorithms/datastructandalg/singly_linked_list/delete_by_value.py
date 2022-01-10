import linked_list

print("---Delete by value---")
llist = linked_list.LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.delete_node("B")
llist.delete_node("E")
llist.print_list()