#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:30:39 2024

@author: bene
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import plotly.express as px

def train_model_lr():
    df_top5_train = pd.read_csv('dataframes/df_top5_train.csv')
    X_train, X_test, y_train, y_test = train_test_split(df_top5_train.drop('price', axis =1)
                                                        , df_top5_train['price']
                                                        , test_size=0.33, random_state=42)
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    return lr

def train_model_dt():
    df_top5_train = pd.read_csv('dataframes/df_top5_train.csv')
    X_train, X_test, y_train, y_test = train_test_split(df_top5_train.drop('price', axis =1)
                                                        , df_top5_train['price']
                                                        , test_size=0.33, random_state=42)
    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    return dt

def train_model_rf():
    df_top5_train = pd.read_csv('dataframes/df_top5_train.csv')
    X_train, X_test, y_train, y_test = train_test_split(df_top5_train.drop('price', axis =1)
                                                        , df_top5_train['price']
                                                        , test_size=0.33, random_state=42)
    rf = RandomForestClassifier(n_estimators=2, max_depth=2)
    rf.fit(X_train, y_train)
    return rf

def train_model_all_rf():
    df_top5_train = pd.read_csv('dataframes/df_all_train.csv')
    X_train, X_test, y_train, y_test = train_test_split(df_top5_train.drop('price', axis =1)
                                                        , df_top5_train['price']
                                                        , test_size=0.33, random_state=42)
    rf_all = RandomForestClassifier(n_estimators=1, max_depth=1)
    rf_all.fit(X_train, y_train)
    return rf_all


