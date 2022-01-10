"""
Is it possible to advance from the start of the array 
to the last element given that the maximum you can 
advance from a position is based on the value of the 
array at the index you are currently present on?
"""
def array_advance(arr):
    furthest_reach = 0
    i = 0
    last_idx = len(arr) - 1
    while i <= furthest_reach and furthest_reach< last_idx:
        furthest_reach = max(furthest_reach, arr[i] + i)
        i += 1
    return furthest_reach >= last_idx

# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(A)
print("Possible to navigate to last index in A?\n" + str(array_advance(A)))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(A)
print("Possible to navigate to last index in A?\n" + str(array_advance(A)))