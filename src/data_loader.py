import pandas as pd

def load_smard_cvs(url: str) -> pd.DataFrame:
	df = pd.read_csv(url, sep=";")
	df.colums = df.columns.str.strip() #Spaltennamen bereinigen
	return df