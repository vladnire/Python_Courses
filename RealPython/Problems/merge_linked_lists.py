class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"


def merge_k_linked_lists(linked_lists):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''
    # # Brute force solution
    # # put all the values of all linked list int o a list
    # # sort the list and create a final list from those values
    # # k - length of linked lists
    # # n - max length of any linked list
    # # k*n - upper bound of number of values in all linked lists
    # values = []
    # # O(k*n)
    # for link in linked_lists: # O(k)
    #     while link: # O(n)
    #         values.append(link.val)
    #         link = link.next

    # sorted_vals = sorted(values)
    # result = Link(0)
    # pointer = result

    # # O(k*n)
    # for val in sorted_vals:
    #     pointer.next = Link(val)
    #     pointer = pointer.next
    
    # # Final runtime: O(k*n*log(k*n))
    # return result.next


    # look at the front value of all the linked lists
    # find the minimum, put it in the result linked list
    # 'remove' that value that we've added
    # keep going until there are no more values to add
    # copy_linked_lists = linked_lists[:] # O(k)
    # result = Link(0)
    # pointer = result

    # # Loop runs k*n times
    # while any(copy_linked_lists): # O(k)
    #     front_vals = [link.val for link in copy_linked_lists if link] # O(k)
    #     min_val = min(front_vals)# O(k)

    #     for i, link in enumerate(copy_linked_lists):# O(k)
    #         if link and link.val == min_val:
    #             pointer.next = Link(link.val)
    #             pointer = pointer.next
    #             copy_linked_lists[i] = link.next

    # # Final runtime O(k*n*k)
    # return result.next

    from collections import defaultdict
    from queue import PriorityQueue

    # keep a mapping of the value to the linked list
    # number -> list of linked list
    pq = PriorityQueue()
    val_to_links = defaultdict(list) # O(k)
    for link in linked_lists:
        val_to_links[link.val].append(link)
        pq.put(link.val)

    result = Link(0)
    pointer = result

    # Loop runs k*n times
    while len(val_to_links) != 0: # O(1)
        min_val = pq.get()# O(log(k))

        link = val_to_links[min_val].pop()
        pointer.next = Link(link.val)
        pointer = pointer.next

        if len(val_to_links[min_val]) == 0:
            del val_to_links[min_val] # O(1)
        if link.next:
            val_to_links[link.next.val].append(link.next) # O(1)
            pq.put(link.next.val)

    # Final runtime O(k*n*log(k))
    return result.next






    




