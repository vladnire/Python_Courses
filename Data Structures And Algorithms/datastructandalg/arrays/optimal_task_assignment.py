"""
Assign tasks to workers so that the time it takes to 
complete all the tasks is minimized given a count of 
workers and an array where each element indicates 
the duration of a task.
"""

A = [6, 3, 2, 7, 5, 5]
A = sorted(A)
for i in range(len(A)//2):
    print(A[i], A[~i])
    
# So ~i on line 6 is the bitwise complement operator 
# which puts a negative sign in front of i and subtracts 1 from it. 
# Thus, the negative numbers as indexes mean that you count 
# from the right of the array instead of the left.
#  So, A[-1] refers to the last element, A[-2] is the second-last, and so on.