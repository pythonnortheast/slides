#!/usr/bin/env python
"""
Merging (try it out in the Python shell).

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


# read CVS file to a data frame
new_data = pandas.read_csv("february_2016.csv", skiprows=2, thousands=",")
# replace spaces in column names with underscores
new_data.columns = new_data.columns.str.replace(" ", "_")

# convert strings to date, set NaT for invalid/missing values
new_data["Paid_Date"] = pandas.to_datetime(new_data["Paid_Date"], format="%d-%b-%y",
	errors="coerce")

# remove empty column
new_data = new_data.dropna(how="all", axis=1)
# remove all rows with missing values
new_data = new_data.dropna()


# concatenate the data frames, use new index
pandas.concat([data, new_data], ignore_index=True)
