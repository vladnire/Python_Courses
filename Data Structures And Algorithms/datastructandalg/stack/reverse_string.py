import stack

def reverse_string(input_str: str) -> str:
    s = stack.Stack()

    for e in input_str:
        s.push(e)

    reversed = ""
    while not s.is_empty():
        reversed += s.pop()

    return reversed


input_string = "12312!!!aaa###"
print(reverse_string(input_string))