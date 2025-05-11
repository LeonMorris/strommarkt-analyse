import pandas as pd

def load_smard_cvs(url):
    # lädt SMARD CVS-Datei und bereitet sie auf
	df = pd.read_csv(url, sep=";", decimal=',') #SMARD nutz komma als Dezimalzeichen
	df.colums = df.columns.str.strip() #Entfernt Leerzeichen
    df["datetime"] = pd.to_datetime(df["Datum"] + " " + df["Uhrzeit"], format="%d.%m.%Y %H:%M")
    df = df[["datetime", "Lasr (MW)"]] #Nur relevante Spalten
    df = df.dropna() #entfernt Zeilen mit fehlenden Werten
	return df