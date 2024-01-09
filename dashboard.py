#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:16:53 2024

@author: bene
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_extras.metric_cards import style_metric_cards # beautify metric card with css
import plotly.graph_objs as go
import plotly.express as px
from bornly import lineplot
from plotly.subplots import make_subplots


def app():
    df = pd.read_csv('dataframes/autoscout24.csv')
    df_clean = pd.read_csv('dataframes/cleaned_df.csv')
    #st.dataframe(df)
    # creates the container for page title
    dash_1 = st.container()
    
    with dash_1:
        col_01, col_02, col_03 = st.columns([1,1,1])
        with col_02:
            st.markdown("<h2 style='text-align: center;'>Dashboard</h2>", unsafe_allow_html=True)
            st.image('thumb/autoscout24.png')
        
        st.write("[Datensatzquelle](https://www.kaggle.com/datasets/ander289386/cars-germany)")
        st.write("")
    
  

    
    # creates the container for metric card
    dash_2 = st.container()
    
    with dash_2:
        # get kpi metrics
        insertions = df['make'].count()
        avg_price = df['price'].mean()
        avg_mileage = df['mileage'].mean()
        total_orders = df['make'].nunique()
    
        col1, col2, col3, col4 = st.columns(4)
        # create column span
        col1.metric(label="Anzahl Inserate", value= insertions)
        
        col2.metric(label="Durchschnittlicher Inseratspreis", value= f"{int(avg_price)} €")
        
        col3.metric(label="Durchschnittliche Kilometerzahl", value= f"{int(avg_mileage)} km")
        
        col4.metric(label="Anzahl verschiedener Automarken", value=total_orders)
        
        # this is used to style the metric card
        style_metric_cards(border_left_color="#DBF227", border_size_px=0.1)
        
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Verkaufszahlen", "Automarken", "Korrelationen", 
                                                        "Trends Zulassungsjahr", "Inseratspreise", "Kilometerzahl","DataFrame"])    
    
    with tab1:
        
        dash_3 = st.container(border=True)
        
        with dash_3:
            st.markdown("<h2 style='text-align: left;'>Wieviele Autos wurden verkauft? Über welchen Zeitraum?</h2>", unsafe_allow_html=True)
            st.info('Der Datensatz enthält nur, zum Zeitpunkt des Scrapings, inserierte Autos. Eine Aussage ob ein Auto verkauft wurde kann nicht gemacht werden. Der Datensatz enthält ebenfalls keine Information über das Datum des Inserats, lediglich über das Zulassungsjahr des inserierten Autos.', icon="ℹ️")
            st.metric(label = "Anzahl der Inserate von Autos deren Erstzulassung zwischen 2011 und 2021 liegt", value = insertions)
    
    with tab2:     
        dash_4 = st.container(border = True)
        
        with dash_4:
            
            makes = df['make'].unique()
            col1_1, col2_2 = st.columns([1,1.3])
            with col1_1:
                st.markdown("<h2 style='text-align: center;'>Welche Marken sind erfasst?</h2>", unsafe_allow_html=True)
                st.markdown('#')
                col0, col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(10)
                for index, make in enumerate(makes):
                    if index > 9:
                        index = str(index)[-1]
                    eval(f'col{index}').image(f'thumb/{make.lower()}.png')
                  
            with col2_2:  
                      st.markdown("<h2 style='text-align: center;'>Beliebte Automarken und Modelle</h2>", unsafe_allow_html=True)
                      make_counts = df[['make']].value_counts()
                      make_counts = pd.DataFrame(make_counts)
                      make_counts.reset_index(inplace=True)
                      
                      model_counts = df[['model']].value_counts()
                      model_counts = pd.DataFrame(model_counts)
                      model_counts.reset_index(inplace=True)
                      
                      fig = make_subplots(rows=2, cols=1)
                      fig.append_trace(go.Bar(
                      x=make_counts[:5]['count'],
                      y=make_counts[:5]['make'],
                      orientation='h'), row=1, col=1)

                      
                      fig.append_trace(go.Bar(
                      x=model_counts[:5]['count'],
                      y=model_counts[:5]['model'],
                      orientation='h'), row=2, col=1)
                      
                      fig.update_yaxes(dict(autorange="reversed"), row=1, col=1)
                      fig.update_xaxes(title_text="Anzahl Inserate", row=2, col=1)
                      fig.update_yaxes(dict(autorange="reversed"), row=2, col=1)
                      fig.update_layout(autosize=True, height=420)#, width=770)
                                        #title_text="Multiple Subplots with Titles")
                      fig.update_layout(showlegend=False,
                            margin=dict(l=20, r=20, t=30, b=20)
                        )
                      st.plotly_chart(fig, use_container_width=True)
                      
    with tab3:  
        dash_5 = st.container(border = True)
        
        with dash_5:
            st.markdown("<h2 style='text-align: center;'>Existieren Korrelationen zwischen den (numerischen) Features?</h2>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('')
                plt.figure()
                sns.set(rc={"figure.figsize":(61, 35)})
                sns.pairplot(df[(df['price']<100000) & (df['mileage']<300000) & (df['hp']<500)])
                sns.set(rc={'figure.figsize':(0.4,0.3)})
                st.pyplot(plt)
            
            with col2:
                col1, col2 = st.columns([1,10])
                with col2:
                    options = st.multiselect('Welche Features interessieren dich?',['mileage', 'fuel', 'gear', 'offerType','price', 'hp','year'],['mileage', 'fuel', 'gear', 'offerType','price', 'hp','year'])
                correlations = df_clean[options].corr(numeric_only = True)
                fig = px.imshow(correlations.round(2), text_auto=True, aspect="auto", width=670, height=570)
                fig.update(layout_coloraxis_showscale=False)
                fig.update_layout(showlegend=False,
                      margin=dict(l=0, r=0, t=0, b=20)
                  )
                st.plotly_chart(fig, use_container_width=True) 
                
            
                
    with tab4:  
        dash_6 = st.container(border = True)
         
        with dash_6:
             st.markdown("<h2 style='text-align: center;'>Gibt es Veränderungen über die Jahre?</h2>", unsafe_allow_html=True)
             col1, col2 = st.columns(2)
             with col1:
                 fig = lineplot(df, x="year", y="price")
                 fig.update_layout(width=670,
                 yaxis_title='Verkaufspreis [€]',
                 xaxis_title='Zulassungsjahr',
                 title='Durchschnittlicher Inseratspreis je Zulassungsjahr',
                 hovermode="closest")
                 fig.update_layout(height=400, width=670)
                 fig.update_layout(showlegend=False,
                       margin=dict(l=20, r=20, t=20, b=20)
                   )
                 st.plotly_chart(fig)
             with col2:
                 fig = lineplot(df, x="year", y="hp")
                 fig.update_layout(width=670,
                 yaxis_title='Leistung [PS]',
                 xaxis_title='Zulassungsjahr',
                 title='Durchschnittliche Leistung je Zulassungsjahr',
                 hovermode="closest")
                 fig.update_layout(height=400, width=670)
                 fig.update_layout(showlegend=False,
                       margin=dict(l=20, r=20, t=20, b=20)
                   )
                 st.plotly_chart(fig, use_container_width=True)
             
             col1, col2 = st.columns(2)
             with col1:
                 fig = lineplot(df[(df['fuel']=='Gasoline') | (df['fuel']=='Diesel') | (df['fuel']=='Electric')| (df['fuel']=='Electric/Gasoline')], x="year", y="hp", hue='fuel')
                 fig.update_layout(width=670,
                 yaxis_title='Leistung [PS]',
                 xaxis_title='Zulassungsjahr',
                 title='Durchschnittliche Leistung je Zulassungsjahr und Antriebsart',
                 hovermode="closest")
                 fig.update_layout(height=400, width=670)
                 fig.update_layout(showlegend=False,
                       margin=dict(t=20)
                   )
                 st.plotly_chart(fig)
             
             with col2:
                 fuel_df = df.groupby(['fuel','year'], as_index=False)['make'].count()
                 fig = lineplot(fuel_df[(fuel_df['make']>30)], x="year", y="make", hue = 'fuel')
                 fig.update_layout(width=670,
                 yaxis_title='Anzahl Inserate',
                 xaxis_title='Zulassungsjahr',
                 title='Anzahl Inserate (>30) je Zulassungsjahr und Antriebsart',
                 hovermode="closest")
                 fig.update_layout(height=400, width=670)
                 fig.update_layout(showlegend=True,
                       margin=dict(t=20)
                   )
                 st.plotly_chart(fig,use_container_width=True)
      

    with tab5:  
        dash_8 = st.container(border=True)
          
        with dash_8:
              st.markdown("<h2 style='text-align: left;'>Preise der verschiedenen Automarken</h2>", unsafe_allow_html=True)
    
              top_10_maked = make_counts['make'][:10].tolist()
              make_list = st.multiselect('Welche Marken interessieren dich?',df['make'].unique().tolist(),top_10_maked)        
              filtered_df = df[df['make'].isin(make_list)]
            
    
              fig = px.box(filtered_df, x='make',y="price")
              fig.update_layout(
              yaxis_title='Inseratspreis [€]',
              xaxis_title='Automarke',
              hovermode="closest")
              fig.update_yaxes(range=[0, 75000])
              fig.update_layout(height=600, width=1340)
              st.plotly_chart(fig,use_container_width=True)
              
              

              col1, col2 = st.columns(2)
              with col1:
                  teuerste = df.groupby(["make"])['price'].median().sort_values(ascending=False)
                  teuerste = pd.DataFrame(teuerste)
                  teuerste.reset_index(inplace=True)
      
                  fig = go.Figure(go.Bar(
                  x=teuerste[:5]['make'],
                  y=teuerste[:5]['price']))
                  #fig.update_layout(yaxis=dict(autorange="reversed"))
                  fig.update_layout(
                  title='Top 5 teuersten Automarken',  
                  yaxis_title='Durchschnittlicher Inseratspreis [€]',
                  hovermode="closest")
                  fig.update_layout(height=400, width=670)
                  fig.update_layout(showlegend=False,
                       margin=dict(t=20)
                   )
                  st.plotly_chart(fig,use_container_width=True)
                  
              with col2:      
                  teuerste_model = df.groupby(["model"])['price'].median().sort_values(ascending=False)
                  teuerste_model = pd.DataFrame(teuerste_model)
                  teuerste_model.reset_index(inplace=True)
      
                  fig = go.Figure(go.Bar(
                  x=teuerste_model[:5]['model'],
                  y=teuerste_model[:5]['price']))
                  #fig.update_layout(yaxis=dict(autorange="reversed"))
                  fig.update_layout(
                  title='Top 5 teuersten Automodelle',  
                  yaxis_title='Durchschnittlicher Inseratspreis [€]',
                  hovermode="closest")
                  fig.update_layout(height=400, width=670)
                  fig.update_layout(showlegend=False,
                       margin=dict(t=20)
                   )
                  st.plotly_chart(fig,use_container_width=True)

              col1, col2 = st.columns(2)
              with col1:
                  make_counts = df[['make']].value_counts()
                  make_counts = pd.DataFrame(make_counts)
                  make_counts.reset_index(inplace=True)
                  make_counts = make_counts[(make_counts['count']>=100)]
                  make_counts = df[df['make'].isin(make_counts['make'].tolist())]
                  cheapest = make_counts.groupby(["make"])['price'].median().sort_values(ascending=False)
                  cheapest = pd.DataFrame(cheapest)
                  cheapest.reset_index(inplace=True)
    
                  fig = go.Figure(go.Bar(
                  x=cheapest[-5:]['make'],
                  y=cheapest[-5:]['price']))
                  fig.update_layout(xaxis=dict(autorange="reversed"))
                  #fig.update_layout(yaxis=dict(autorange="reversed"))
                  fig.update_layout(
                  title='Top 5 günstigsten Automarken',  
                  yaxis_title='Durchschnittlicher Inseratspreis [€]',
                  hovermode="closest")
                  fig.update_layout(height=400, width=670)
                  fig.update_layout(showlegend=False,
                        margin=dict(t=20)
                    )
                  st.plotly_chart(fig,use_container_width=True)
                  
              with col2:
                  make_counts = df[['model']].value_counts()
                  make_counts = pd.DataFrame(make_counts)
                  make_counts.reset_index(inplace=True)
                  make_counts = make_counts[(make_counts['count']>=100)]
                  make_counts = df[df['model'].isin(make_counts['model'].tolist())]
                  cheapest = make_counts.groupby(["model"])['price'].median().sort_values(ascending=False)
                  cheapest = pd.DataFrame(cheapest)
                  cheapest.reset_index(inplace=True)
    
                  fig = go.Figure(go.Bar(
                  x=cheapest[-5:]['model'],
                  y=cheapest[-5:]['price']))
                  fig.update_layout(xaxis=dict(autorange="reversed"))
                  #fig.update_layout(yaxis=dict(autorange="reversed"))
                  fig.update_layout(
                  title='Top 5 günstigsten Automodelle',  
                  yaxis_title='Durchschnittlicher Inseratspreis [€]',
                  hovermode="closest")
                  fig.update_layout(height=400, width=670)
                  fig.update_layout(showlegend=False,
                        margin=dict(t=20)
                    )
                  st.plotly_chart(fig,use_container_width=True)
                  
        
    with tab6:  
        dash_9 = st.container(border = True)
   

        with dash_9:
              st.markdown("<h2 style='text-align: left;'>Mit welchen Automodellen werden die meisten/wenigsten Kilometer gefahren bevor es verkauft wird.</h2>", unsafe_allow_html=True)
              st.info('Es werden nur Automodelle berücksichtigt welche min. 50x im Datensatz vorhanden sind.', icon="ℹ️")
              #DataFrame mit milage_per_age 
              df_model = df_clean
              df_model["age"] = 2021 - df_model["year"] + 1
              df_model["mileage_per_age"] = df_model["mileage"]/(df_model["age"])
              df_model = df_clean.groupby(["make", "model"])
              df_model = df_model['mileage_per_age'].mean().sort_values(ascending=False)
              df_model = pd.DataFrame(df_model)
              df_model.reset_index(inplace=True)
              df_model['make_model'] = df_model['make'] + ' ' + df_model['model']
              
              col1, col2 = st.columns(2)
              with col1:
                  fig = go.Figure(go.Bar(
                  x=df_model[:5]['mileage_per_age'],
                  y=df_model[:5]['make_model'],
                  orientation='h'))
                  fig.update_layout(yaxis=dict(autorange="reversed"))
                  fig.update_layout(
                  title='Top 5 Automodelle mit den meisten jährlich gefahrenen Kilometern',  
                  xaxis_title='Kilometer pro Jahr',
                  hovermode="closest")
                  fig.update_layout(height=400, width=670)
                  fig.update_layout(showlegend=False,
                        margin=dict(t=20)
                    )
                  st.plotly_chart(fig)
              
              with col2:
                  fig = go.Figure(go.Bar(
                  x=df_model[-5:]['mileage_per_age'],
                  y=df_model[-5:]['make_model'],
                  orientation='h'))
                  fig.update_layout(
                  title='Top 5 Automodelle mit den wenigsten jährlich gefahrenen Kilometern',  
                  xaxis_title='Kilometer pro Jahr',
                  hovermode="closest")
                  fig.update_layout(height=400, width=670)
                  fig.update_layout(showlegend=False,
                        margin=dict( t=20)
                    )
                  st.plotly_chart(fig,use_container_width=True)
    with tab7:  
        st.dataframe(df,use_container_width=True)

          

          
          