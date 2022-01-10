import circular_list

print("---Remove Node---")
cllist = circular_list.CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.print_list()
print('\n')
cllist.remove("A")
cllist.remove("C")
cllist.print_list()