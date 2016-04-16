#!/usr/bin/env python
"""
Aggregation (try it out in the Python shell).

"""
import pandas
import numpy

# read data from a CSV file
data = pandas.read_csv("january_2016.csv", skiprows=2, thousands=",")
# replace spaces in column names with underscores
data.columns = data.columns.str.replace(" ", "_")
# convert strings to date (DD/MM/YYYY) using null for invalid/missing values
data.Paid_Date = pandas.to_datetime(data.Paid_Date, format="%d/%m/%Y", errors="coerce")
# remove all rows with missing values
data = data.dropna()


# group rows by one of the columns
grouped = data.groupby("Supplier_Name")

# all groups as a dictionary
grouped.group

# single group
grouped.get_group("ROYAL MAIL")


# build-in functions
grouped.size()
grouped.first()

# custom functions
grouped.aggregate(numpy.sum)
grouped.Total.aggregate([numpy.mean, numpy.std])


# modify members of the group
grouped.transform(lambda x: x.fillna(x.mean()))
