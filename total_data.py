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

admins = {"Obama": Obama_Admin,
         "Trump": Trump_Admin,
         "Biden": Biden_Admin}

Total_Data = pd.concat(admins).reset_index()
Total_Data["Department Name"] = Total_Data["Department Name"].str.strip()
pivot_table = Total_Data.pivot(index="Department Name", columns="level_0", values="Percent of Minority Owned Business Contracting to Total Contracting Dollars").round(2)




















