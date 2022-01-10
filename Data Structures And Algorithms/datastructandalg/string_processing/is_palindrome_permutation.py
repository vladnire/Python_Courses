"""
Determine if a string is a palindrome permutation.
Given a string, write a function to check if it is a permutation of a palindrome.
Palindrome: A word or phrase that is the same forwards and backward.
Permutation: A rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
"""

def is_palin_perm(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    d = dict()

    for e in input_str:
        d[e] = 1 + d.get(e, 0)

    odd_count = 0
    for e in d.values():
        if e % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif e % 2 != 0 and odd_count != 0:
            return False

    return True 


palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))