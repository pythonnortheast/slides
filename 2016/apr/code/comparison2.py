#!/usr/bin/env python
"""
Visualisation - comparison.

"""
import pandas
import seaborn
import calendar

seaborn.set_style("whitegrid")
seaborn.set_context("paper")


# read data from a CSV file
data = pandas.read_csv("january_2016.csv", skiprows=2, thousands=",")
# replace spaces in column names with underscores
data.columns = data.columns.str.replace(" ", "_")
# convert strings to date (DD/MM/YYYY) using null for invalid/missing values
data.Paid_Date = pandas.to_datetime(data.Paid_Date, format="%d/%m/%Y", errors="coerce")
# remove all rows with missing values
data = data.dropna()


# add extra columns
data["week"] = data.Paid_Date.apply(lambda x: x.week)
data["day"] = data.Paid_Date.apply(lambda x: calendar.day_name[x.dayofweek])


# mean payment value for each day of week
plot = seaborn.barplot(x="day", y="Total", data=data)
plot.figure.savefig("bar_plot.pdf", bbox_inches="tight")
plot.figure.clear()


# sum up payments for each day of week
weekdays = data.groupby([data.week, data.day]).sum()
# pivot inner level of the index to the column labels
new_data = weekdays.unstack()["Total"]
# specify order of columns
new_data = new_data[["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]]

# draw a heatmap
plot = seaborn.heatmap(new_data, annot=True, fmt=".0f", linewidths=0.5)
plot.figure.savefig("heatmap.pdf", bbox_inches="tight")
