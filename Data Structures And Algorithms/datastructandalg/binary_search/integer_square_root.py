"""
You are required to write a function that takes a non-negative integer, 
k, and returns the largest integer whose square is less than or equal to the specified integer k.
Use binary search.
"""
def integer_square_root(k):
    low = 0
    high = k 

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= k:
            low = mid + 1
        else:
            high = mid - 1
        
    return low - 1

print(integer_square_root(300))