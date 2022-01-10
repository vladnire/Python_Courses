"""
Given an array of sorted integers and a key 
return the index of the first occurrence of that key from the array.
"""

# Linear O(n)
def find_lin(A, target):
  for i in range(len(A)):
    if A[i] == target:
      return i
    return None


# O(logn) binary search
def find_bin(a, target):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        if target < a[mid]:
            high = mid - 1
        elif target > a[mid]:
            low = mid + 1
        else:
            # The first occurrence is on the first index
            if mid - 1 < 0:
                return mid
            if a[mid - 1] != target:
                return mid
            high = mid - 1

    return False

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
x = find_bin(A, target)
print(x)