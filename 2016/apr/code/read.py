#!/usr/bin/env python
"""
Reading real-world data (try it out in the Python shell).

"""
import pandas


data = pandas.read_csv("january_2016.csv")
data.info()
"""
# python3 needs defined encoding (to read the pound symbol)
data = pandas.read_csv("january_2016.csv", encoding="iso-8859-1")
"""


# skip first two rows
data = pandas.read_csv("january_2016.csv", skiprows=2)
data.info()


# number with a thousands separator
data = pandas.read_csv("january_2016.csv", skiprows=2, thousands=",")
data.info()

# replace spaces in column names with underscores
data.columns = data.columns.str.replace(" ", "_")
"""
# for pandas < 0.17 use map instead:
data.columns = data.columns.map(lambda x: x.replace(" ", "_"))
"""

# show the values in dates column
data["Paid_Date"].value_counts()

# convert strings to date (DD/MM/YYYY) - raises exception
data["Paid_Date"] = pandas.to_datetime(data["Paid_Date"], format="%d/%m/%Y")

# convert strings to date, set NaT for invalid/missing values
data["Paid_Date"] = pandas.to_datetime(data["Paid_Date"], format="%d/%m/%Y",
	errors="coerce")
"""
# for pandas < 0.17 use a different keyword argument:
data["Paid_Date"] = pandas.to_datetime(data["Paid_Date"], format="%d/%m/%Y",
	coerce=True)
"""


data.info()
data.Paid_Date[0]

data = data.dropna()
