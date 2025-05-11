import sqlite3

def save_to_sqlite(df, db_path: str, table_name: str):
	conn = sqlite3.connect(db_path)
	df.to_sql(table_name, conn, if exists='replace', index=False)
	conn.close()