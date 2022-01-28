from re import search


def binary_iterative(elements, search_items):
    """ Return the index of the search_item or None"""
    left, right = 0, len(elements) - 1

    while left <= right:
        #mid_idx = (left + right) // 2 # may overflow
        mid_idx = left + (right - left) // 2 # can't overflow
        mid_el = elements[mid_idx]

        if mid_el == search_items:
            return mid_idx
            
        if mid_el < search_items:
            left = mid_idx + 1
        elif mid_el > search_items:
            right = mid_idx - 1

    return None


def binary_leftmost(elements, search_item):
    tentative = binary_iterative(elements, search_item)
    if tentative is None:
        return None
    while elements[tentative] == search_item and tentative >= 0:
        tentative -= 1
    return tentative + 1


def binary_recursive(elements, search_item, idx_mod=0):

    while len(elements) > 0:
        mid_idx = len(elements) // 2
        mid_el = elements[mid_idx]

        if mid_el == search_item:
            return mid_idx + idx_mod

        if mid_el < search_item:
            return binary_recursive(
                elements[mid_idx+1:],
                search_item,
                idx_mod + mid_idx + 1)
        elif mid_el < search_item:
            return binary_recursive(
                elements[:mid_idx],
                search_item,
                idx_mod)

    return None


els = [3, 4, 5, 5, 9, 9, 10]
print(binary_iterative(els, 5))
print(binary_iterative(els, 9))
print(binary_leftmost(els, 5))
print(binary_recursive(els, 5))