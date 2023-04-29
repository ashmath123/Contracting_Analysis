#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:28:57 2023

@author: ashleymathew
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300

Obama_Admin = pd.read_csv("Obama_Admin_Filtered.csv")
Trump_Admin = pd.read_csv("Trump_Admin_Filtered.csv")
Biden_Admin = pd.read_csv("Biden_Admin_Filtered.csv")

# Create percentage
Obama_Admin["MOB_Total_Obama"] = (Obama_Admin["Total Minority Owned Business Dollars"]/ Obama_Admin["Total Dollars"])*100
Trump_Admin["MOB_Total_Trump"] = (Trump_Admin["Total Minority Owned Business Dollars"]/ Trump_Admin["Total Dollars"])*100
Biden_Admin["MOB_Total_Biden"] = (Biden_Admin["Total Minority Owned Business Dollars"]/ Biden_Admin["Total Dollars"])*100

print(Obama_Admin["MOB_Total_Obama"],Trump_Admin["MOB_Total_Trump"],Biden_Admin["MOB_Total_Biden"])