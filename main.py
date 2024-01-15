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

st.set_page_config(layout="wide")

pages = {
    "1. Über mich": resume,
    "2. Autoscout24 Dashboard": dashboard,
    "3. Preisrechner": price_prediction_v1
    #"4. Model": price_prediction
}

st.sidebar.title("Seitenmenü")
select = st.sidebar.radio("Gehe zu Seite", list(pages.keys()))
pages[select].app()
