import matplotlib.pyplot as plt

def plot_time_series(df, time_col: str, value_col: str, title: str)
	df[time_col] = pd.to_datetime(df[time_col])
	df.plot(x=time_col, y=value_col, figsize=(10,5))
	plt.title(title)
	plt.grid(True)
	plt.tight_layout()
	plt.show()