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

# Which letter occurs the most frequently in the letters Series?

# Which letter occurs the Least frequently?

# How many vowels are in the Series?

# How many consonants are in the Series?

# Create a Series that has all of the same letters but uppercased.

# Create a bar plot of the frequencies of the 6 most commonly occuring letters.



