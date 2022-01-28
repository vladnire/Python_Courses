import bisect
fruits = ['apple', 'banana', 'banana', 'orange', 'pineapple']

# Where can I put stuff to make sure that this list maintains sorted order
print(bisect.bisect(fruits, "banana"))
print(bisect.bisect_right(fruits, "banana"))
print(bisect.bisect_left(fruits, "banana"))

# number of occurences of item
print(bisect.bisect_right(fruits, "banana") - bisect.bisect_left(fruits, "banana"))

bisect.insort_left(fruits, "kiwi")
print(fruits)