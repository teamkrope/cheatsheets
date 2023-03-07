# INSTALLING NumPy ----------------------------------------
# pip install numpy


# NumPy CODEBASE ----------------------------------------
# https://github.com/numpy/numpy


# IMPORTING NumPy ----------------------------------------
import numpy as np


# CREATING NumPy ARRAYS ----------------------------------------
# From Python List
np.array([1, 2, 3])

# 1D Array with Zeros
np.zeros(5)

# 2D Array with Ones
np.ones((2, 3))

# Array with Linspace
np.linspace(0, 20, num=10)

# Array with a Range
np.arange(10)

# Array with a Range and a Step
np.arange(5, 51, 5)

# Array with Random Values
np.random.rand(3, 2)

# Array with Custom Values
np.array([[1, 2], [3, 4]])


# ACCESSING ELEMENTS IN ARRAYS ----------------------------------------
# Array
arr1 = np.array([1, 2, 3])

# Access the first element
arr1[0]

# Access elements from index 1 to 3
arr1[1:3]

# Access elements from the start to index 2
arr1[:2]

# Access elements from index 1 to the end
arr1[1:]

# Access the last element
arr1[-1]


# SLICING ----------------------------------------
# Array 
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slice rows from index 1 to 2
arr2[1:3, :]

# Slice columns from index 0 to 1
arr2[:, 0:2]


# CONCATENATING ----------------------------------------
# Arrays
a1 = np.array([1, 2, 3])
b1 = np.array([4, 5, 6])

# Concatenate
np.concatenate((a1, b1))

# Vertical
np.vstack((a1, b1))

# Horizontal
np.hstack((a1, b1))


# STACKING ----------------------------------------
# Arrays
a2 = np.array([1, 2, 3])
b2 = np.array([4, 5, 6])

# with axis 0
np.stack((a2, b2), axis=0)

# with axis 1
np.stack((a2, b2), axis=1)


# SPILITING ----------------------------------------
# Arrray
arr3 = np.array([1, 2, 3, 4, 5, 6])

np.split(arr3, 3)
print(np.split(arr3, [2, 4]))


# BROADCASTING ----------------------------------------
a3 = np.array([1, 2, 3])
b3 = 2

# Multiply 
a3 * b3

# Plus
a3 + b3


# UNIVERSAL FUNCTIONS ----------------------------------------
# Array 
arr4 = np.array([1, 2, 3])

# Sine
np.sin(arr4)

# Cosine 
np.cos(arr4)

# Exponential
np.exp(arr4)


# AGGREGATE FUNCTIONS ----------------------------------------
# Array 
arr5 = np.array([1, 2, 3])

# Minimum
arr5.min()

# Maxiumum
arr5.max()

# Varience
arr5.var()

# Sum
arr5.sum()

# Mean
arr5.mean()

# Standard Deviation
arr5.std()

# Any
arr5.any()

# All
arr5.all()

# Product
arr5.prod()


# ARRAY MANIPULATION ----------------------------------------
# Transposing an Array
arr6 = np.array([[1, 2], [3, 4]])

arr6.transpose()

# Reshaping an Array
arr7 = np.array([1, 2, 3, 4])

arr7.reshape((2, 2))

# Flattening an Array
arr8 = np.array([[1, 2], [3, 4]])

arr8.flatten()


# ITERATING ----------------------------------------
arr9 = np.array([[1, 2], [3, 4]])

for x in np.nditer(arr9):
    print(x)


# MASKING ----------------------------------------
arr10 = np.array([1, 2, 3, 4, 5, 6])

arr10[arr10 > 3]


# MESHGRID ----------------------------------------
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

X, Y = np.meshgrid(x, y)
print(X, Y)