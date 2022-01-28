import random
import time


# O(n ** 2) worst case O(n logn) average, depending on the pivot 
def quick_sort(items):
    # print("---Quick Sort---")
    # print(items)

    if len(items) <= 1:
        return items

    #pivot = items[0]
    pivot = random.choice(items)
    less_than_pivot = [x for x in items if x < pivot]
    equal_to_pivot = [x for x in items if x == pivot]
    greater_than_pivot = [x for x in items if x > pivot]

    # print("Less than pivot:", less_than_pivot)
    # print("Pivot:", equal_to_pivot)
    # print("Greater than pivot:", greater_than_pivot)

    # Recursively divide the list into elements greater than, less than,
    # and equal to a chose pivot, then combine the lists as below using recursion.
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

# items = [2, 9, 5, 3, 8, 1, 4]
# print(quick_sort(items))

items = [random.randint(1, 100000) for _ in range(100000)]
start = time.perf_counter()
quick_sort(items)
print(time.perf_counter() - start)