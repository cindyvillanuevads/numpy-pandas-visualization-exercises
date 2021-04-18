import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# 1. How many negative numbers are there?
#neg_a have all the numbers < 0 ( negative)
#neg_a = a[a < 0]
# len() gives as the total elements which are the negative numbers
#total_neg = len(neg_a)

total_neg = len(a[a < 0])
print("Total negative numbers: ",total_neg)

# 2. How many positive numbers are there?
total_pos = len(a[a > 0])
print("Total positive numbers: ", total_pos)

# 3. How many even positive numbers are there?
#even has all the even numbers
even = a[a % 2 == 0 ]
#we count with len() how many are positive
total_even_postitive = (len(even[even > 0]))
print("Total positive even numbers: ", total_even_postitive)

# 4. If you were to add 3 to each data point, how many positive numbers would there be?
#add 3 to each element that is in the array
even_3 = a + 3
# with len() we know how many number are positive using the condition even_3 > 0
total_even3 = len( even_3 [ even_3 > 0 ])
print("Total positive even numbers (we added 3): ", total_even3)

# 5. If you squared each number, what would the new mean and standard deviation be?
sq_num = a ** 2
# remove nan values using numpy.isnan() 
# and numpy.logical_not
# remove   nan values (b = a[numpy.logical_not(numpy.isnan(a))])
#other way 
# d = c[~(numpy.isnan(c))]
# msn =  sqrt_num [~(np.isnan(sqrt_num))]
mean_sq_num = sq_num.mean()
std_sq_num = sq_num.std()
print("New mean: ",mean_sq_num, "New standard deviation:", std_sq_num)

#6.  A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0.
#  This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.
mean_a = a.mean()
print("mean ", mean_a)
centering = a - mean_a
print("Centering: ", centering)


#7.  Calculate the z-score for each data point. Recall that the z-score is given by:
#  z = (n - mean) / standard deviation
std_a = a.std()

zscore_a = (a - mean_a) / std_a
print("Z-score for each data point ", zscore_a)

#8.  Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a / len(a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for n in a:
    product_of_a = product_of_a * n


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [n ** 2 for n in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a =[ n for n in a if n % 2 != 0 ]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a =[ n for n in a if n % 2 == 0 ]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
#we need to convert c which is a list into an array
b = np.array(b)
type(b)
#this gives us the sum of each column. we dont want that
sum_of_b = sum(b)

#this gives us the sum of each row
example = sum(b[0])

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# Exercise 9 - print out the shape of the array b.
print(b.shape)
# Exercise 10 - transpose the array b.
np.transpose(b)
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
np.reshape(b,6)
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
np.reshape(b,(6,1))
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c = np.array(c)

c.max()
c.sum()
product_of_c = c.prod()
# Exercise 2 - Determine the standard deviation of c.
np.std(c)

# Exercise 3 - Determine the variance of c.
np.var(c)

# Exercise 4 - Print out the shape of the array c
print(c.shape)

# Exercise 5 - Transpose c and print out transposed result.
tc = np.transpose(c)
print(tc)

# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c,c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
ct= np.transpose(c)
ct_times_c = ct *c
ct_times_c
sum_ct_times_c = ct_times_c.sum()

print(sum_ct_times_c)

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
cxc= c * c
cxc_t = np.transpose(cxc)
prod_cxc_t = cxc_t.prod()
print(prod_cxc_t)

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d =np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
sine_d = np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d
cos_d = np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d
tan_d = np.tan(d)

# Exercise 4 - Find all the negative numbers in d
neg_num_d = d[d < 0]

# Exercise 5 - Find all the positive numbers in d
pos_num_d = d[d > 0]

# Exercise 6 - Return an array of only the unique numbers in d.
unique_d = np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))

# Exercise 8 - Print out the shape of d.
print(d.shape)

# Exercise 9 - Transpose and then print out the shape of d.
dt =  np.transpose(d)
print(dt.shape)

# Exercise 10 - Reshape d into an array of 9 x 2
new_d = d.reshape(9,2)