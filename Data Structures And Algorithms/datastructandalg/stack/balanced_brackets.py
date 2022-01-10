import stack


def my_sollution(paren_str: str) -> bool:
    s = stack.Stack()
    brackets = {')': '(', ']': '[', '}': '{'}

    for e in paren_str:
        if e in brackets.values():
            s.push(e)
        elif e in brackets.keys():
            if s.is_empty() or s.pop() != brackets[e]:
                return False

    if not s.is_empty():
        return False

    return True

print("String : (((({})))) Balanced or not?")
print(my_sollution("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(my_sollution("[][]]]"))

print("String : [][] Balanced or not?")
print(my_sollution("[][]"))


def is_paren_balanced(paren_str: str) -> bool:
    s = stack.Stack()
    is_balanced = True
    index = 0

    while index < len(paren_str) and is_balanced:
        paren = paren_str[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_matched(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


def is_matched(p1: str, p2: str) -> bool:
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))