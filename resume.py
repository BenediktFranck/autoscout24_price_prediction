#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:52:01 2024

@author: bene
"""

from pathlib import Path

import streamlit as st
from PIL import Image




def app():
 
    col1, col2, col3 = st.columns([1, 3, 1], gap="small")
    
    with col2:
    
        # --- PATH SETTINGS ---
        #current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
        #css_file = current_dir / "styles" / "main.css"
        resume_file = 'assets/cv.pdf'
        profile_pic = 'assets/profile-pic.png'
     
        Path(__file__).parents[1] / 'GarretBurhennData/Garret_Burhenn_Pitches.csv'
        
        # --- GENERAL SETTINGS ---
        PAGE_TITLE = "Digital CV | John Doe"
        NAME = "Benedikt Franck"
        DESCRIPTION = """
        Junior Data Analyst, zur datengestützten Entscheidungsfindung.
        """
        EMAIL = "Benedikt.Franck@protonmail.com"
        SOCIAL_MEDIA = {
            "LinkedIn": "https://linkedin.com/in/benedikt-franck",
            "GitHub": "https://github.com/BenediktFranck",
        }
        PROJECTS = {
            "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
            "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
            "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
            "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
        }
        
        
        #st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
        
        
        # --- LOAD CSS, PDF & PROFIL PIC ---
        #with open(css_file) as f:
         #   st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
        with open(resume_file, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        profile_pic = Image.open(profile_pic)
        
        
        # --- HERO SECTION ---
        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.image(profile_pic, width=230)
            
        
        
        with col2:
            st.title(NAME)
            st.write(DESCRIPTION)
            st.download_button(
                label=" 📄 Download Lebenslauf",
                data=PDFbyte,
                file_name=resume_file,
                mime="application/octet-stream",
            )
            st.write("📫", EMAIL)
        
        
        # --- SOCIAL LINKS ---
        st.write('\n')
        cols = st.columns(len(SOCIAL_MEDIA))
        cols[0].markdown('''
        <a href="https://linkedin.com/in/benedikt-franck">
            <img src="https://static-00.iconduck.com/assets.00/linkedin-icon-2048x2048-ya5g47j2.png" width="50" height="50" />
        </a>''',
        unsafe_allow_html=True)
        cols[1].markdown('''
        <a href="https://github.com/BenediktFranck">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/1024px-GitHub_Invertocat_Logo.svg.png" width="50" height="50" />
        </a>''',
        unsafe_allow_html=True)

        
        
        # --- EXPERIENCE & QUALIFICATIONS ---
        st.write('\n')
        st.subheader("Erfahrung und Qualifikationen")
        st.write(
            """
        ✔️ 6-jährige Berufserfahrung als wissenschaftlicher Mitarbeiter \n
        ✔️ Praktische Erfahrung und Kenntnisse in Python, SQL, Tableau und Excel \n
        ✔️ Gute Kenntnisse der statistischen Grundsätze und ihrer jeweiligen Anwendungen \n
        ✔️ Teamplayer mit ausgeprägtem Sinn für Eigeninitiative bei der Erfüllung von Aufgaben 
        """
        )
        
        
        # --- SKILLS ---
        st.write('\n')
        st.subheader("Hard Skills")
        st.write(
            """
        👩‍💻 Prammierung: Python (Scikit-learn, Pandas), SQL, VBA \n
        📊 Datenvisualisierung: Tableau, MS Excel, Seaborn, Plotly \n
        📚 Machine Learning: Logistic regression, linear regression, decition trees \n
        🗄️ Datenbanken: MySQL, SQLite
        """
        )
        
        
        # --- WORK HISTORY ---
        st.write('\n')
        st.subheader("Berufserfahrung")
        st.write("---")
        
        # --- JOB 1
        st.write("🚧", "**Wissenschaftlicher Mitarbeiter | Universität Stuttgart**")
        st.write("11/2017 - 04/2023")
        st.write(
            """
        **Entwicklung und Automatisierung von datengetriebenen Prüfständen:**  \n 
        ► Entwicklung der Fallprüfstandssoftware (Back- und Frontend) mit automatisierter Messdatenauswertung von durchgeführten Versuchen, inklusive Datenspeicherung, -strukturierung und Reporting mit Visualisierung für CEN-Zertifizierungen von Bergsportprodukten \n
        ► Entwicklung einer Seilendverbindung mit integrierter Sensorik zur Erfassung von Daten, datengetriebenen Auswertung von Versuchen und Predictive Maintenance mittels Machine Learning \n
        **Durchführung von Forschungs- und Industrieprojekten:**  \n 
        ► Analyse von Problemstellung und Anforderungen \n
        ► Entwurf von Projektplan und statistischer Versuchsplanung \n
        ► Versuchsdurchführung mit Einsatz von passender Messsensorik \n
        ► Datenanalyse und Reporting: Aufbereitung der Ergebnisse in Form von Prüf-/Forschungsberichten \n
        **Gremienarbeit und Lehre**  \n         
        ► Mitarbeit und Experte im Prüflaboratorium für Persönliche Schutzausrüstung gegen Absturz (PSAgA) der notifizierten Stelle \n
        ► Normungsgremienarbeit im Bereich PSAgA (CEN/TC136/WG5 und UIAA): Working Group Leader zur Erarbeitung neuer Normen \n
        ► Lehre: Praktikumsversuch und Betreuung studentischer Arbeiten\n
        """
        )
        
        # --- JOB 2
        st.write('\n')
        st.write("🚧", "**Praktikant Seiltechnik | Fatzer AG**")
        st.write("09/2016 - 01/2017")
        st.write(
            """
        ► Überprüfung der Seillebensdauer in Dauerbiegeversuchen \n
        ► Entwicklung einer Prozessoptimierung von Drahtschweißprozessen mittels Machine Learning\n
        
        """
        )
        
        # --- JOB 3
        st.write('\n')
        st.write("🚧", "**Studentischer Mitarbeiter | Universität Stuttgart**")
        st.write("01/2015 - 10/2017")
        st.write(
            """
        ► Durchführung und Datenauswertung von Seillebensdauerversuchen \n
        ► Entwicklung einer Kalibrierungssoftware für magnetinduktive Seilprüfgeräte \n
        ► Programmierung einer automatisierten Erstellung von Kalibrierprotokollen“
        """
        )
        
        
        # --- Projects & Accomplishments ---
        #st.write('\n')
        #st.subheader("Projects & Accomplishments")
        #st.write("---")
        #for project, link in PROJECTS.items():
        #    st.write(f"[{project}]({link})")
