import circular_list

print("---Josephus Problem---")
cllist = circular_list.CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
cllist.josephus_circle(2)
cllist.print_list()