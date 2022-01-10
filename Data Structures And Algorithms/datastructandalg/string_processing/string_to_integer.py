"""
Given some numeric string as inpu, you have 
to convert the string you are given to an integer.
eg: "123" -> 123
hint: 123 = 100 + 20 + 3 = 1 * 100 + 2 * 10 + 3 * 1
"""
def str_to_int(input_str):
    output_int = 0

    if input_str[0] == '-':
        negative = True
        start_idx = 1
    else:
        negative = False
        start_idx = 0

    for i in range(start_idx, len(input_str)):
        place = 10 ** (len(input_str) - (i + 1))
        digit = ord(input_str[i]) - ord('0')
        output_int += place * digit

    if negative:
        return -output_int

    return output_int


s = "554"
x = str_to_int(s)
print(type(x))

s = "123"
print(str_to_int(s))

s = "-123"
print(str_to_int(s))