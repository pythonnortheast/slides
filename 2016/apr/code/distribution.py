#!/usr/bin/env python
"""
Visualisation - distribution.

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


small_payments = data.query("0 < Total < 10000")

# histogram + kernel density estimation
plot = seaborn.distplot(small_payments.Total)
plot.figure.savefig("distribution.pdf", bbox_inches="tight")
plot.figure.clear()


# box plots
plot = seaborn.boxplot(x="Total", y="Directorate", data=small_payments)
plot.figure.savefig("box_plot.pdf", bbox_inches="tight")
plot.figure.clear()


# violin plots
plot = seaborn.violinplot(x="Total", y="Directorate", data=small_payments)
plot.figure.savefig("violin_plot.pdf", bbox_inches="tight")
