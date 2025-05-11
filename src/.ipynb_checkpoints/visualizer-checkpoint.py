import matplotlib.pyplot as plt

def plot_time_series(df, time_col, value_col, title="Zeitreihe"):
    #Erstellt eine einfache Zeitreihe-Plot
	#df.plot(x=time_col, y=value_col, figsize=(10,5))
    plt.figure(figsize=(12,5))
    plt.plot(df[time_col], df[value_col])
	plt.title(title)
    plt.xlable("Zeit")
    plt.ylable(value_col)
	plt.grid(True)
	plt.tight_layout()
	plt.show()