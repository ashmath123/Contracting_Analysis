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

excel = 'Contracting Dollars by Administration.xlsx'
contract_dollars = pd.read_excel(excel,sheet_name=None)


