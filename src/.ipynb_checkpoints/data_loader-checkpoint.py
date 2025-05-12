import pandas as pd

def load_smard_cvs(url):
    # lädt SMARD CSV-Datei und bereitet sie auf
    df = pd.read_csv(url, sep=";", decimal=',')#SMARD nutzt komma als Dezimalzeichen
    df.columns = df.columns.str.strip()#Entfernt Leerzeichen
    df = df[["Datum von", "Netzlast inkl. Pumpspeicher [MWh] Originalauflösungen"]]#Nur relevante Spalten
    df = df.dropna()#entfernt Zeilen mit fehlenden Werten
    return df