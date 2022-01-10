# Import allows us to make use of the bisect module.
import bisect

# This sorted list will be used throughout this lesson
# to showcase the functionality of the "bisect" method.
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
print(A)

# The bisect_left function finds the index of the target element. 
# In the event where duplicate entries are satisfying the target element, 
# the bisect_left function returns the left-most occurrence. 
# -10 is at index 1
print(bisect.bisect_left(A, -10))

# First occurrence of 285 is at index 6
print(bisect.bisect_left(A, 285))

# The bisect_right function returns the insertion point which comes after, 
# or to the right of, any existing entries of the target element in the list. 
# It takes in a sorted list as the first parameter and the target 
# element to be searched as the second parameter.
# Index position to right of -10 is 2.
print(bisect.bisect_right(A, -10)) 

# Index position after last occurrence of 285 is 9.
print(bisect.bisect_right(A, 285))

# bisect function is equivalent to bisect_right
# Index position to right of -10 is 2. (Same as bisect_right)
print(bisect.bisect(A, -10)) 

# Index position after last occurrence of 285 is 9. (Same as bisect_right).
print(bisect.bisect(A, 285))

# Functions insort_left and insort_right behave in a similar way to bisect_left 
# and bisect_right, only the insort functions insert at the index positions. 
print(A)
bisect.insort_left(A, 108)
print(A)

bisect.insort_right(A, 108)
print(A)