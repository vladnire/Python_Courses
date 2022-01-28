""" Sum of Integers Up To n
    Write a function, add_it_up, which returns the sum of the integers from 0
    to the single integer input parameter.
    The function should return 0 if a non-integer is passed in.
"""


def add_it_up(n):
    if not isinstance(n, int) or n <= 0:
        return 0
    
    sum = 0
    for el in range(n + 1):
        sum += el

    return sum

    # course solution
    # try:
    #     result = sum(range(n + 1))
    # except TypeError:
    #     result = 0
    # return result