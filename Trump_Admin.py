#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:26:44 2023

@author: ashleymathew
"""
import pandas as pd
import geopandas as gpd
import os
import glob
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300

# Import data for the Trump administration
case2 = 'Trump_Admin.xlsx'
Trump_Admin = pd.read_excel(case2) 

#case3 = 'Biden_Admin.csv'
#Biden_Admin = pd.read_csv(case3)
            
# Convert to floats
# Convert float columns to string type
Trump_Admin["Total Minority Owned Business Dollars"] = Trump_Admin["Total Minority Owned Business Dollars"].astype(str)
Trump_Admin["Small Business Dollars"] = Trump_Admin["Small Business Dollars"].astype(str)
Trump_Admin["Asian-Pacific American Owned Dollars"] = Trump_Admin["Asian-Pacific American Owned Dollars"].astype(str)
Trump_Admin["Black American Owned Dollars"] = Trump_Admin["Black American Owned Dollars"].astype(str)
Trump_Admin["Hispanic American Owned Dollars"] = Trump_Admin["Hispanic American Owned Dollars"].astype(str)
Trump_Admin["Native American Owned Dollars"] = Trump_Admin["Native American Owned Dollars"].astype(str)
Trump_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] = Trump_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"].astype(str)
Trump_Admin["Other Minority Owned Business Dollars"] = Trump_Admin["Other Minority Owned Business Dollars"].astype(str)

# Use .str method to remove commas and dollar signs
Trump_Admin["Total Minority Owned Business Dollars"] = Trump_Admin["Total Minority Owned Business Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Trump_Admin["Small Business Dollars"] = Trump_Admin["Small Business Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Trump_Admin["Asian-Pacific American Owned Dollars"] = Trump_Admin["Asian-Pacific American Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Trump_Admin["Black American Owned Dollars"] = Trump_Admin["Black American Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Trump_Admin["Hispanic American Owned Dollars"] = Trump_Admin["Hispanic American Owned Dollars"].str.replace('()', '').str.replace(',', '').str.replace('$', '').astype(float)
Trump_Admin["Native American Owned Dollars"] = Trump_Admin["Native American Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Trump_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] = Trump_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Trump_Admin["Other Minority Owned Business Dollars"] = Trump_Admin["Other Minority Owned Business Dollars"].str.replace(',', '').str.replace('$', '').astype(float)

# Create Proportions
Trump_Admin["Proportion of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Asian-Pacific American Owned Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Black American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Black American Owned Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Hispanic American Owned Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Native American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Native American Owned Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin['Proportion of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars'] = Trump_Admin["Other Minority Owned Business Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]

Trump_Data = pd.DataFrame({
    "Department Name": Trump_Admin["Department Name"],
    "Asian-Pacific American": Trump_Admin["Proportion of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"],
    "Black American": Trump_Admin["Proportion of Black American Owned Dollars to Total Minority Owned Business Dollars"],
    "Hispanic American": Trump_Admin["Proportion of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"],
    "Native American": Trump_Admin["Proportion of Native American Owned Dollars to Total Minority Owned Business Dollars"],
    "Subcontinent Asian (Asian-Indian)": Trump_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"],
    "Other Minority": Trump_Admin['Proportion of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars']
})

# Set the index to "Department Name"
Trump_Data.set_index("Department Name", inplace=True)

fig,ax=plt.subplots(figsize=(12,6))

# Create a stacked bar chart
chart2 = Trump_Data.plot.barh(stacked=True, width=0.8, ax=ax)

chart2.tick_params(axis='x', labelsize=8)

# Add labels and title
chart2.set_xlabel('Percentage')
chart2.set_ylabel('Department Name')
chart2.set_title('Contracting Rates to Minority Owned Businesses by Executive Department - Trump Administration')

# Adjust the font size of the x-axis tick labels
chart2.tick_params(axis='x', labelsize=7)

# Increase the spacing between the bars
chart2.set_axisbelow(True)
chart2.yaxis.grid(True)
chart2.xaxis.grid(False)
chart2.set_axisbelow(True)
#plt.subplots_adjust(bottom=0.15)
chart2.legend(loc="upper left", bbox_to_anchor=(1,1))
fig.tight_layout()
# Save the plot to a file
fig.savefig('Trump_Admin.png')

