"""
Given two sorted arrays, A and B, determine their intersection. 
What elements are common to A and B?
"""
#A = [2, 3, 3, 5, 7, 11]
#B = [3, 3, 7, 15, 31]
#print(set(A).intersection(B))

def intersect_sorted_array(a, b):
    i = 0
    j = 0
    intersection = []

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if i == 0 or a[i] != a[i-1]:
                intersection.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    return intersection

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]
print(A)
print(B)
print(intersect_sorted_array(A, B))