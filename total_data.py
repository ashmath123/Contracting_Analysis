#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:28:57 2023

@author: ashleymathew
"""
# Import standard modules
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 300

# Read all the csv files from previous scripts. Combining all administrations
# into one concatinated data set

Obama_Admin = pd.read_csv("Obama_Admin_Filtered.csv")
Trump_Admin = pd.read_csv("Trump_Admin_Filtered.csv")
Biden_Admin = pd.read_csv("Biden_Admin_Filtered.csv")

admins = {"Obama": Obama_Admin,
         "Trump": Trump_Admin,
         "Biden": Biden_Admin}

Total_Data = pd.concat(admins).reset_index()
Total_Data["Department Name"] = Total_Data["Department Name"].str.strip()

# Create a pivot table from Total_Datawhich pulls the percent of Minority 
# Owned Business contracting dollars to total contracting dollars

pivot_table = Total_Data.pivot(index="Department Name", columns="level_0", values="Percent of Minority Owned Business Contracting to Total Contracting Dollars").round(2)
pivot_table = pivot_table.loc[:, ["Obama", "Trump", "Biden"]]

print(pivot_table)

# Create an image of the pivot table

fig, ax = plt.subplots(figsize=(8, 6))
ax.axis("tight")
ax.axis("off")
table = ax.table(cellText=pivot_table.values, colLabels=pivot_table.columns, rowLabels=pivot_table.index, cellLoc="center", loc='center')
table.auto_set_font_size(False)
table.set_fontsize(8)

title = "Percent of Minority Owned Business Contracting Dollars to Total Contracting Dollars \n Under Obama, Trump, and Biden Administration"
fig.suptitle(title)

fig.tight_layout()
fig.savefig("Pivot_table_total.png")
























