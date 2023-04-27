#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:26:44 2023

@author: ashleymathew
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300

# Import data for the Trump administration
case2 = 'Trump_Admin.xlsx'
Trump_Admin = pd.read_excel(case2) 

#%%
# Drop columns
Trump_drop_columns = ['Total Actions', 'Total Dollars',
       'Large Business Actions', 
       'Small Business Actions', 
       'Total Education Actions',
       'HBCU (Historically Black College or University) Actions',
       'MI (Minority Institutions) Actions', 'HBCU and MI Actions',
       'Other Education Actions', 'Total Education Dollars',
       'HBCU (Historically Black College or University) Dollars',
       'MI (Minority Institutions) Dollars', 'Total of HBCU and MI Dollars',
       'Other Education Dollars',
       'Indian Tribe (Federally Recognized) Actions',
       'Indian Tribe (Federally Recognized) Dollars',
       'Native Hawaiian Organization Owned Firm Actions',
       'Native Hawaiian Organization Owned Firm Dollars',
       'Tribally Owned Firm Actions', 'Tribally Owned Firm Dollars',
       'Total Minority Owned Business Actions',
       'Asian-Pacific American Owned Actions', 'Black American Owned Actions',
       'Hispanic American Owned Actions', 'Native American Owned Actions',
       'Subcontinent Asian (Asian-Indian) Owned Actions',
       'Other Minority Owned Business Actions',
       'American Indian Owned Actions', 'American Indian Owned Dollars',
       'US Tribal Government Actions', 'US Tribal Government Dollars',
       'Alaskan Native Corporation Owned Firm Actions',
       'Alaskan Native Corporation Owned Firm Dollars',
       'U.S. Hospital Actions', 'U.S. Hospital Dollars', 'UNICOR Actions',
       'UNICOR Dollars', 'Other U.S. Government Actions',
       'Other U.S. Government Dollars', 'Non Profit Actions',
       'Non Profit Dollars', 'The AbilityOne Program Actions',
       'The AbilityOne Program Dollars', 'Foreign Concern or Entity Actions',
       'Foreign Concern or Entity Dollars',
       'U.S. Business Performing Overseas Actions',
       'U.S. Business Performing Overseas Dollars']

Trump_Admin = Trump_Admin.drop(columns=Trump_drop_columns)

# Drop rows
Trump_bad_rows = ["ADMINISTRATIVE CONFERENCE OF THE U. S.", "AGENCY FOR INTERNATIONAL DEVELOPMENT",
	"CHEMICAL SAFETY AND HAZARD INVESTIGATION BOARD",
	"COMMODITY FUTURES TRADING COMMISSION",
	"CONSUMER FINANCIAL PROTECTION BUREAU",
	"CONSUMER PRODUCT SAFETY COMMISSION","CORPORATION FOR NATIONAL AND COMMUNITY SERVICE",
	"COURT SERVICES AND OFFENDER SUPERVISION AGENCY","DEFENSE NUCLEAR FACILITIES SAFETY BOARD",
	"ELECTION ASSISTANCE COMMISSION","ENVIRONMENTAL PROTECTION AGENCY",
	"EQUAL EMPLOYMENT OPPORTUNITY COMMISSION", "EXECUTIVE OFFICE OF THE PRESIDENT",
	"EXPORT-IMPORT BANK OF THE U.S.","FEDERAL COMMUNICATIONS COMMISSION","FEDERAL ELECTION COMMISSION",
	"FEDERAL HOUSING FINANCE AGENCY","FEDERAL LABOR RELATIONS AUTHORITY"
	"FEDERAL MARITIME COMMISSION","FEDERAL MEDIATION AND CONCILIATION SERVICE",
	"FEDERAL MINE SAFETY AND HEALTH REVIEW COMMISSION","FEDERAL TRADE COMMISSION",
	"GENERAL SERVICES ADMINISTRATION","GOVERNMENT ACCOUNTABILITY OFFICE",
	"INTERNATIONAL BOUNDARY AND WATER COMMISSION: U.S.-MEXICO",
	"INTERNATIONAL TRADE COMMISSION","INTERNATIONAL TRADE COMMISSION, UNITED STATES (DUNS # 02-1877998)",
	"J. F. KENNEDY CENTER FOR THE PERFORMING ARTS","LIBRARY OF CONGRESS","MERIT SYSTEMS PROTECTION BOARD",
	"MILLENNIUM CHALLENGE CORPORATION","NATIONAL AERONAUTICS AND SPACE ADMINISTRATION",
	"NATIONAL ARCHIVES AND RECORDS ADMINISTRATION","NATIONAL CAPITAL PLANNING COMMISSION",
	"NATIONAL ENDOWMENT FOR THE ARTS","NATIONAL ENDOWMENT FOR THE HUMANITIES",
	"NATIONAL GALLERY OF ART","NATIONAL LABOR RELATIONS BOARD","NATIONAL MEDIATION BOARD",
	"NATIONAL SCIENCE FOUNDATION","NATIONAL TRANSPORTATION SAFETY BOARD",
	"NUCLEAR REGULATORY COMMISSION","OCCUPATIONAL SAFETY AND HEALTH REVIEW COMMISSION",
	"OFFICE OF PERSONNEL MANAGEMENT","OFFICE OF SPECIAL COUNSEL","OVERSEAS PRIVATE INVESTMENT CORPORATION",
	"PEACE CORPS","PENSION BENEFIT GUARANTY CORPORATION","PRETRIAL SERVICES AGENCY",
	"RAILROAD RETIREMENT BOARD","RECOVERY ACCOUNTABILITY AND TRANSPARENCY BOARD","SECURITIES AND EXCHANGE COMMISSION",
	"SELECTIVE SERVICE SYSTEM","SMALL BUSINESS ADMINISTRATION","SMITHSONIAN INSTITUTION",
	"SOCIAL SECURITY ADMINISTRATION","THE COUNCIL OF THE INSPECTORS GENERAL ON INTEGRITY AND EFFICIENCY",
	"THE INSTITUTE OF MUSEUM AND LIBRARY SERVICES","Total","UNITED STATES AGENCY FOR GLOBAL MEDIA, BBG",
	"UNITED STATES TRADE AND DEVELOPMENT AGENCY", "FEDERAL LABOR RELATIONS AUTHORITY", "FEDERAL MARITIME COMMISSION",
    "NUCLEAR WASTE TECHNICAL REVIEW BOARD", "VIETNAM EDUCATION FOUNDATION", "MARINE MAMMAL COMMISSION",
    "DISTRICT OF COLUMBIA COURTS", "COMMITTEE FOR PURCHASE FROM PEOPLE WHO ARE BLIND OR SEVERELY DISABLED",
    "UNITED STATES INTERNATIONAL DEVELOPMENT FINANCE CORPORATION"]

Trump_Admin = Trump_Admin[~Trump_Admin["Department Name"].isin(Trump_bad_rows)]
       
#%%    
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

#%%
# Create Proportions
Trump_Admin["Proportion of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Asian-Pacific American Owned Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Black American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Black American Owned Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Hispanic American Owned Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Native American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Native American Owned Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin['Proportion of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars'] = Trump_Admin["Other Minority Owned Business Dollars"]/ Trump_Admin["Total Minority Owned Business Dollars"]

#%%
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
chart2 = Trump_Data.plot.barh(stacked=True, width=0.6, ax=ax)

chart2.tick_params(axis='x', labelsize=8)

# Add labels and title
chart2.set_xlabel('Share of Total Minority Owned Business Dollars')
chart2.set_ylabel('Department Name')
chart2.set_title('Contracting Rates to Minority Owned Businesses by Executive Department \n Trump Administration')

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

#%%
Trump_Total_Data = pd.DataFrame({
    "Department Name": Trump_Admin["Department Name"],
    "Asian-Pacific American": Trump_Admin["Asian-Pacific American Owned Dollars"],
    "Black American": Trump_Admin["Black American Owned Dollars"],
    "Hispanic American": Trump_Admin["Hispanic American Owned Dollars"],
    "Native American": Trump_Admin["Native American Owned Dollars"],
    "Subcontinent Asian (Asian-Indian)": Trump_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"],
    "Other Minority": Trump_Admin["Other Minority Owned Business Dollars"]
})
# Set the index to "Department Name"
Trump_Total_Data.set_index("Department Name", inplace=True)

fig,ax=plt.subplots(figsize=(12,6))

# Create a stacked bar chart
chart = Trump_Total_Data.plot.barh(stacked=True, width=0.6, ax=ax)

chart.tick_params(axis='x', labelsize=8)

# Add labels and title
chart.set_xlabel('Total Minority Owned Business Dollars')
chart.set_ylabel('Department Name')
chart.set_title('Contracting Rates to Minority Owned Businesses by Executive Department \n Trump Administration')

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
fig.savefig('Trump_Admin_Total.png')
