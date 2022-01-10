"""
To generate a member of the sequence from the previous member, 
read off the digits of the previous member and 
record the count of the number of digits in groups of the same digit.
eg: 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ..
"""
def next_number(s):
    result = []
    i = 0

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        result.append(str(count) + s[i])
        i += 1

    return ''.join(result)


s = "1"
print(s)
n = 4
for i in range(n-1):
    s = next_number(s)
    print(s)   