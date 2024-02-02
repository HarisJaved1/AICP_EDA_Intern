# in this program we will be learning about Numpy

# first we will import numpy 
import numpy as np  

#Even Intgers from 30 to 70

even_int = np.arange(30, 71, 2)
print(even_int)

#Generate an Array of 15 random numbers from a standard normal distribution

rand_numbers = np.random.randn(15)
print(rand_numbers)

#Computing the Cross-Product of two matrices 

a1 = np.array([12,22, 33])
a2 = np.array([45, 15, 26])

cross_product = np.cross(a1, a2)
print(cross_product)

#computing the determinant of an array
#Creating a 2-D Array

new_array = np.array([[10, 20],
                      [12, 16]])
determinant = np.linalg.det(new_array)
print(determinant)

# Creating a 3x3x3 array with random values
rand_array = np.random.rand(3, 3, 3)
print(rand_array)

# Creating a 5x5 array with random values and find the min and max values 

array_rand = np.random.rand(5, 5)
print(array_rand)

#Finding the min and max values 
print(np.min(array_rand)) # Min
print(np.max(array_rand)) # Max

# Computing mean, standard deviation and variance of an array along second axis
# we have built-in functions in Numpy and we will use them

array_1 = np.array([[10, 20 , 30],
                   [30, 50,  40],
                   [50, 30, 80]])
mean_val = np.mean(array_1, axis=1) #finding the mean
print("The mean is", mean_val)

std_val = np.std(array_1, axis=1)
print("Standard Deviation is", std_val)

var_val = np.var(array_1, axis= 1)
print("Variance is", var_val)
