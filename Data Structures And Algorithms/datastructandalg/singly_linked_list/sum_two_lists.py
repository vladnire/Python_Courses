import linked_list

print("---Sum Two Lists---")
# 3 6 5 
#   4 2 
# ------
#  
llist1 = linked_list.LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)
llist2 = linked_list.LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)
print(365 + 248)
llist1.sum_two_lists(llist2)