import doubly_list

print("---Reverse---")
dllist = doubly_list.DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.print_list()
print("Reverse")
dllist.reverse()
dllist.print_list()