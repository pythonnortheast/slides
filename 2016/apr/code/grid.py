#!/usr/bin/env python
"""
Visualisation - multi-facet plot.

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

small_payments = data.query("0 < Total < 10000")


# grid of distribution plots
grid = seaborn.FacetGrid(small_payments, col="Directorate", hue="Directorate",
	col_wrap=3, sharex=False, sharey=True)
grid.map(seaborn.distplot, "Total")

grid.set_titles("{col_name}")
grid.set(xlabel="", xlim=(0, 10000))

grid.savefig("grid_distribution.pdf", bbox_inches="tight")
grid.fig.clear()


# sort data by selected columns
small_payments = small_payments.sort(["week", "day"])

# 2D grid of box plots
grid = seaborn.FacetGrid(small_payments, col="day", row="week",
	sharex=True, sharey=True)
grid.map(seaborn.boxplot, "Total", "Directorate")

grid.set_xlabels("")
grid.despine(left=True, bottom=True)

grid.savefig("grid_box_plot.pdf", bbox_inches="tight")
grid.fig.clear()
