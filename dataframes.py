from pydataset import data
import pandas as pd
import numpy as np


# 1. Copy the code from the lesson to create a dataframe full of student grades.
np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})


# 1.a Create a column named passing_english that indicates whether each student has a passing grade in english.

df["passing_english"] = df.english >= 70

# 1.b Sort the english grades by the passing_english column. How are duplicates handled?
# it shows first all False and then All true. it sorted by index value
#df["passing_english"] = df.english > 70

df.sort_values(by="passing_english")


# 1.c Sort the english grades first by passing_english and then by student name. 
# All the students that are failing english should be first,
#  and within the students that are failing english they should be ordered alphabetically.
#  The same should be true for the students passing english. 
# (Hint: you can pass a list to the .sort_values method)
df.sort_values(by=['passing_english', 'name'], ascending=[True, True])
# no need for ascending when is true
df.sort_values(by=['passing_english', 'name']

# What if I want the students passing English first but names in alpha order?

df.sort_values(by=['passing_english', 'name'], ascending=[False, True])


# 1.d Sort the english grades first by passing_english, and then by the actual english grade,
#  similar to how we did in the last step.
df.sort_values(by = ['passing_english','english'], ascending=[True, True])


# 1.e Calculate each students overall grade and add it as a column on the dataframe. 
# The overall grade is the average of the math, english, and reading grades.
df['overall_grade'] = (df['math'] + df['english'] + df['reading']) / 3
#other way to do it
# using .loc if I want to select columns and rows using column labels instead of index position. With this attribute, the indexing IS inclusive. This is not the behavior you are used to when indexing strings, lists, etc. by index position.
# df.loc[row_indexer, column_indexer]
df.loc[:, 'math': 'reading']
# Set axis=1 to sum all of the columns for each row, grades for each student.

df.loc[:, 'math': 'reading'].sum(axis=1)
# divide by 3 and assign this to a new column called overall_average
# df['overall_average'] = round(df.loc[:, 'math': 'reading'].sum(axis=1) / 3)
#other way
#df['overall_average'] = round(df.iloc[:, 1:4].sum(axis=1) / 3).astype(int)
# 2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg')
data('mpg', show_doc=True)

# How many rows and columns are there?
#(234, 11)
mpg.shape

# What are the data types of each column?
mpg.dtypes

# mpg.dtypes
# manufacturer     object
# model            object
# displ           float64
# year              int64
# cyl               int64
# trans            object
# drv              object
# cty               int64
# hwy               int64
# fl               object
# class            object
# dtype: object


# Summarize the dataframe with .info and .describe
mpg.info()
#.info() shows us that all of the columns have the same number of non-null values.

# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 234 entries, 1 to 234
# Data columns (total 11 columns):
#  #   Column        Non-Null Count  Dtype  
# ---  ------        --------------  -----  
#  0   manufacturer  234 non-null    object 
#  1   model         234 non-null    object 
#  2   displ         234 non-null    float64
#  3   year          234 non-null    int64  
#  4   cyl           234 non-null    int64  
#  5   trans         234 non-null    object 
#  6   drv           234 non-null    object 
#  7   cty           234 non-null    int64  
#  8   hwy           234 non-null    int64  
#  9   fl            234 non-null    object 
#  10  class         234 non-null    object 
# dtypes: float64(1), int64(4), object(6)
# memory usage: 31.9+ KB

mpg.describe()
#.describe() provides us with the descriptive statistics for all columns with numeric dtypes.

# 	displ	year	cyl	cty	hwy
# count	234.000000	234.000000	234.000000	234.000000	234.000000
# mean	3.471795	2003.500000	5.888889	16.858974	23.440171
# std	1.291959	4.509646	1.611534	4.255946	5.954643
# min	1.600000	1999.000000	4.000000	9.000000	12.000000
# 25%	2.400000	1999.000000	4.000000	14.000000	18.000000
# 50%	3.300000	2003.500000	6.000000	17.000000	24.000000
# 75%	4.600000	2008.000000	8.000000	19.000000	27.000000
# max	7.000000	2008.000000	8.000000	35.000000	44.000000

# Rename the cty column to city.
mpg = mpg.rename(columns={"cty":"city"})

# Rename the hwy column to highway.
mpg = mpg.rename(columns={'hwy':'highway'})

# Do any cars have better city mileage than highway mileage?
#no, there is no cars thar have better city mileage than highway mileage
mpg[mpg.city > mpg.highway][['model', 'city', 'highway']]

# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

mpg["mileage_difference"] = mpg["highway"] - mpg ["city"]


# Which car (or cars) has the highest mileage difference?
#here I  can see there are 2 cars that has the highest mileage difference
mpg.sort_values(by= 'mileage_difference', ascending = False).head(3)

#other way
mpg.nlargest(1,"mileage_difference", keep='all')

# Which compact class car has the lowest highway mileage? The best?
#I need to rename class because it is a keyword
mpg = mpg.rename(columns={'class':'Class'})
# I use a condition to show only the compact class and get the largest 
mpg[mpg.Class  == 'compact'].nlargest(1,"highway", keep='all')
#I could use this format so the class is not giving an error for being a keyword
mpg[mpg["Class"]  == 'compact'].nlargest(1,"highway", keep='all')


# 	manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	Class	mileage_difference
# 213	volkswagen	jetta	1.9	1999	4	manual(m5)	f	33	44	d	compact	11

#lowest
mpg[mpg.Class  == 'compact'].nsmallest(1,"highway", keep='all')

# 	manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	Class	mileage_difference
# 220	volkswagen	jetta	2.8	1999	6	auto(l4)	f	16	23	r	compact	7

# Create a column named average_mileage that is the mean of the city and highway mileage.
mpg["average_mileage"] = (mpg.city + mpg.highway) / 2
# mpg["average_mileage"] = (mpg.city + mpg.highway) / len (mpg.city , mpg.highway)

# Which dodge car has the best average mileage? The worst?
#the best
mpg[mpg.manufacturer == "dodge"].nlargest(1,"average_mileage", keep="all")[['model','displ','year','cyl','trans','average_mileage']]
 
# model	displ	year	cyl	trans	average_mileage
# 38	caravan 2wd	2.4	1999	4	auto(l3)	21.0

# the worst

mpg[mpg.manufacturer == "dodge"].nsmallest(1,"average_mileage", keep="all")[['model','displ','year','cyl','trans','average_mileage']]
# model	displ	year	cyl	trans	average_mileage
# 55	dakota pickup 4wd	4.7	2008	8	auto(l5)	10.5
# 60	durango 4wd	4.7	2008	8	auto(l5)	10.5
# 66	ram 1500 pickup 4wd	4.7	2008	8	auto(l5)	10.5
# 70	ram 1500 pickup 4wd	4.7	2008	8	manual(m6)	10.5


# 3.  Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
data('Mammals', show_doc=True)
mam = data('Mammals')

# How many rows and columns are there?
mam.shape
#(107, 4)

# What are the data types?
mam.dtypes
# weight      float64
# speed       float64
# hoppers        bool
# specials       bool
# dtype: object

# Summarize the dataframe with .info and .describe
mam.info()
mam.describe()

# What is the the weight of the fastest animal?
mam.nlargest(1, "speed", keep = "all")[["weight"]]
# weight
# 53	55.0

# What is the overal percentage of specials?
#show all specials
mam[mam.specials == True]

#how many are specials
#one way
mam[mam.specials == True].shape[0]
#other way
len(mam[mam.specials == True])

#percentage
perc_specials = mam[mam.specials == True].shape[0] / mam.shape[0] *100
# other way to do it with round
round(mam[mam.specials == True].shape[0] / mam.shape[0] *100, 2)

# How many animals are hoppers that are above the median speed? What percentage is this?
# first calculate the mean
med_speed = mam["speed"].median()

#how many
#this gives us a list
mam[(mam.speed > med_speed) & (mam.hoppers == True)]

total_hopp = mam[(mam.speed > med_speed) & (mam.hoppers == True)].shape[0]

#percentaje
percentaje_hoppers = round(total_hopp / mam.shape[0] *100,2)