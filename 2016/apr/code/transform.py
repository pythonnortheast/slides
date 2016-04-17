#!/usr/bin/env python
"""
Data transformation (try it out in the Python shell).

"""
import pandas
import calendar


# read data from a CSV file
data = pandas.read_csv("january_2016.csv", skiprows=2, thousands=",")
# replace spaces in column names with underscores
data.columns = data.columns.str.replace(" ", "_")
# convert strings to date (DD/MM/YYYY) using null for invalid/missing values
data.Paid_Date = pandas.to_datetime(data.Paid_Date, format="%d/%m/%Y", errors="coerce")
# remove all rows with missing values
data = data.dropna()


# direct transformation
data.Total * 1000

# transformation with function
data.Total.apply(abs)


# add columns
data["week"] = data.Paid_Date.apply(lambda x: x.week)
data["day"] = data.Paid_Date.apply(lambda x: calendar.day_name[x.dayofweek])
# sum up payments for each day of week
weekdays = data.groupby([data.week, data.day]).sum()
print(weekdays)

# multi-level index!
weekdays.index

# pivot inner level of the index to the column labels
weekdays.unstack()["Total"]


# reshape into a new table
directorates = pandas.pivot_table(data, values="Total", index="Paid_Date", columns="Directorate")
print(directorates)
"""
# for pandas < 0.14 use different keyword arguments:
directorates = pandas.pivot_table(data, values="Total", rows="Paid_Date", cols="Directorate")
"""

# unpivot from wide format to long format
pandas.melt(directorates)

# pivot column labels to the inner level of the index
directorates.stack()
