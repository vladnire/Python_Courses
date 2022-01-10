import linked_list

print("---Is Palindrome---")
llist = linked_list.LinkedList()
llist_2 = linked_list.LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")
print(llist.is_palindrome1())
print(llist.is_palindrome2())
print(llist.is_palindrome3())
print(llist_2.is_palindrome1())
print(llist_2.is_palindrome2())
print(llist_2.is_palindrome3())