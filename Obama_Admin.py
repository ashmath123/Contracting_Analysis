#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 23:51:22 2023

@author: ashleymathew
"""
# Import Standad packages
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300

# Import data for the Obama administration
case1 = 'Obama_Admin.xlsx'
Obama_Admin = pd.read_excel(case1)

#%%
# Drop columns
Obama_drop_columns = ['Total Actions', 
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

Obama_Admin = Obama_Admin.drop(columns=Obama_drop_columns)

# Drop rows
Obama_bad_rows = ["ADMINISTRATIVE CONFERENCE OF THE U. S.", "AGENCY FOR INTERNATIONAL DEVELOPMENT",
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
	"UNITED STATES TRADE AND DEVELOPMENT AGENCY", "FEDERAL LABOR RELATIONS AUTHORITY", "FEDERAL MARITIME COMMISSION"]

Obama_Admin = Obama_Admin[~Obama_Admin["Department Name"].isin(Obama_bad_rows)]

#%%

def update_columns(Obama_Admin, columns):
    for col in columns:
        Obama_Admin[col] = Obama_Admin[col].astype(str)
        Obama_Admin[col] = Obama_Admin[col].str.replace(',', '').str.replace('$', '').astype(float)

update_columns(Obama_Admin, ["Total Dollars", "Total Minority Owned Business Dollars", 
                             "Small Business Dollars", "Asian-Pacific American Owned Dollars", 
                             "Black American Owned Dollars", "Hispanic American Owned Dollars", 
                             "Native American Owned Dollars", "Subcontinent Asian (Asian-Indian) Owned Dollars", 
                             "Other Minority Owned Business Dollars"])

#%%
# Create Proportions
Obama_Admin["Percent of Minority Owned Business Contracting to Total Contracting Dollars"] = ((Obama_Admin["Total Minority Owned Business Dollars"]/8)/(Obama_Admin["Total Dollars"]/8))*100

denominator = Obama_Admin["Total Minority Owned Business Dollars"]/8

Obama_Admin["Percent of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"] = ((Obama_Admin["Asian-Pacific American Owned Dollars"]/8)/ denominator)*100
Obama_Admin["Percent of Black American Owned Dollars to Total Minority Owned Business Dollars"] = ((Obama_Admin["Black American Owned Dollars"]/8)/ denominator)*100
Obama_Admin["Percent of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"] = ((Obama_Admin["Hispanic American Owned Dollars"]/8)/ denominator)*100
Obama_Admin["Percent of Native American Owned Dollars to Total Minority Owned Business Dollars"] = ((Obama_Admin["Native American Owned Dollars"]/8)/ denominator)*100
Obama_Admin["Percent of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"] = ((Obama_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"]/8)/ denominator)*100
Obama_Admin["Percent of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars"] = ((Obama_Admin["Other Minority Owned Business Dollars"]/8)/ denominator)*100

# Save good DataFrame to csv
Obama_Admin.to_csv("Obama_Admin_Filtered.csv")

#%%
Obama_Data = pd.DataFrame({
    "Department Name": Obama_Admin["Department Name"],
    "Asian-Pacific American": Obama_Admin["Percent of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"],
    "Black American": Obama_Admin["Percent of Black American Owned Dollars to Total Minority Owned Business Dollars"],
    "Hispanic American": Obama_Admin["Percent of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"],
    "Native American": Obama_Admin["Percent of Native American Owned Dollars to Total Minority Owned Business Dollars"],
    "Subcontinent Asian (Asian-Indian)": Obama_Admin["Percent of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"],
    "Other Minority": Obama_Admin["Percent of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars"]
})

# Set the index to "Department Name"
Obama_Data.set_index("Department Name", inplace=True)

fig,ax=plt.subplots(figsize=(12,6))

# Create a stacked bar chart
chart = Obama_Data.plot.barh(stacked=True, width=0.6, ax=ax)

chart.tick_params(axis='x', labelsize=8)

# Add labels and title
chart.set_xlabel("Percent of Total Minority Owned Business Dollars Spent")
chart.set_ylabel("Department Name")
chart.set_title("Contracting Percentages to Minority Owned Businesses \n Obama Administration - Executive Departments")

# Adjust the font size of the x-axis labels
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
fig.savefig("Obama_Admin.png")

#%%
Obama_Total_Data = pd.DataFrame({
    "Department Name": Obama_Admin["Department Name"],
    "Asian-Pacific American": (Obama_Admin["Asian-Pacific American Owned Dollars"]/8)/1e9,
    "Black American": (Obama_Admin["Black American Owned Dollars"]/8)/1e9,
    "Hispanic American": (Obama_Admin["Hispanic American Owned Dollars"]/8)/1e9,
    "Native American": (Obama_Admin["Native American Owned Dollars"]/8)/1e9,
    "Subcontinent Asian (Asian-Indian)": (Obama_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"]/8)/1e9,
    "Other Minority": (Obama_Admin["Other Minority Owned Business Dollars"]/8)/1e9
})
# Set the index to "Department Name"
Obama_Total_Data.set_index("Department Name", inplace=True)

# Sort the data from smallest to largest
Obama_Total_Data_Sorted = Obama_Total_Data.loc[Obama_Total_Data.sum(axis=1).sort_values(ascending=False).index]

# Create a stacked bar chart
fig,ax=plt.subplots(figsize=(12,6))
chart = Obama_Total_Data_Sorted.plot.barh(stacked=True, width=0.6, ax=ax)

chart.tick_params(axis='x', labelsize=8)

# Add labels and title
chart.set_xlabel("Total Minority Owned Business Dollars (in Billions)")
chart.set_ylabel("Department Name")
chart.set_title("Annual Contracting Dollars to Minority Owned Businesses - Total Spend \n Obama Administration - Executive Departments")

# Adjust the font size of the x-axis labels
chart.tick_params(axis='x', labelsize=7)

# Increase the spacing between the bars
chart.set_axisbelow(True)
chart.yaxis.grid(True)
chart.xaxis.grid(False)
chart.set_axisbelow(True)
chart.legend(loc="upper left", bbox_to_anchor=(1,1))
fig.tight_layout()
# Save the plot to a file
fig.savefig("Obama_Admin_Total.png")

#%%






