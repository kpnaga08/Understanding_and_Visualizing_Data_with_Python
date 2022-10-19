Question 1
In the code block below, generate 3 normal random variables with mean 100 and standard deviation 1. 

This will require about 4 lines of code. Use the functions provided in this outline.

Import the numpy library
Set the seed to 123 to initialize environment so random variables are replicated according to the grader. (hint: np.random.seed(?))
Generate three random normal variables with mean 100 and standard deviation 1 and assign them to a variable named sample. (hint: sample = np.random.normal(?,?,?))
Print the variable sample.
The question marks in the hints indicate input parameters.

Choose the answer that matches your result to three decimal places.

Reference Documentation

https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.seed.html
https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.normal.html



# Write your function here
import numpy as np
import random

np.random.seed(123)
sample = np.random.normal(100, 1, size=(1, 3))
print(sample)


[[  98.9143694   100.99734545  100.2829785 ]]




99.914 101.937 100.282
98.914  100.997  100.283
100.915   99.997  101.283
99.922 100.103 100.819
99.822  100.093  100.719

Answer: 98.914  100.997  100.28


Question 2
Generating random samples from a population lies at the heart of statistics. In the code block below, draw a sample of size 10 from a set containing the integers 1 through 100.

This will require about 5 lines of code. Use the functions provided in this outline.  

Import the numpy library
Set the seed to 123 to initialize environment so random variables are replicated according to the grader. (hint: np.random.seed(?))
Create a vector called population, and put the numbers 1-100 into the population list. (hint: np.arange(?,?))
Generate a sample with length 10 from the population. (hint: sample = np.random.choice(?, ?)) and assign the output to a variable named sample.
Print the variable sample.
The question marks in the hints above indicate input parameters.

Reference Documentation

https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.seed.html
https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.arange.html
https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.choice.html


import numpy as np
import random
np.random.seed(123)
population = np.random.choice(np.arange(0, 100), 100, replace=False)
sample = []
for i in range(100):
    sample.append(np.random.choice(population, 10))
sample = np.array(sample)



[[42 43 20 91 74 54  8 87 41 70]
 [49 64 21 50 47 15 10 61 71  1]
 [26 50 96 40 60 53 13 68 95 83]
 [20 96 13 72 93 81 99  5 10 86]
 [40 20  7 61 61 91 50 60  1 70]
 [89 99 30 78 13 17 28 38 96 78]
 [ 3 17 16 82 56 11 74 44 87 56]
 [32 11  6 52 67 18 71 65 85 73]
 [48 23 28 74 72 43 29 91  9 44]
 [28 66 99 80 43 14 30 78 78 63]
 [ 3 30 15  4 58 69  3  4 39 53]
 [58 23 28 14 28 29 32 98 84 97]
 [54 78 80 91 38 72 58 74 23 81]
 [83 91 66 71 10 50 40 66 17 12]
 [55 73 62  0  4 20 64 78 88 25]
 [16 95  1 73 66 49 67 94 24 99]
 [29 18 53  2 31 42 54  2 68 46]
 [63 88 33 12 70 92 55 46 87 72]
 [62 70 51 38 74 19 45 25  7  8]
 [87 49 86 34 12 78 49 99 41 75]
 [97 70  0 67 87 93 91 17 47 40]
 [72 41 67 88 77 21 98  2 21 76]
 [46 49 77 73 62 92 50 97 24  8]
 [83 82 97 79 18 94 24 94 67 97]
 [86 75 72  5 46 34 93 99 40 83]
 [26 17 28  8 93 86 97 51 49 82]
 [92 83 24 82 32 46 33 55 98 33]
 [21 28 57 32 39 32 99 88 21 43]
 [68 90 40 83 50 93 94 96 57  9]
 [10 77 46 70 50 97 75 13 35 25]
 [21 49  3 24 30  8 25 53 10 88]
 [15 53 81 20 35  6 57 57 12 91]
 [79 61 82 57 33 83 89 61 37  3]
 [28 13  3 16 58 46 49 38 75 41]
 [52 26 19 11 82 54 81 56 87 12]
 [85 32 34 34 67 35 76 85 94 12]
 [51 39 12 81 85  2 82 98 51 28]
 [12 26 98 22 93 34 40 41 31 62]
 [39  7 31 33 18 45 16 68 26 26]
 [52 98 27  8 17 21 35 29 56 15]
 [43 68 31 75 91  5 58 98 34 47]
 [23 34 77 34 11 59 13 41 37 42]
 [28 68 54 69 84 13 76 85 34 20]
 [89 53 42 51 74 64 95 43 52 24]
 [35 69 80 80 81 91 61 38  8 19]
 [33 11 86 35 36 39 15 85 18 26]
 [13 60 11  5 48  9 82 88 68 18]
 [53 75 58 46 68 33 47 79 20 81]
 [79 36 45 19 22 35 90 91 33 43]
 [81  2  3 74  5  5 64 33  4  2]
 [ 9 11 74 88 35 98 90 90 87 21]
 [ 3 45 35 84 93 19 89 29 47 52]
 [64 89 41 40  0 34 26 25 67 66]
 [91 66 20 71 45 43 61  6 29 86]
 [80 12 67 13 69 36 62  8 75 31]
 [ 0 47 49 27 67 82 87  3 97 22]
 [55 97  9 11 27 11  4 78 25 34]
 [63 76 80 69 31 19 68 82 50 74]
 [94 62 16 88  1  7 19 14 39 16]
 [ 9 92 53 72  3 93 73  9 52 11]
 [28 78 70 13 53 96 86 11 24 97]
 [83 14 34 12 42 69  0 36 51 35]
 [92 53 92 70 83 91 59 57 38 17]
 [41 19 79  6 49 19 12 13 34 60]
 [36 93 70 28 78 66 81 42 57 90]
 [85 24 71 66 31 24 65 40 66 29]
 [ 3 20 43 21 35 43  7 39 93 96]
 [60 67 60 29 34 31 17  9 78 38]
 [30 17 89 58 65 87 64 55 48 46]
 [77 37 32 12 88 13  4  0 77 48]
 [18  3 80 54 39 71 31 33  8 99]
 [77 37 44 56 45 55 49  8 36 42]
 [29 49 99 13 44 29 44 13 20 33]
 [57 44 98 86 24 22 65 84 95 41]
 [25 23 43 90 70  4 74 88 27  6]
 [72 41 51 96 35 67 75 39 62 84]
 [53 98 47  6 51 79 58  6 90 44]
 [93 25 64  9 34 83 66 43 76 49]
 [38 16 54 49 37 83 68 74 29 32]
 [63 41 37 51 29 60 66 87 91 76]
 [35 25 17 12 93 68 37 72 14 11]
 [56 65 87 47 33 36 94 20 61 32]
 [32 56 21 54 89 77 32 71  0 43]
 [56 44 36 12  1 89  3 29 88 51]
 [68 93 29 31 77 84  2 98  9 10]
 [69 22 82 72 98 88 89 28 99 66]
 [65 95 20 44 18 40 86 63 46 96]
 [77  9 85 51 91 14 73 43 85  2]
 [97 39 81 90  8 81 54 40 95  0]
 [95 62 28 14 95 52  4 92 50 19]
 [40 18 10 97 75 21 41 79 96  4]
 [43  2 81 44 90 78 42 65 84 11]
 [77 53 30 87 92 71  5 56  9 80]
 [35 63 14 57  8 13 49  9 59 79]
 [65 38  1 16 63 21 10  1 72 27]
 [70 67 98 84 59 31 42 44 20 59]
 [75 72 71 90 49 13 62 24 38 40]
 [58 34 53 34  8 68  1 10 69 35]
 [79 33 30 12 40 24 27 41 59  6]
 [77 62 79 68 82 95 77  2  7 52]]


Select the answer matching your sample below.


67 93 99 18 84 58 87 98 97 48

-0.2144699617662135 0.4160333636063626 0.02927226924712613 -0.5072293848619751 2.6014747539872567 0.17141327084834654 -0.21195901381927462 -0.37671989689029883 0.1799644167541328 -0.8515596897956541
110  67  93  99 103  18  84 107  58  87

0.70579387 -0.69160146  1.12461493  0.36499493  0.19864388 -0.85155969
 -2.88011494 -0.77227959  0.36499493  0.809468

12 14 57 79 70 72 36 25 67 9

9 25 68 88 80 49 11 95 53 99

Answer: 67 93 99 18 84 58 87 98 97 48


