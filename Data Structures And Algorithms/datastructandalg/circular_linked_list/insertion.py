import circular_list

print("---Insertion---")
cllist = circular_list.CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list() 