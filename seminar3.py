import numpy as np

# Lambda in python
medie = lambda a, b: (a + b) / 2  # noqa: E731

medie_vector = lambda vector: np.mean(vector)  # noqa: E731

# Generator in python
# We do not have comprehension for tuples in python
# This is the definition of a generator
patrate = ((x + 1)**2 for x in range(10))
print(list(patrate))

# We observe patrate is of type generator, an instance of the generator class
print(type(patrate), patrate)

# A generator only computes the next value when asked for it, it does not store all the values in memory


# Creates a matrix of (3,5) populated with random values between 1 and 10 using numpy
matrix = np.random.randint(1, 11, size=(3, 5))

# New way of doing random in numpy
generator = np.random.Generator(np.random.PCG64())
matrix2 = generator.integers(1, 11, size=(3, 5))

print(matrix)
print(matrix2)

vector = generator.integers(1, 11, 15)

# order args
# C Continuous = row major
# F Fortran    = column major
# A Any        = based on the OS / runtime
matrice3 = np.ndarray(shape=(3, 5), dtype=int, buffer=vector.data, order='C')
print(vector)
print(matrice3)


# We need to create 3 more to have enough data in the vector to create a 3x5 matrix
vector2 = generator.integers(1, 11, 15 + 3)
print(vector2)

# We can also ignore the first 3 elements from the buffer
# Offset is always a buffer in terms of bytes
matrice4 = np.ndarray(shape=(3,5), dtype=int, buffer=vector2, order='C', offset=3*(vector.itemsize))
print(matrice4)

# Dictionary comprehension
# Dictionary for the square of the first 10 natural numbers
dict1 = {x: (x + 1)**2 for x in range(10)}
print(dict1)

# Dict with keys in the form of 'Stud_1', 'Stud_2', ... 'Stud_10' and values of random numbers between 1 and 10
dict2 = {f'Stud_{x}': generator.integers(1, 6, generator.integers(1,11)) for x in range(10)}
print(dict2)

# We can also use the zip function to create a dictionary
keys = [f'Stud_{x}' for x in range(10)]
values = [generator.integers(1, 6, generator.integers(1,11)) for x in range(10)]

dict3 = dict(zip(keys, values))

print(dict3)