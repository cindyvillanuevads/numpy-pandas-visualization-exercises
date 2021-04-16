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
sqrt_num = a ** .5
# remove nan values using numpy.isnan() 
# and numpy.logical_not
# remove   nan values (b = a[numpy.logical_not(numpy.isnan(a))])
#other way 
# d = c[~(numpy.isnan(c))]
msn =  sqrt_num [~(np.isnan(sqrt_num))]
mean_sqrt_num = msn.mean()
std_sqrt_num = msn.std()
print("New mean: ",mean_sqrt_num, "New standard deviation:", std_sqrt_num)

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