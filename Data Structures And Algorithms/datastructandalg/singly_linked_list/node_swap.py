import linked_list

print("---Node swap---")
llist = linked_list.LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
print("Original List")
llist.print_list()
llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()
llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.print_list()
llist.swap_nodes("D", "B")
print("Swapping nodes D and B where key_2 is head node")
llist.print_list()
llist.swap_nodes("C", "C")
print("Swapping nodes C and C where both keys are same")
llist.print_list()