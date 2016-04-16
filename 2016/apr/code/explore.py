#!/usr/bin/env python
"""
Exploring the data (try it out in the Python shell).

"""
import pandas


# read data from a CSV file
data = pandas.read_csv("january_2016.csv", skiprows=2, thousands=",")
# replace spaces in column names with underscores
data.columns = data.columns.map(lambda x: x.replace(" ", "_"))
# convert strings to date (DD/MM/YYYY) using null for invalid/missing values
data.Paid_Date = pandas.to_datetime(data.Paid_Date, format="%d/%m/%Y", errors="coerce")
# remove all rows with missing values
data = data.dropna()


# show basic statistics for each numerical column
data.describe()

# show frequency
data["Directorate"].value_counts()

# show high value payments
data.query("Total > 1000000")

# complex queries
data.query("Group_Description == 'Revenue Income' and Total > 10000")


# alternative syntax
data[(data.Group_Description == "Revenue Income") & (data.Total > 10000)]
