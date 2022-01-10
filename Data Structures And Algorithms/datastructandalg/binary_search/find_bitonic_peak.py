"""
bitonically sorted, an array that starts off with increasing 
terms and then concludes with decreasing terms. 
In any such sequence, there is a “peak” element which is the
largest element in the sequence.
eg: 1, 2, 3, 4, 5, 4, 3, 2, 1
We assume that a “peak” element will always exist.
The sequence for this problem does not contain any duplicates.
"""
def find_bitonic_peak(a):
    low = 0
    high = len(a) - 1

    # There should be at least 3 elements for bitonic sequence
    if len(a) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2

        if mid - 1 > 0:
            mid_left = a[mid - 1]
        else:
            mid_left = float("-inf")  

        if mid + 1 < len(a):
            mid_right = a[mid + 1]
        else:
            mid_right = float("inf")

        if mid_left < a[mid] and a[mid] < mid_right:
            low = mid + 1
        elif mid_left > a[mid] and a[mid] > mid_right:
            high = mid - 1
        elif mid_left < a[mid] and a[mid] > mid_right:
            return a[mid]

    return None
        

A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A))
A = [1, 2, 3, 4, 5]
print(find_bitonic_peak(A))
A = [5, 4, 3, 2, 1]
print(find_bitonic_peak(A))