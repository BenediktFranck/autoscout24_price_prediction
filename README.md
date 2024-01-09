# autoscout24_price_prediction

# Projektbeschreibung (Datensatz analysieren)

In diesem Notebook soll ein Datensatz von [autoscout24](https://www.kaggle.com/datasets/ander289386/cars-germany) analysiert werden und anschließend mit verschiedenen Machine Learning Modellen eine Vorhersage für den Preis zu machen.

# 1. Daten

Die Datei autoscout24.csv enth¨alt Informationen aus AutoScout24 über inserierte Autos. Siehe auch [hier ](https://www.kaggle.com/datasets/ander289386/cars-germany). Diese Daten sollen analysiert und visualsiert werden.

# 2. Analyse

Wieviele Autos wurden inseriert? 
Welche Marken sind erfasst?
Beliebte Automarken und Modelle.
Existieren Korrelationen zwischen den Features? 
Gibt es Veränderungen über die Jahre?
Preise der verschiedenen Automarken.
Mit welchen Automodellen werden die meisten/wenigsten Kilometer gefahren bevor es verkauft wird?

# 3. Machine Learning

Um den Verkaufspreis vorherzusagen werden folgende Modelle traniert und deren Güte bewertet:
- LinearRegression
- DecisionTree
- RandomForest

# 4. Dashboard in Streamlit

Um die Ergebnisse ansprechend darzustellen wurde Streamlit gewählt.
Um die Streamlit App zu starten bitte zuerste das Notebook starten (Lokale Dateien werden erstellt).
Anschließend:
```
streamlit run main.py
```
