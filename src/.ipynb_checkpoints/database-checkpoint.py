import sqlite3

def save_to_sqlite(df, db_path, table_name):
    #Speichert dataframe in SQLite-Datenbank
	conn = sqlite3.connect(db_path)
	df.to_sql(table_name, conn, if_exists='replace', index=False) #Tabelle ersetzen, wenn sie existiert
	conn.close()