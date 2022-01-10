"""
Given an array of n distinct integers sorted in ascending order, 
write a function that returns a fixed point in the array. 
If there is not a fixed point, return None.
A fixed point in an array A is an index i such that A[i] is equal to i.
"""

# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_linear(a):
    for i, v in enumerate(a):
        if i == v:
            return v
    return None


# The list is sorted.
# The list contains distinct elements.
# Use binary search
# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_fixed_point(a):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] < mid:
            low = mid + 1
        elif a[mid] > mid:
            high = mid - 1
        else:
            return a[mid]   
    return None


# Fixed point is 3:
A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]
print("Linear Approach")
print(A1)
print(find_fixed_point_linear(A1))
print(A2)
print(find_fixed_point_linear(A2))
print(A3)
print(find_fixed_point_linear(A3))
print(A1)
print(find_fixed_point(A1))
print(A2)
print(find_fixed_point(A2))
print(A3)
print(find_fixed_point(A3))