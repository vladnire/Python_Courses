"""
Given two strings, write a function to determine if one is a permutation of the other.
is_permutation_1 = "google"
is_permutation_2 = "ooggle"
"""

# Solution 1: Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(1)
def is_perm_1(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    str_1 = str_1.lower()
    str_2 = str_2.lower()
    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))
    n = len(str_1)

    for i in range(n):
        if str_1[i] != str_2[i]:
            return False

    return True


# Approach 2: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_perm_2(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    str_1 = str_1.lower()
    str_2 = str_2.lower()

    d = dict()
    for e in str_1:
        d[e] = 1 + d.get(e, 0)

    for e in str_2:
        if e in d:
            d[e] -= 1
        else:
            return False

    # The all() function returns True if all items in an iterable are True.
    return all(value == 0 for value in d.values())


is_permutation_1 = "google"
is_permutation_2 = "ooggle"

not_permutation_1 = "not"
not_permutation_2 = "top"
print(is_perm_1(is_permutation_1, is_permutation_2))
print(is_perm_1(not_permutation_1, not_permutation_2))

print(is_perm_2(is_permutation_1, is_permutation_2))
print(is_perm_2(not_permutation_1, not_permutation_2))