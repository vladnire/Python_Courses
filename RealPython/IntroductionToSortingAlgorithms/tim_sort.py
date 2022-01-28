import random
from timing import timed_func
from merge_sort import merge_sorted_lists


# A simplified TimSort
# Uses both insertion and merge-sort strategies to produce a 
# stable, fast sort that uses existing runs in the data.


def insertion_sort(items, left=0, right=None):
    if right is None:
        right = len(items) - 1

    # sort subsection instead of full list
    for i in range(left + 1, right + 1): 
        j = i - 1
        current_item  = items[i]

        while j >= left and current_item < items[j]:
            # Break when the current element is in the right place
            items[j + 1] = items[j] # moving item up
            j -= 1

        items[j + 1] = current_item # insert current item in the correct spot

    return items


# Python sorted() function
# O(n logn)
@timed_func
def tim_sort(items):
    min_subsection_size = 32

    for i in range(0, len(items), min_subsection_size):
        insertion_sort(items, 
                        i, 
                        min((i + min_subsection_size - 1), len(items) - 1))


    size = min_subsection_size
    while size < len(items):
        for start in range(0, len(items), size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (len(items)- 1))

            merged_array = merge_sorted_lists(
                            items[start:mid + 1], 
                            items[mid + 1:end + 1])

            items[start:start + len(merged_array)] = merged_array

        size *= 2

    return items


# items = [2, 9, 5, 3, 8, 1, 4]
# print(tim_sort(items))

items = [random.randint(1, 100000) for _ in range(100000)]
tim_sort(items)
