import linked_list

print("---Rotate---")
llist = linked_list.LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist.rotate(4)
llist.print_list()