#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:09:47 2024

@author: bene
"""

import streamlit as st
import streamlit.components.v1 as components




#the body of the page
def app():

     
    #st.image("images/logo4.png",use_column_width=True)
    dash_1 = st.container()
    with dash_1:
        col_01, col_02, col_03 = st.columns([1.5,1,1.5])
        with col_02:
            st.markdown("<h2 style='text-align: center;'>Dashboard</h2>", unsafe_allow_html=True)
            st.image('thumb/park4night.png',use_column_width = "auto")
            st.write('')
    st.write("""\nDas folgende Tableau Dashboard ist ein Auszug meines Abschlussprojekt am [Data Science Institute](https://data-science-institute.de/). \n
   Für das Abschlussprojekt habe ich mittels Python alle Stellplätze der [Park4Night-App](https://park4night.com) gescraped. 
   Die Daten wurden anschließend in einer mySQL Datenbank gespeichert. \n
   Es wurden insgesamt:\n
   ♟ **294519 Stellplatzinformationen und**  \n
   ♟ **2774271 Kommentare** \n
   ♟ **in 44 Sprachen** \n
   gescraped. Weitere Informationen findest du [hier](https://github.com/BenediktFranck/park4night_app). \n\n
   _**Folgendes Tableau-Dashboard zeigt folgende 3 Informationen**_\n\n
   ♟ Weltkarte mit allen Stellplätzen auf Park4Night. Mittels keyword-Filter lassen sich Stellplätze nach Kommentaren filtern. Mit dem aktuellen keyword 'surfer' werden Stellplätze angezeigt wo man vermutlich gut surfen kann.\n
   ♟ Die Tortendiagramme zeigt die Verteilung der Stellplatzarten weltweit und nach dem ausgewählten Land.\n
   ♟ Das Liniendiagramm zeigt die jährlichen Kommentare weltweit und im vergleich mit den beliebtesten Urlaubsländern. Man erkennt einen deutlich Knick im Corona Jahr.\n
   Viel Spaß mit dem interaktiven Dashboard, probiere ruhig die Filter aus!\n\n
    """)

    html_temp = """
<div class='tableauPlaceholder' id='viz1705327172925' style='position: relative'><noscript><a href='#'><img alt='Stellplätze ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Park4Night&#47;Stellpltze&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Park4Night&#47;Stellpltze' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Park4Night&#47;Stellpltze&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='de-DE' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1705327172925');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1366px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='795px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1366px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='795px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1527px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    components.html(html_temp, width=1400, height=800)
    st.markdown(f'Link to the public dashboard [here](https://public.tableau.com/shared/BZ5DT72H7?:display_count=n&:origin=viz_share_link)')


    #max_width_str = f"max-width: 1030px;"
    #st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",unsafe_allow_html=True)

