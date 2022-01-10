"""
Given: An array of non-negative digits that represent a decimal integer.
Problem: Add one to the integer. Assume the solution still works even 
if implemented in a language with finite-precision arithmetic.
"""
print("One line")
A = [1, 4, 9]
s = ''.join(map(str, A))
print(int(s) + 1)


print("Algorithm")
def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    if arr[0] == 10:
        arr[0] == 1
        arr.append(0)
    return arr


A1 = [1, 4, 9]
print(plus_one(A1))
A2 = [9, 9, 9]
print(plus_one(A2))