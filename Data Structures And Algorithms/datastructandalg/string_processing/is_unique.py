"""
Your task is to implement an algorithm to determine if a string has all unique characters.
Assume that the input string will only contain alphabets or spaces.
"""

def is_unique(input_str):
    temp = set()

    for e in input_str:
        if e in temp:
            return False
        else:
            temp.add(e)

    return True

print(is_unique("abCDefGh"))
print(is_unique("nonunique"))

# Solution 1
# It uses a Python dictionary to solve the problem 
# in linear time complexity, but because of the additional 
# data structure, the space complexity is also linear.
def is_unique_1(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True


# Solution 2
# Very concise and straightforward. 
# In this solution, we make use of set(). 
# Let’s find out how by having a look at the implementation in Python.
def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)


# Solution 3
def is_unique_3(input_str):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True


unique_str = "AbCDefG"
non_unique_str = "non UniqueSTR"

print("Unique String")
print(unique_str)
print("Non-Unique String")
print(non_unique_str, "\n")

print("Solution 1 where input string is unique string")
print(is_unique_1(unique_str))
print("Solution 1 where input string is non-unique string")
print(is_unique_1(non_unique_str), "\n")


print("Solution 2 where input string is unique string")
print(is_unique_2(unique_str))
print("Solution 2 where input string is non-unique string")
print(is_unique_2(non_unique_str), "\n")

print("Solution 3 where input string is unique string")
print(is_unique_3(unique_str))
print("Solution 3 where input string is non-unique string")
print(is_unique_3(non_unique_str))