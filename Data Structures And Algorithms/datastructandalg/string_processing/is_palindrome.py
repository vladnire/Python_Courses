"""
How to test whether a string is a palindrome in Python.
A palindrome is a word, number, phrase, or any other 
sequence of characters that reads the same forward as it does backward.
"""
s = "Was it a cat I saw?"

# Solution 1
# Solution uses extra space proportional to size of string "s"
s = ''.join([i for i in s if i.isalnum()]).replace(" ", "").lower()
print(s == s[::-1])


# Solution 2
def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        # Skip in case we don't have alphanum chars
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True

print(is_palindrome(s))