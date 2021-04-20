#Use pandas to create a Series named fruits from the following list:
import pandas as pd
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])



# 1. Determine the number of elements in fruits.
fruits.size
#fruits.shape


# 2. Output only the index from fruits.
fruits.index
#list(fruits.index)

# 3. Output only the values from fruits.
fruits.values

# 4. Confirm the data type of the values in fruits.
fruits.dtype

# 5. Output only the first five values from fruits.
fruits.head(5) 
 
# Output the last three values. 
fruits.tail(3)

# Output two random values from fruits.
fruits.sample(2)

# 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()
# count       17
# unique      13
# top       kiwi
# freq         4
# dtype: object

# 7. Run the code necessary to produce only the unique string values from fruits.
fruits.unique()
#fruits.nunique()

# 8. Determine how many times each unique string value occurs in fruits.
fruits.value_counts()


# 9. Determine the string value that occurs most frequently in fruits.
fruits.value_counts().nlargest(n=1)
#other ways
fruits.value_counts().head(1)
fruits.value_counts().idxmax()
#this gives all the max values
fruits.value_counts().nlargest(n=1, keep = "all")

# 10. Determine the string value that occurs least frequently in fruits.
fruits.value_counts().nsmallest()
#other way
fruits.value_counts().nsmallest(n=1, keep = "all")

## ###############################################
#               PART II
## ###############################################

# 1.Capitalize all the string values in fruits.
fruits.str.upper()

# 2. Count the letter "a" in all the string values (use string vectorization).
sum(fruits.str.lower().str.count(r'[a]'))

# 3. Output the number of vowels in each and every string value.
fruits.str.lower().str.count('[aeiou]')

# 4. Write the code to get the longest string value from fruits.
fruits[fruits.str.len().argmax()]
#ither way
max(fruits, key=len)
# 5. Write the code to get the string values with 5 or more letters in the name.
fruits[fruits.str.len() >= 5]

# 6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
fruits[fruits.apply(lambda fruit: fruit.count('o') > 1)]


# 7. Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]

# 8. Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]

# 9. Which string value contains the most vowels?
fruits[fruits.str.lower().str.count('[aeiou]').max()]

## ###############################################
#               PART III
## ###############################################

word='hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
letters = pd.Series(list(word))
# 1. Which letter occurs the most frequently in the letters Series?
#it gives me the count of each letter
letters.value_counts()
# these are the ways that we can get the most frequent
letters.value_counts().idxmax()
letters.value_counts().head(1)
letters.value_counts().nlargest(n=1, keep='all')
# 2. Which letter occurs the Least frequently?
letters.value_counts().idxmin()
#other ways
letters.value_counts().tail(1)
letters.value_counts().nsmallest(n=1, keep='all')

# 3. How many vowels are in the Series?
(letters.str.lower().str.count('[aeiou]')).sum()
vowel_sum = (letters.str.lower().str.count('[aeiou]')).sum()

# 4. How many consonants are in the Series?
#we already know how many vowels
total_cons = len(letters) - vowel_sum
#other ways
#we are couting from a-z  and  we are removing the vowels with - (letters.str.lower().str.count('[aeiou]'))
letters.str.lower().str.count(r'[a-z]') - (letters.str.lower().str.count('[aeiou]'))
sum(letters.str.lower().str.count(r'[a-z]') - (letters.str.lower().str.count('[aeiou]')))
# I can simply use the tilde to return the opposite, the consonants.

(~letters.str.lower().isin(['a', 'e', 'i', 'o', 'u'])).sum()

# 5. Create a Series that has all of the same letters but uppercased.
letters.str.upper()
# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.

letters.value_counts().head(6).plot.bar(title='Pandas Letter Visualization', 
                                                                            rot=0, 
                                                                            color='m', 
                                                                            ec='black',
                                                                            width=.9).set(xlabel='Letter',
                                                                                         ylabel='Frequency')

# Use pandas to create a Series named numbers from the following list:


#     ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
num =   ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
numbers = pd.Series(num)

# 7. What is the data type of the numbers Series?
numbers.dtype

# 8. How many elements are in the number Series?
numbers.size

# 9. Perform the necessary manipulations by accessing Series attributes and methods to convert 
# the numbers Series to a numeric data type.
new_numbers= numbers.str.replace('$', '').str.replace(",","").astype("float")

# 10. Run the code to discover the maximum value from the Series.
new_numbers.max()

# 11. Run the code to discover the minimum value from the Series.
new_numbers.min()

# 12. What is the range of the values in the Series?
range =  new_numbers.max() - new_numbers.min()

# 13. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
pd.cut(new_numbers, 4)
pd.cut(new_numbers, 4).value_counts()
# 14. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
import matplotlib.pyplot as plt
pd.cut(new_numbers,4).value_counts().sort_index(ascending = False).plot(kind = 'barh', color = "m")
plt.title('4 Bins ')
plt.xlabel('Counts')
plt.ylabel('US $')
plt.show()

# Use pandas to create a Series named exam_scores from the following list:

# Copied to clipboard
#     [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
exam_scores =  [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
exam_scores = pd.Series(exam_scores)

# 15. How many elements are in the exam_scores Series?
exam_scores.size

# 16. Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
exam_scores.describe()

# 17. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
exam_scores.value_counts().plot(kind = 'bar', color = "m")
plt.title('Exam Scores ')
plt.xlabel('Scores')
plt.ylabel('Counts')
plt.show()

# 18. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades.
#  Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
curv = 100 - exam_scores.max()
curved_grades = exam_scores + curv
# 19. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. 
# For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
#define bine edges
bin_edges = [0,70,75,80,90,101]
#create the bin labes
bin_labels = ['F','D','C','B','A']

#using the .cut()function to create the 5 bins and labels.
#check documentation for .cut()
#pandas.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', 
#           ordered=True)
letter_grades = pd.cut(curved_grades, bins = bin_edges, labels = bin_labels)

# 20.Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
letter_grades.value_counts().plot(kind="bar", color = 'b')
plt.title('Letter Grades ')
plt.xlabel('Scores')
plt.ylabel('Counts')
plt.show()