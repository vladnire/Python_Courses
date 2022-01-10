"""
You are required to write a function that determines 
the index of the smallest element of the cyclically shifted array.
An array is “cyclically shifted” if it is possible to 
shift its entries cyclically so that it becomes sorted.
eg: A = [4, 5, 6, 7, 1, 2, 3]
"""

def find(a):
    low = 0
    high = len(a) - 1

    while low < high:
        mid = (low + high) // 2
        if a[mid] > a[high]:
            low = mid + 1
        elif a[mid] <= a[high]:
            high = mid

    return low

A = [4, 5, 6, 7, 1, 2, 3]
idx = find(A)
print(A[idx])