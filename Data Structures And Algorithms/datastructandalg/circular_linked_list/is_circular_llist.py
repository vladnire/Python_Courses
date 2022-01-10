# Not recommended
"""
import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'singly_linked_list')))
import linked_list
"""
from ..singly_linked_list import linked_list

import circular_list

print("---Is Circular Llist---")
cllist = circular_list.CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
llist = linked_list.LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
print(cllist.is_circular_linked_list(cllist))
print(cllist.is_circular_linked_list(llist))
