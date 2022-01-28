import doubly_list

print("---Delete node---")
dllist = doubly_list.DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.print_list()
print("Delete head node")
dllist.delete(1)
dllist.print_list()
print("Delete node that does not exist")
dllist.delete(6)
dllist.print_list()
print("Delete node in the middle")
dllist.delete(3)
dllist.print_list()
print("Delete last node")
dllist.delete(4)
dllist.print_list()