import pandas as pd
import numpy as np
from env import host, username, password

# 1. Create a function named get_db_url. It should accept a username, hostname, password,
#  and database name and return a url connection string formatted like in the example at the start of this lesson.
def get_db_url(host, username, password):
    url = f'mysql+pymysql://{username}:{password}@{host}/employees'
    return url
url = get_db_url(host, username, password)


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