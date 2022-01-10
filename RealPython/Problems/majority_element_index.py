def majority_element_indexes(lst: list) -> list:
    """
    Return a list of indexes of the majority element
    Majority element is the element that appears
    more than floor(n/2) times where n is list length
    If there is not majority element return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([])
    []
    >>> majority_element_indexes([1, 1, 1, 1, 2, 2, 3])
    [0, 1, 2, 3]
    """
    n = len(lst)
    majority_times = n // 2
    output = []
    counter_dict = {}

    for e in lst:
        counter_dict[e] = counter_dict.get(e, 0) + 1

    for i, v in enumerate(lst):
        if counter_dict[v] > majority_times:
            output.append(i)

    return output


def majority_element_indexes_solution(lst: list) -> list:
    from collections import Counter
    
    if lst == []:
        return []

    count = Counter(lst)
    #top_elems = sorted (
    #    count.keys(),
    #    key=lambda x: -count[x]
    #) # O(nlogn)
    #maj_elem = top_elems[0]

    top_count = max(count.values()) # O(n)
    maj_elem = [
        elem for elem, count
        in count.items if count == top_count
    ][0] # O(n)
    
    if count[maj_elem] > len(lst) // 2:
        return [
            i for i, elem in enumerate(lst)
            if elem == maj_elem
        ] # O(n)

    return []