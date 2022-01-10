import stack


def convert_int_to_bin(nr: int) -> str:
    
    if nr == 0:
        return "0"

    s = stack.Stack()

    while nr > 0:
        s.push(nr % 2)
        nr //= 2

    binary_str = ""
    while not s.is_empty():
        binary_str += str(s.pop())

    return binary_str


print(convert_int_to_bin(242))
print(convert_int_to_bin(56))
print(convert_int_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))
print(int(convert_int_to_bin(56),2)==56)