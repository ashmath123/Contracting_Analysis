#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 23:51:22 2023

@author: ashleymathew
"""
# import Standad packages
import pandas as pd
import geopandas as gpd
import os
import glob
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300

# Import data for the Obama administration
case1 = 'Obama_Admin.xlsx'
Obama_Admin = pd.read_excel(case1) 

#case3 = 'Biden_Admin.csv'
#Biden_Admin = pd.read_csv(case3)
            
# Convert float columns to string type
Obama_Admin["Total Minority Owned Business Dollars"] = Obama_Admin["Total Minority Owned Business Dollars"].astype(str)
Obama_Admin["Small Business Dollars"] = Obama_Admin["Small Business Dollars"].astype(str)
Obama_Admin["Asian-Pacific American Owned Dollars"] = Obama_Admin["Asian-Pacific American Owned Dollars"].astype(str)
Obama_Admin["Black American Owned Dollars"] = Obama_Admin["Black American Owned Dollars"].astype(str)
Obama_Admin["Hispanic American Owned Dollars"] = Obama_Admin["Hispanic American Owned Dollars"].astype(str)
Obama_Admin["Native American Owned Dollars"] = Obama_Admin["Native American Owned Dollars"].astype(str)
Obama_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] = Obama_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"].astype(str)
Obama_Admin["Other Minority Owned Business Dollars"] = Obama_Admin["Other Minority Owned Business Dollars"].astype(str)

# Use .str method to remove commas and dollar signs
Obama_Admin["Total Minority Owned Business Dollars"] = Obama_Admin["Total Minority Owned Business Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Obama_Admin["Small Business Dollars"] = Obama_Admin["Small Business Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Obama_Admin["Asian-Pacific American Owned Dollars"] = Obama_Admin["Asian-Pacific American Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Obama_Admin["Black American Owned Dollars"] = Obama_Admin["Black American Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Obama_Admin["Hispanic American Owned Dollars"] = Obama_Admin["Hispanic American Owned Dollars"].str.replace('()', '').str.replace(',', '').str.replace('$', '').astype(float)
Obama_Admin["Native American Owned Dollars"] = Obama_Admin["Native American Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Obama_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] = Obama_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Obama_Admin["Other Minority Owned Business Dollars"] = Obama_Admin["Other Minority Owned Business Dollars"].str.replace(',', '').str.replace('$', '').astype(float)

# Create Proportions
Obama_Admin["Proportion of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Asian-Pacific American Owned Dollars"]/ Obama_Admin["Total Minority Owned Business Dollars"]
Obama_Admin["Proportion of Black American Owned Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Black American Owned Dollars"]/ Obama_Admin["Total Minority Owned Business Dollars"]
Obama_Admin["Proportion of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Hispanic American Owned Dollars"]/ Obama_Admin["Total Minority Owned Business Dollars"]
Obama_Admin["Proportion of Native American Owned Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Native American Owned Dollars"]/ Obama_Admin["Total Minority Owned Business Dollars"]
Obama_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"]/ Obama_Admin["Total Minority Owned Business Dollars"]
Obama_Admin['Proportion of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars'] = Obama_Admin["Other Minority Owned Business Dollars"]/ Obama_Admin["Total Minority Owned Business Dollars"]

Obama_Data = pd.DataFrame({
    "Department Name": Obama_Admin["Department Name"],
    "Asian-Pacific American": Obama_Admin["Proportion of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"],
    "Black American": Obama_Admin["Proportion of Black American Owned Dollars to Total Minority Owned Business Dollars"],
    "Hispanic American": Obama_Admin["Proportion of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"],
    "Native American": Obama_Admin["Proportion of Native American Owned Dollars to Total Minority Owned Business Dollars"],
    "Subcontinent Asian (Asian-Indian)": Obama_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"],
    "Other Minority": Obama_Admin['Proportion of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars']
})

# Set the index to "Department Name"
Obama_Data.set_index("Department Name", inplace=True)

fig,ax=plt.subplots(figsize=(12,6))

# Create a stacked bar chart
chart = Obama_Data.plot.barh(stacked=True, width=0.8, ax=ax)

chart.tick_params(axis='x', labelsize=8)

# Add labels and title
chart.set_xlabel('Percentage')
chart.set_ylabel('Department Name')
chart.set_title('Contracting Rates to Minority Owned Businesses by Executive Department - Obama Administration')

# Adjust the font size of the x-axis tick labels
chart.tick_params(axis='x', labelsize=7)

# Increase the spacing between the bars
chart.set_axisbelow(True)
chart.yaxis.grid(True)
chart.xaxis.grid(False)
chart.set_axisbelow(True)
#plt.subplots_adjust(bottom=0.15)
chart.legend(loc="upper left", bbox_to_anchor=(1,1))
fig.tight_layout()
# Save the plot to a file
fig.savefig('Obama_Admin.png')







