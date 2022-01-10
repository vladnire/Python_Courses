"""
Given an array of integers, return True or False if 
the array has two numbers that add up to a specific target. 
You may assume that each input would have exactly one solution.
"""

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_brute_force(arr, target):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                print(arr[i], arr[j])
                return True

    return False

A = [-2, 1, 2, 4, 7, 11]
print(A)
target = 13
print(two_sum_brute_force(A,target))
target = 20
print(two_sum_brute_force(A,target))

# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_hash_table(arr, target):
    ht = dict()
    for i in range(len(arr)):
        if arr[i] in ht:
            print(ht[arr[i]], arr[i])
            return True
        else:
            ht[target - arr[i]] = arr[i]
    
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 13
print(A)
print(two_sum_hash_table(A,target))

# Time Complexity: O(n)
# Space Complexity: O(1)
# This approach assumes that the array is sorted
def two_sum(arr, target):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])
            return True
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1

    return False

A = [-2, 1, 2, 4, 7, 11]
target = 13
print(A)
print(two_sum(A,target))