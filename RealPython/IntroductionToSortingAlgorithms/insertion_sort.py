import random
from timing import timed_func


@timed_func
# O(n ** 2)
def insertion_sort(items):
    for i in range(1, len(items)):
        j = i - 1
        current_item  = items[i]

        while j >= 0 and current_item < items[j]:
            # Break when the current element is in the right place
            items[j + 1] = items[j] # moving item up
            j -= 1

        items[j + 1] = current_item # insert current item in the correct spot

    return items


# items = [2, 9, 5, 3, 8, 1]
# print(items)
# print(insertion_sort(items))

items = [random.randint(1, 100000) for _ in range(100000)]
insertion_sort(items)