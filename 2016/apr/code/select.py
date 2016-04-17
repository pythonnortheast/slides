#!/usr/bin/env python
"""
Selection (try it out in the Python shell).

"""
import pandas


# read data from a CSV file
data = pandas.read_csv("january_2016.csv", skiprows=2, thousands=",")
# replace spaces in column names with underscores
data.columns = data.columns.str.replace(" ", "_")
# convert strings to date (DD/MM/YYYY) using null for invalid/missing values
data.Paid_Date = pandas.to_datetime(data.Paid_Date, format="%d/%m/%Y", errors="coerce")
# remove all rows with missing values
data = data.dropna()


# first 5 rows
data[:5]  # data.head()

# fifth row
data.ix[5]

# third column of the fifth row
data.ix[5, 3]
data.ix[5][3]


# default index
data.index

# use date column as index
indexed_data = data.set_index("Paid_Date")
indexed_data.info()

# get all rows with given index
indexed_data.ix["2016-01-06"]
# get all rows with index in given range
indexed_data.ix["2016-01-12":"2016-01-14"]
