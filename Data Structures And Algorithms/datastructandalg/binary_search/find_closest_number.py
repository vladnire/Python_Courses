"""
In this lesson, we will be given a sorted array and a target number. 
Our goal is to find a number in the array that is closest to the target number.
The array may contain duplicate values and negative numbers.
"""
A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]

def find_closest_num(a, target):
    min_diff = min_diff_left = min_diff_right = float("inf")
    low = 0
    high = len(a) - 1
    closest_num = None

    # Edge case for empty list
    if len(a) == 0:
        return None
    # Edge case for list with 1 element
    if len(a) == 1:
        return a[0]

    while low <= high:
        mid = (low + high) // 2

        # Ensure to not read beyond the bounds
        if mid + 1 < len(a):
            min_diff_right = abs(a[mid + 1] -  target)
        if mid > 0:
            min_diff_left = abs(a[mid - 1] - target)

        # Check if the absolute value between left
        # and right elements is smaller that any seen prior
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = a[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = a[mid + 1]

        # Move the mid-point appropriately with binary search
        if a[mid] < target:
            low = mid + 1
        elif a[mid] > target:
            high = mid - 1
            if high < 0:
                return a[mid]
        # The element is the target
        else:
            return a[mid]

    return closest_num

print(find_closest_num(A1, 11))
print(find_closest_num(A2, 4))