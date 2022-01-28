import random
from timing import timed_func


@timed_func
# O(n ** 2)
def bubble_sort(items):
    for i in range(len(items)):
        sorted = True
        for j in range(len(items) - i - 1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                sorted = False
        if sorted:
            break

    return items


# items = [2, 8, 5, 3, 8, 1]
# print(items)
# print(bubble_sort(items))

items = [random.randint(1, 100000) for _ in range(100000)]
bubble_sort(items)