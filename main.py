#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:29:00 2024

@author: bene
"""

import streamlit as st


import dashboard
import resume
import price_prediction_v1
import tableau

st.set_page_config(layout="wide")

pages = {
    "1. Über mich": resume,
    "2. Data Analysis": dashboard,
    "3. Machine Learning": price_prediction_v1,
    "4. Tableau": tableau
}

st.sidebar.title("Seitenmenü")
select = st.sidebar.radio("Gehe zu Seite", list(pages.keys()))
pages[select].app()
