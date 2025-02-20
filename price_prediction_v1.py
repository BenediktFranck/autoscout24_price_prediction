#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:55:54 2024

@author: bene
"""

import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go
from ml_models import train_model_lr, train_model_dt, train_model_rf
#from sklearn.ensemble import RandomForestClassifier




def app():
    st.markdown("<h2 style='text-align: center;'>Preisrechner</h2>", unsafe_allow_html=True)
    st.write("")
    tab1, tab2 = st.tabs(["Top 5 inserierte Automarken", "Alle Automarken"])    
    
    with tab1:
        st.info('Folgender Preisrechner wurde mittels supervised learning anhand des autoscout24 Datensatzes entwickelt.', icon="ℹ️")
        col1_1, col2_2 = st.columns(2)
        
        with col1_1:
            dash_1 = st.container(border = True)
            with dash_1:
                df_top5 = pd.read_csv('dataframes/df_top5.csv')
                vorhersage = pd.read_csv('dataframes/df_top5_prediction.csv')
                vorhersage.drop(['price'], axis = 1, inplace= True)
                vorhersage = vorhersage.head(0)

                @st.cache_resource
                def load_model_lr():
                    model_lr = train_model_lr()
                    return model_lr
                        
                @st.cache_resource
                def load_model_dt():
                    model_dt = train_model_dt()
                    return model_dt
                    
                @st.cache_resource
                def load_model_rf():
                    model_rf = train_model_rf()
                    return model_rf
                
                if "graph_lr" not in st.session_state:  
                    st.session_state.graph_lr = None
                    with open('graphs/lin_reg_fig.pkl', 'rb') as file:
                        st.session_state.graph_lr = pickle.load(file)
                if "graph_dct" not in st.session_state:  
                    st.session_state.graph_dct = None
                    with open('graphs/decs_tree_fig.pkl', 'rb') as file:
                        st.session_state.graph_dct = pickle.load(file)
                if "graph_rf" not in st.session_state:  
                    st.session_state.graph_rf = None
                    with open('graphs/rand_forest_fig.pkl', 'rb') as file:
                        st.session_state.graph_rf = pickle.load(file)
                
                
                
        
                col1, col2 = st.columns(2)
                with col1:
            
                    make = st.selectbox('Bitte wähle deine Automarke', df_top5['make'].unique().tolist())
                    vorhersage.at[0, make] = True
                    year = st.text_input('Zulassungsjahr', '2019')
                    vorhersage.at[0, 'year'] = int(year)
                    hp = st.text_input('Leistung in PS', '110')
                    vorhersage.at[0, 'hp'] = int(hp)
                    offerType = st.selectbox('Um was für ein Auto handelt es sich?', ['Used','Demonstration',"Employee's car", 'Pre-registered', 'New'])
                    if offerType == 'Used':
                        offerType = 0
                    elif offerType == 'Demonstration':
                        offerType = 1
                    elif offerType == "Employee's car":
                        offerType = 2
                    elif offerType == 'Pre-registered':
                        offerType = 3
                    elif offerType == 'New':
                        offerType = 4
                        
                    vorhersage.at[0, 'offerType'] = offerType
                    
                    model_select = st.selectbox(
                    'Welchen Classifier möchtest du verwenden?',
                    ('LinearRegression', 'DecisionTree', 'RandomForest'))
                    
                with col2:    
                    model = st.selectbox('Bitte wähle dein Automodell', df_top5[(df_top5['make']==make)]['model'].unique().tolist())
                    vorhersage.at[0, model] = True
                    mileage = st.text_input('Kilometerzahl', '1000')
                    vorhersage.at[0, 'mileage'] = int(mileage)
                    gear = st.selectbox('Bitte wähle dein Getriebe aus', ['Manual','Automatic','Semi-automatic'])
                    if gear == 'Manual':
                        gear = 0
                    elif gear == 'Automatic':
                        gear = 1
                    elif gear == 'Semi-automatic':
                        gear = 2
                    vorhersage.at[0, 'gear'] = gear
                    st.write('')
                button = st.button('Berechne Verkaufspreis')
        
                vorhersage = vorhersage.fillna(False)
                    
    
            
    
            
        with col2_2:
            dash_2 = st.container(border = True)
            with dash_2:
                if button:
                    if model_select == 'LinearRegression':
                        model_lr = load_model_lr()
                        preis = model_lr.predict(vorhersage)
                    elif model_select == 'DecisionTree':
                        model_dt = load_model_dt()
                        preis = model_dt.predict(vorhersage)
                    elif model_select == 'RandomForest':
                        model_rf = load_model_rf()
                        preis = model_rf.predict(vorhersage)
                
                    st.success(f'Der vorgeschlagene Inseratspreis deines Autos beträgt {int(preis[0])} €')

                    fig = px.box(x=df_top5[(df_top5['make']==make)&(df_top5['model']==model)]['make'],
                                 y= df_top5[(df_top5['make']==make)&(df_top5['model']==model)]['price'])
                    fig.update_layout(height=380,width=670,
                    title = 'Vergleichspreise anderer Verkäufer mit dem gleichen Automodell',
                    yaxis_title='Inseratspreis [€]',
                    xaxis_title=model,
                    hovermode="closest")
                    fig.update_layout(showlegend=True,
                           margin=dict(t=30)
                       )

                    fig.layout.xaxis2 = go.layout.XAxis(overlaying='x', range=[0,2], showticklabels=False)
                    fig.add_scatter(x = [0,2], y = [preis[0],preis[0]], mode='lines', xaxis='x2',
                                        showlegend=True, line=dict(dash='dash', color = "firebrick", width = 2), name='Dein Verkaufspreis')
            
                    st.plotly_chart(fig, use_container_width=True)
                    
        with st.expander("Fehlermetrik"):
                st.info('Um die Güte des Modells zu verbesser wurden nur Automodelle berücksichtigt welche min. 100x im Datensatz vorhanden sind.', icon="ℹ️")
                st.write("[Jupyter Notebook](https://github.com/BenediktFranck/autoscout24_price_prediction/blob/main/Dataset_autoscout24.ipynb)")
                
                df_scores = pd.DataFrame([['1868.4', '2785.4', '0.88'],['1650.6','2830.4','0.87'],['1470.11','2519.0','0.90']],
                                         columns=['Mean Absolute Error (MAE)','Root Mean Squared Error (RMSE)', 'Bestimmheitsmaß R2'],
                                         index=['LinearRegression','DecisionTree','RandomForest'])
                st.table(df_scores)
                col1, col2, col3 = st.columns(3)
                with col1:
                    fig = st.session_state.graph_lr
                    fig.update_layout(height=420)
                    st.plotly_chart(fig, use_container_width=True)
                with col2:
                    fig = st.session_state.graph_dct
                    fig.update_layout(height=420)
                    st.plotly_chart(fig, use_container_width=True)
                with col3:
                    fig = st.session_state.graph_rf
                    fig.update_layout(height=420)
                    st.plotly_chart(fig, use_container_width=True)
                    
    with tab2:
        st.info('Aufgrund der begrenzen Ressourcen von Streamlit kann das Preisrechner nicht für alle Automarken angewendet werden. Bei Interesse kann aber eine lokal gehostete Streamlit-Instanz [hier](https://github.com/BenediktFranck/autoscout24_price_prediction) heruntergeladen und gestartet werden.', icon="ℹ️")