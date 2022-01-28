''' Implementations of various search algorithms'''
from typing import List
from random import randint


def load_names(path: str) -> List[str]:
    """Return a list of names from the given file."""
    print(f"Loading names from path `{path}`... ", end="", flush=True)
    with open(path, encoding="utf8") as text_file:
        names = text_file.read().splitlines()
        print("ok")
        return names


basic_names = load_names("names.txt")
sorted_names = load_names("sorted_names.txt")


def random_find(items, search_val):
    while True:
        rand_dex = randint(0, len(items) - 1)
        rand_el = items[rand_dex]
        if rand_el == search_val:
            return rand_dex


els = [3, 4, 5, 5, 9]
# print(random_find(els, 4))
# print(random_find(basic_names, "Dominique Bovard"))


def linear_find(items, search_val):
    for idx, el in enumerate(items):
        if el == search_val:
            return idx
    return None


linear_find(els, 4)
print(linear_find(basic_names, "Dominique Bovard"))