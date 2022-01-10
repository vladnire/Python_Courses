"""
Determine whether two strings are anagrams of each other.
An anagram is when two strings can be written using the same letters.
"rail safety" = "fairy tales"
"William Shakespeare" = "I am a weakish speller"
"""

# Solution 1
s1 = "fairy tales"
s2 = "rail safety"

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

# Requires n log n time (since any comparison 
# based sorting algorithm requires at least 
# n log n time to sort).
print(sorted(s1) == sorted(s2))


# Solution 2
def is_anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    ht = {}

    for e in s1:
        ht[e] = 1 + ht.get(e, 0)

    for e in s2:
        if e in ht:
            ht[e] -= 1
        else:
            ht[e] = 1

    for e in ht:
        if ht[e] != 0:
            return False

    return True


s1 = "fairy tales"
s2 = "rail safety"  
print(is_anagram(s1, s2))