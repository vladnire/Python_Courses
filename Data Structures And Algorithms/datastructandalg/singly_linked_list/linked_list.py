class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node =  cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)  
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        # If key is head element
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # If key is not head element
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        # If there is no element with key value
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            # If pos is head element
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            # If pos is not head element
            prev = None
            count = 0   
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            # If there is no element with key value
            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    def len_iterative(self):
        cur_node = self.head
        len = 0

        while cur_node:
            len += 1
            cur_node = cur_node.next     
        
        return len

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key1, key2):

        if key1 == key2:
            return

        # Check if key1 is in the list
        prev1 = None
        cur1 = self.head
        while cur1 and cur1.data != key1:
            prev1 = cur1
            cur1 = cur1.next

        # Check if key2 is in the list
        prev2 = None
        cur2 = self.head
        while cur2 and cur2.data != key1:
            prev2 = cur2
            cur2 = cur2.next

        # If at least one of the elements does not exist, we can't swap
        if not cur1 or not cur2:
            return

        # Check if cur1 is head 
        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2

        # Check if cur2 is head 
        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1

        cur1.next, cur2.next = cur2.next, cur1.next    

    def reverse_iterative(self):
        prev = None
        cur = self.head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        # Check if one of the lists is empty
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_vals = dict()

        while cur:
            if cur.data in dup_vals:
                # Remove node
                prev.next = cur.next
                cur = None
            else:
                dup_vals[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last1(self, n):
        total_len = self.len_iterative()

        cur = self.head 
        while cur:
            if total_len == n:
                return cur.data
            total_len -= 1
            cur = cur.next

        if cur is None:
            return 

    def print_nth_from_last2(self, n):
        p = self.head
        q = self.head

        if n > 0:
            count = 0
            while q:
                count += 1
                if count >= n:
                    break
                q = q.next

            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return

            while p and q.next:
                p = p.next
                q = q.next
            return p.data

        return None

    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head

        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next

        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            # Get p and q to pivot
            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev

            # Get q to end of list
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome1(self):
        s = ""       
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

    def is_palindrome2(self):
        s = []     
        p = self.head
        while p:
            s.append(p.data)
            p = p.next
        p = self.head

        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        
        return True

    def is_palindrome3(self): 
        if self.head:  
            p = self.head
            q = self.head
            prev = []

            # Move q to the end of list
            # and append node data to prev
            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]

            count = 1
            while count <= i // 2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1

        return True

    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head
            second_to_last = None

            while last.next:
                second_to_last = last
                last = last.next

            last.next = self.head
            self.head = last
            second_to_last.next = None

    def sum_two_lists(self, llist):
        p = self.head  
        q = llist.head
        sum_llist = LinkedList()
        carry = 0

        while p or q:
            if not p:
                i = 0
            else:
                i = p.data

            if not q:
                j = 0 
            else:
                j = q.data

            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)

            if p:
                p = p.next
            if q:
                q = q.next
                
        return sum_llist