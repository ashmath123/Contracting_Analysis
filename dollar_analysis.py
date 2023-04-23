#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 23:51:22 2023

@author: ashleymathew
"""
import pandas as pd
import geopandas as gpd
import os
import glob

case1 = 'Obama_Admin.xlsx'
Obama_Admin = pd.read_excel(case1)

case2 = 'Trump_Admin.xlsx'
Trump_Admin = pd.read_excel(case2)

case3 = 'Biden_Admin.xlsx'
Biden_Admin = pd.read_excel(case3)

Obama_Admin["Proportion of Total Minority Owned Business Dollars to Total Small Business Dollars"] = Obama_Admin["Total Minority Owned Business Dollars"] / Obama_Admin["Small Business Dollars"]     

Obama_Admin["Proportion of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Asian-Pacific American Owned Dollars"] / Obama_Admin["Total Minority Owned Business Dollars"]     
Obama_Admin["Proportion of Black American Owned Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Black American Owned Dollars"] / Obama_Admin["Total Minority Owned Business Dollars"]
Obama_Admin["Proportion of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Hispanic American Owned Dollars"] / Obama_Admin["Total Minority Owned Business Dollars"]
Obama_Admin["Proportion of Native American Owned Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Native American Owned Dollars"] / Obama_Admin["Total Minority Owned Business Dollars"]
Obama_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] / Obama_Admin["Total Minority Owned Business Dollars"]
Obama_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] / Obama_Admin["Total Minority Owned Business Dollars"]
Obama_Admin["Proportion of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars"] = Obama_Admin["Other Minority Owned Business Dollars"] / Obama_Admin["Total Minority Owned Business Dollars"]

Trump_Admin["Proportion of Total Minority Owned Business Dollars to Total Small Business Dollars"] = Trump_Admin["Total Minority Owned Business Dollars"] / Trump_Admin["Small Business Dollars"]     

Trump_Admin["Proportion of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Asian-Pacific American Owned Dollars"] / Trump_Admin["Total Minority Owned Business Dollars"]     
Trump_Admin["Proportion of Black American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Black American Owned Dollars"] /Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Hispanic American Owned Dollars"] / Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Native American Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Native American Owned Dollars"] / Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] / Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] / Trump_Admin["Total Minority Owned Business Dollars"]
Trump_Admin["Proportion of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars"] = Trump_Admin["Other Minority Owned Business Dollars"] / Trump_Admin["Total Minority Owned Business Dollars"]

Biden_Admin["Proportion of Total Minority Owned Business Dollars to Total Small Business Dollars"] = Biden_Admin["Total Minority Owned Business Dollars"] / Trump_Admin["Small Business Dollars"]     

Biden_Admin["Proportion of Asian-Pacific American Owned Dollars to Total Minority Owned Business Dollars"] = Biden_Admin["Asian-Pacific American Owned Dollars"] / Biden_Admin["Total Minority Owned Business Dollars"]     
Biden_Admin["Proportion of Black American Owned Dollars to Total Minority Owned Business Dollars"] = Biden_Admin["Black American Owned Dollars"] /Biden_Admin["Total Minority Owned Business Dollars"]
Biden_Admin["Proportion of Hispanic American Owned Dollars to Total Minority Owned Business Dollars"] = Biden_Admin["Hispanic American Owned Dollars"] / Biden_Admin["Total Minority Owned Business Dollars"]
Biden_Admin["Proportion of Native American Owned Dollars to Total Minority Owned Business Dollars"] = Biden_Admin["Native American Owned Dollars"] / Biden_Admin["Total Minority Owned Business Dollars"]
Biden_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"] = Biden_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] / Biden_Admin["Total Minority Owned Business Dollars"]
Biden_Admin["Proportion of Subcontinent Asian (Asian-Indian) Owned Dollars to Total Minority Owned Business Dollars"] = Biden_Admin["Subcontinent Asian (Asian-Indian) Owned Dollars"] / Biden_Admin["Total Minority Owned Business Dollars"]
Biden_Admin["Proportion of Other Minority Owned Business Dollars to Total Minority Owned Business Dollars"] = Biden_Admin["Other Minority Owned Business Dollars"] / Biden_Admin["Total Minority Owned Business Dollars"]




