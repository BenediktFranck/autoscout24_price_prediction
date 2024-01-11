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
from ml_models import train_model_lr, train_model_dt, train_model_rf, train_model_all_rf
#from sklearn.ensemble import RandomForestClassifier




def app():
    st.markdown("<h2 style='text-align: center;'>Preisrechner</h2>", unsafe_allow_html=True)
    st.write("")
    tab1, tab2 = st.tabs(["Top 5 inserierte Automarken", "Alle Automarken"])    
    
    with tab1:
        col1_1, col2_2 = st.columns(2)
        
        with col1_1:
            dash_1 = st.container(border = True)
            with dash_1:
                df_top5 = pd.read_csv('dataframes/df_top5.csv')
                vorhersage = pd.read_csv('dataframes/df_top5_prediction.csv')
                vorhersage.drop(['price'], axis = 1, inplace= True)
                vorhersage = vorhersage.head(0)
                
                
                if "model_lr" not in st.session_state:  
                    st.session_state.model_lr = None
                    with open('models/linreg_top5.pkl', 'rb') as file:
                        st.session_state.model_lr = train_model_lr()
                        
                if "model_dt" not in st.session_state:  
                    st.session_state.model_dt = None
                    with open('models/decisiontree_top5.pkl', 'rb') as file:
                        st.session_state.model_dt = train_model_dt()
                        
                if "model_rf" not in st.session_state:  
                    st.session_state.model_rf = None
                    with open('models/randomforest_top5.pkl', 'rb') as file:
                        st.session_state.model_rf = train_model_rf()
                
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
                    if model_select == 'LinearRegression' and st.session_state.model_lr != None:
                        preis = st.session_state.model_lr.predict(vorhersage)
                    elif model_select == 'DecisionTree' and st.session_state.model_dt != None:
                        preis = st.session_state.model_dt.predict(vorhersage)
                    elif model_select == 'RandomForest' and st.session_state.model_rf != None:
                        preis = st.session_state.model_rf.predict(vorhersage)
                
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
                    
#MachineLearning Model für alle Automarken                
    with tab2:
        col1_1, col2_2 = st.columns(2)
        
        with col1_1:
            dash_1 = st.container(border = True)
            with dash_1:
                df_all = pd.read_csv('dataframes/df_all.csv')
                vorhersage_all = pd.read_csv('dataframes/df_all_prediction.csv')
                vorhersage_all.drop(['price'], axis = 1, inplace= True)
                vorhersage_all = vorhersage_all.head(0)
                    
                        
                if "model_rf_all" not in st.session_state:  
                    st.session_state.model_rf_all = None
                    with open('models/randomforest_all.pkl', 'rb') as file:
                        st.session_state.model_rf_all = train_model_all_rf()
                
                if "graph_rf_all" not in st.session_state:  
                    st.session_state.graph_rf_all = None
                    with open('graphs/rand_forest_all_fig.pkl', 'rb') as file:
                        st.session_state.graph_rf_all = pickle.load(file)
                
                
                
        
                col1, col2 = st.columns(2)
                with col1:
            
                    make_all = st.selectbox('Bitte wähle deine Automarke', df_all['make'].unique().tolist(), key='make_all')
                    vorhersage_all.at[0, make_all] = True
                    year_all = st.text_input('Zulassungsjahr', '2019', key='year_all')
                    vorhersage_all.at[0, 'year'] = int(year_all)
                    hp_all = st.text_input('Leistung in PS', '110', key='hp_all')
                    vorhersage_all.at[0, 'hp'] = int(hp_all)
                    offerType_all = st.selectbox('Um was für ein Auto handelt es sich?', 
                                                 ['Used','Demonstration',"Employee's car", 'Pre-registered', 'New'], key='offerType_all')
                    if offerType_all == 'Used':
                        offerType_all = 0
                    elif offerType_all == 'Demonstration':
                        offerType_all = 1
                    elif offerType_all == "Employee's car":
                        offerType_all = 2
                    elif offerType_all == 'Pre-registered':
                        offerType_all = 3
                    elif offerType_all == 'New':
                        offerType_all = 4
                        
                    vorhersage_all.at[0, 'offerType'] = offerType_all
                    
                    
                with col2:    
                    model_all = st.selectbox('Bitte wähle dein Automodell', df_all[(df_all['make']==make_all)]['model'].unique().tolist(),key='model_all')
                    vorhersage_all.at[0, model_all] = True
                    mileage_all = st.text_input('Kilometerzahl', '1000', key='mileage_all')
                    vorhersage_all.at[0, 'mileage'] = int(mileage_all)
                    gear_all = st.selectbox('Bitte wähle dein Getriebe aus', ['Manual','Automatic','Semi-automatic'],key='gear_all')
                    if gear_all == 'Manual':
                        gear_all = 0
                    elif gear_all == 'Automatic':
                        gear_all = 1
                    elif gear_all == 'Semi-automatic':
                        gear_all = 2
                    vorhersage_all.at[0, 'gear'] = gear_all
                    st.write('')
                button_2 = st.button('Berechne Verkaufspreis', key='button_2')
        
                vorhersage_all = vorhersage_all.fillna(False)
                    
            
        with col2_2:
            dash_2 = st.container(border = True)
            with dash_2:
                if button_2:
                    if st.session_state.model_rf_all != None:
                        preis = st.session_state.model_rf_all.predict(vorhersage_all)

                
                    st.success(f'Der vorgeschlagene Inseratspreis deines Autos beträgt {int(preis[0])} €')
                        
                    fig = px.box(x=df_all[(df_all['make']==make)&(df_all['model']==model)]['make'],
                                 y= df_all[(df_all['make']==make)&(df_all['model']==model)]['price'])
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
                
                df_scores_all = pd.DataFrame([['1558.8', '2646.3', '0.92']],
                                         columns=['Mean Absolute Error (MAE)','Root Mean Squared Error (RMSE)', 'Bestimmheitsmaß R2'],
                                         index=['RandomForest'])
                st.table(df_scores_all)
                fig = st.session_state.graph_rf_all
                st.plotly_chart(fig, use_container_width=True)
