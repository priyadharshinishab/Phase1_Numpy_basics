import numpy as np
marks=np.array([[50,39,72],
            [34,50,35],
            [60,98,78],
            [88,95,93],
            [25,60,45]])
average = marks.mean(axis=1)
print("Average marks:", average)
high_scorers = marks[average > 75]
print("Students with average > 75:\n", high_scorers)
marks[marks < 40] = 0
print("Marks after replacing < 40 with 0:\n", marks)
