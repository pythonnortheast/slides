#!/usr/bin/env python
"""
Visualisation - simple comparison.

"""
import pandas
import seaborn

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


# plot number of payments per directorate
plot = seaborn.countplot(x="Directorate", data=data)
plot.figure.savefig("count_plot.pdf")


# fix labels overlap, shrink margins
seaborn.plt.subplots(figsize=(8, 4))
plot = seaborn.countplot(x="Directorate", data=data)
plot.figure.savefig("count_plot_improved.pdf", bbox_inches="tight")
plot.figure.clear()


# split into categories, plot bars horizontally
plot = seaborn.countplot(y="Directorate", hue="Cap/Rev", data=data)
plot.figure.savefig("count_plot_categories.pdf", bbox_inches="tight")
