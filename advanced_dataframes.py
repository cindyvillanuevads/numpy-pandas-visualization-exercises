import pandas as pd
import numpy as np
from env import host, username, password

# 1. Create a function named get_db_url. It should accept a username, hostname, password,
#  and database name and return a url connection string formatted like in the example at the start of this lesson.
# def get_db_url(host, username, password):
#     url = f'mysql+pymysql://{username}:{password}@{host}/employees'
#     return url
# url = get_db_url(host, username, password)

#better way rto do it so database is a variable too

def get_db_url(username,password,host,db_name):
    return f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
url =  get_db_url(username,password,host, 'employees')

#2. Use your function to obtain a connection to the employees database.
pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)


query = '''
SELECT
    t.title as title,
    d.dept_name as dept_name
FROM titles t
JOIN dept_emp USING (emp_no)
JOIN departments d USING (dept_no)
LIMIT 100
'''

title_dept = pd.read_sql(query, url)
title_dept.head()

#3. Once you have successfully run a query:
#url = get_db_url(hofst, username, password)
#pd.read_sql('SELECT * FROM employtees LIMIT 5 OFFSET 50', url)

# 4.Read the employees and titles tables into two separate DataFrames.
emp_df = pd.read_sql('SELECT * FROM employees ', url)
titles_df = pd.read_sql('SELECT * FROM titles', url)

# 5.  How many rows and columns do you have in each DataFrame? 
# Is that what you expected?
emp_df.shape
#(300024, 6)
titles_df.shape
#

titles_df.shape
(443308, 4)


# 6. Display the summary statistics for each DataFrame.
#employees dataframe
emp_df.describe(exclude = np.number)

#titles dataframe
titles_df.describe(include="all")
# describe() has mani options to show information

# 7.  How many unique titles are in the titles DataFrame?
titles_df["title"]
titles_df["title"].unique()
len(titles_df["title"].unique())


#8. What is the oldest date in the to_date column?

#check which dataframe has to_date using .head()
emp_df.head()
titles_df.head()

#titles_df has to_date column
titles_df["to_date"].min()

#9.  What is the most recent date in the to_date column?
titles_df["to_date"].max()


# ******************************************************************************************************************************************
#                                                                   EXERCISES II
#******************************************************************************************************************************************

# 1. Copy the users and roles DataFrames from the examples above.

# Create the users DataFrame.
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users2 = pd.DataFrame({
    'id_user': [1, 2, 3, 4, 5, 6],
    'names': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})


# Create the roles DataFrame

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})

# 2. What is the result of using a right join on the DataFrames?
#all the rows of the right dataframe are taken as it is 
# and only those of the left dataframe that are common in both.
users.merge(roles, left_on='role_id', right_on='id', how='right',indicator=True)


#3. What is the result of using an outer join on the DataFrames?
#it Shows all the rows of both dataframes.
users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)


# 4. What happens if you drop the foreign keys from the DataFrames and try to merge them?
#it joins both df using id or name  as a foreign key but it gives a wrong  df because the roles are under name. 
users.merge(roles, how='outer', indicator=True)

#what if there are not columns in common 
#users2.merge(roles, how='outer', indicator=True)

# 5. Load the mpg dataset from PyDataset.
from pydataset import data
mpg = data('mpg')

# 6. Output and read the documentation for the mpg dataset.
data('mpg', show_doc=True)

# 7. How many rows and columns are in the dataset? (234, 11)
mpg.shape


# 8. Check out your column names and perform any cleanup you may want on them.
#I'm checking the unique values in the column fl
mpg.fl.unique()

new_mpg = mpg.drop(columns=['fl'])

#rename columns
#mpg.columns = ['manufacturer', 'model', 'displacement', 'year', 'cylinders', 'transmission', 'drive', 'city','highway', 'fuel', 'class']

# 9. Display the summary statistics for the dataset.
new_mpg.describe()

# 10. How many different manufacturers are there?
# it gives us an array with all the manufactures
new_mpg['manufacturer'].unique()
#we can use shape or len to see how many elements are in the list
new_mpg['manufacturer'].unique().shape
len(new_mpg['manufacturer'].unique())

#mpg.manufacturer.nunique() 
#value_counts()



# 11. How many different models are there?
new_mpg.model.unique()
diff_models= new_mpg.model.unique().shape[0]
print("There are ", diff_models," differents models")

# 12. Create a column named mileage_difference like you did in the DataFrames exercises; 
# this column should contain the difference between highway and city mileage for each car.

new_mpg["mileage_difference"] = new_mpg.hwy - new_mpg.cty

# 13. Create a column named average_mileage like you did in the DataFrames exercises; 
# this is the mean of the city and highway mileage.
new_mpg["average_mileage"] = (new_mpg.hwy + new_mpg.cty) / 2

# 14. Create a new column on the mpg dataset named is_automatic 
# that holds boolean values denoting whether the car has an automatic transmission.
#first I check the column that has this information and check the unique observations
new_mpg.trans.unique()

#there are differents types of auto. so we can use .str.startswith to get all the observations
#that start with a
new_mpg["is_automatic"] =  new_mpg['trans'].str.startswith("a")

# *********************
# create more thtn one columns at a time
# mpg = mpg.assign(mileage_difference = mpg.highway - mpg.city,
#                  average_mileage = (mpg.highway + mpg.city) / 2,
#                  is_automatic = mpg.transmission.str.startswith('a'))

# 15. Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
new_mpg.nlargest(1,"average_mileage", keep='all')[["manufacturer", "model"]]

# 	manufacturer	model
# 222	volkswagen	new beetle


# 16. Do automatic or manual cars have better miles per gallon? 
#manual ransmission  has better
#I can use groupby and with .agg get the mean
new_mpg.groupby('is_automatic').average_mileage.agg('mean')

# I create anew df that has manual and automatin avg
groupby_trans =new_mpg.groupby('is_automatic').average_mileage.agg(['mean'])

# I rename the index
groupby_trans = groupby_trans.rename(index={False: "Manual" , True: "Automatic"})
car_better_mi = groupby_trans.nlargest(1,"mean")
print("the type of transmission  that has better miles per gallon is:", car_better_mi )


# ************************************************
# If you need to troubleshoot column names, 
# I’d recommend running “df.columns” on its own line
# df.columns.tolist()
# ************************************************************

# ******************************************************************************************************************************************
#                                                                   EXERCISES III
#******************************************************************************************************************************************

# 1. Use your get_db_url function to help you explore the data from the chipotle database.
url2 =  get_db_url(username,password,host, 'chipotle')
order_ch = pd.read_sql('SELECT * FROM orders', url2)


# 2. What is the total price for each order?
#first we need item_price
order_ch['item_price']
#we need to remove $ 
order_ch['item_price'].str. replace('$',' ')

#convert to float
order_ch['item_price'].str. replace('$',' ').astype('float')

#asign to the column
order_ch['item_price'] = order_ch['item_price'].str. replace('$',' ').astype('float')

#this gives us a panda series
order_ch.groupby('order_id').item_price.sum()

#this give us a dataframe
order_ch.groupby('order_id').sum('item_price')

# 3. What are the most popular 3 items?
#we need 2 columns for this
order_ch[["item_name", "quantity"]]

#lets se how many of each item_name
order_ch.groupby("item_name").sum("quantitive")
#this gives us just the 2 columns
order_ch.groupby("item_name").sum()[["quantity"]]
items_quat = order_ch.groupby("item_name").sum()[["quantity"]]
#lets order
items_quat.nlargest(3, "quantity", keep="all")




# 4. Which item has produced the most revenue?
#first I group by item_name and the revenue of each item
total_price = order_ch.groupby("item_name").sum()[["item_price"]]

#then I get the max value with .nlargest()
total_price.nlargest(1, "item_price", keep= "all")

# 5. Using the titles DataFrame, visualize the number of employees with each title.
titles_df.groupby("title").count()[['emp_no']]

# 6. Join the employees and titles DataFrames together.

# 7. Visualize how frequently employees change titles.

# 8.For each title, find the hire date of the employee that was hired most recently with that title.

# 9.Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas code to perform the manipulations.)

