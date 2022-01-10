"""
Given two numbers, find their product using recursion. 
In Python, we usually use the * operator to multiply two numbers, 
but you have to use recursion to solve this challenge.
hint: 5 * 3 = 5 + 5 + 5 = 15
"""

def recursive_multiply(x, y):
    # This cuts down on the total number of
    # recursive calls and prevents 
    # RecursionError: maximum recursion depth exceeded in comparison
    if x < y:
        return recursive_multiply(y, x)

    if y == 1:
        return x

    return x + recursive_multiply(x, y - 1)


print(recursive_multiply(5, 3))