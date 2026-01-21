import numpy as np
arr1=np.array([10,20,30])
arr2=np.array([[60, 70, 80],
                 [90, 85, 88],
                 [75, 65, 95],
                 [55, 45, 60],
                 [99, 92, 89]])
print(np.zeros((2,3)))
print(np.ones((3,3)))
print(np.arange(1,10))
print(np.linspace(0,1,5))
marks = np.array([
    [78, 85, 90],
    [65, 70, 60],
    [92, 88, 95],
    [55, 45, 50],
    [99, 98, 97]])
total = marks.sum(axis=1)
average = marks.mean(axis=1)

print("Total:", total)
print("Average:", average)
