import pandas as pd

def load_smard_cvs(url):
    # lädt SMARD CSV-Datei und bereitet sie auf
    df = pd.read_csv(url, sep=";", decimal=',')#SMARD nutzt komma als Dezimalzeichen
    df.columns = df.columns.str.strip()#Entfernt Leerzeichen
    df = df[["Datum von", "Netzlast inkl. Pumpspeicher [MWh] Originalauflösungen"]]#Nur relevante Spalten
    df = df.dropna()#entfernt Zeilen mit fehlenden Werten
    df["Datum von"] = pd.to_datetime(df["Datum von"],  format="%d.%m.%Y %H:%M")  # Text → datetime
    df = df.set_index('Datum von')

    df['Netzlast inkl. Pumpspeicher [MWh] Originalauflösungen'] = (
        df['Netzlast inkl. Pumpspeicher [MWh] Originalauflösungen']
        .replace('-', None)                     # Strich als fehlenden Wert behandeln
        .str.replace('.', '', regex=False)   # Punkt entfernen (Tausendertrennzeichen)
        .str.replace(',', '.', regex=False)  # Komma → Punkt (Dezimaltrennzeichen)
        .astype(float)                       # Umwandeln in float
    )
    print(df['Netzlast inkl. Pumpspeicher [MWh] Originalauflösungen'].unique()[:10])
    #df['Netzlast inkl. Pumpspeicher [MWh] Originalauflösungen'] = pd.to_numeric(df['Netzlast inkl. Pumpspeicher [MWh] Originalauflösungen'], errors='coerce')
    df_daily = df.resample('D').mean()
    return df_daily