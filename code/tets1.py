import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Pfad zu src/ hinzufügen, damit wir unsere Module importieren können
sys.path.append(os.path.abspath("/Users/leonmorris/Desktop/python/strommarkt-analyse/strommarkt-analyse/src"))

from data_loader import load_smard_cvs
#from database import save_to_sqlite
from visualizer import plot_time_series

#Daten laden
url = "/Users/leonmorris/Desktop/python/strommarkt-analyse/strommarkt-analyse/raw_data/Realisierter_Stromverbrauch_202501010000_202506010000_Viertelstunde.csv"
df = load_smard_cvs(url)
print(df)

plot_time_series(df, df.index, "Netzlast inkl. Pumpspeicher [MWh] Originalauflösungen", "Stromverbrauch in Deutschland")