#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:32:22 2023

@author: ashleymathew
"""
import pandas as pd
import geopandas as gpd
import os
import glob
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300

# Import data for the Biden administration
case3 = 'Biden_Admin.xlsx'
Biden_Admin = pd.read_excel(case3) 
            
# Convert to floats
# Convert float columns to string type
Biden_Admin["Total Minority Owned Business Dollars"] = Biden_Admin["Total Minority Owned Business Dollars"].astype(str)
Biden_Admin["Small Business Dollars"] = Biden_Admin["Small Business Dollars"].astype(str)
Biden_Admin["Asian-Pacific American Owned Dollars"] = Biden_Admin["Asian-Pacific American Owned Dollars"].astype(str)
Biden_Admin["Black American Owned Dollars"] = Biden_Admin["Black American Owned Dollars"].astype(str)
Biden_Admin["Hispanic American Owned Dollars"] = Biden_Admin["Hispanic American Owned Dollars"].astype(str)
Biden_Admin["Native American Owned Dollars"] = Biden_Admin["Native American Owned Dollars"].astype(str)
Biden_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] = Biden_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"].astype(str)
Biden_Admin["Other Minority Owned Business Dollars"] = Biden_Admin["Other Minority Owned Business Dollars"].astype(str)

# Use .str method to remove commas and dollar signs
Biden_Admin["Total Minority Owned Business Dollars"] = Biden_Admin["Total Minority Owned Business Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Biden_Admin["Small Business Dollars"] = Biden_Admin["Small Business Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Biden_Admin["Asian-Pacific American Owned Dollars"] = Biden_Admin["Asian-Pacific American Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Biden_Admin["Black American Owned Dollars"] = Biden_Admin["Black American Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Biden_Admin["Hispanic American Owned Dollars"] = Biden_Admin["Hispanic American Owned Dollars"].str.replace('()', '').str.replace(',', '').str.replace('$', '').astype(float)
Biden_Admin["Native American Owned Dollars"] = Biden_Admin["Native American Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Biden_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] = Biden_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"].str.replace(',', '').str.replace('$', '').astype(float)
Biden_Admin["Other Minority Owned Business Dollars"] = Biden_Admin["Other Minority Owned Business Dollars"].str.replace(',', '').str.replace('$', '').astype(float)

# Create Proportions
Biden_Admin["Proportion of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"] = Biden_Admin["Asian-Pacific American Owned Dollars"]/ Biden_Admin["Total Minority Owned Business Dollars"]
Biden_Admin["Proportion of Black American Owned Dollars to Total Minority Owned Business Dollars"] = Biden_Admin["Black American Owned Dollars"]/ Biden_Admin["Total Minority Owned Business Dollars"]
Biden_Admin["Proportion of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"] = Biden_Admin["Hispanic American Owned Dollars"]/ Biden_Admin["Total Minority Owned Business Dollars"]
Biden_Admin["Proportion of Native American Owned Dollars to Total Minority Owned Business Dollars"] = Biden_Admin["Native American Owned Dollars"]/ Biden_Admin["Total Minority Owned Business Dollars"]
Biden_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"] =Biden_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"]/ Biden_Admin["Total Minority Owned Business Dollars"]
Biden_Admin['Proportion of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars'] = Biden_Admin["Other Minority Owned Business Dollars"]/ Biden_Admin["Total Minority Owned Business Dollars"]

Biden_Data = pd.DataFrame({
    "Department Name": Biden_Admin["Department Name"],
    "Asian-Pacific American": Biden_Admin["Proportion of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"],
    "Black American": Biden_Admin["Proportion of Black American Owned Dollars to Total Minority Owned Business Dollars"],
    "Hispanic American": Biden_Admin["Proportion of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"],
    "Native American": Biden_Admin["Proportion of Native American Owned Dollars to Total Minority Owned Business Dollars"],
    "Subcontinent Asian (Asian-Indian)": Biden_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"],
    "Other Minority": Biden_Admin['Proportion of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars']
})

# Set the index to "Department Name"
Biden_Data.set_index("Department Name", inplace=True)

fig,ax=plt.subplots(figsize=(12,6))

# Create a stacked bar chart
chart3 = Biden_Data.plot.barh(stacked=True, width=0.8, ax=ax)

chart3.tick_params(axis='x', labelsize=8)

# Add labels and title
chart3.set_xlabel('Share of Total Minority Owned Business Dollars')
chart3.set_ylabel('Department Name')
chart3.set_title('Contracting Rates to Minority Owned Businesses by Executive Department \n Biden Administration')

# Adjust the font size of the x-axis tick labels
chart3.tick_params(axis='x', labelsize=7)

# Increase the spacing between the bars
chart3.set_axisbelow(True)
chart3.yaxis.grid(True)
chart3.xaxis.grid(False)
chart3.set_axisbelow(True)
#plt.subplots_adjust(bottom=0.15)
chart3.legend(loc="upper left", bbox_to_anchor=(1,1))
fig.tight_layout()
# Save the plot to a file
fig.savefig('Biden_Admin.png')
