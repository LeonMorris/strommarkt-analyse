import matplotlib.pyplot as plt

def plot_time_series(df, time_col, value_col, title):
    #Erstellt eine einfache Zeitreihe-Plot
    #df.plot(x=time_col, y=value_col, figsize=(10,5))
    #plt.figure(figsize=(12,5))
    #plt.plot(df[time_col], df[value_col])
    #plt.title(title)
    #plt.xlable("Zeit")
    #plt.ylable(value_col)
    #plt.grid(True)
    #plt.tight_layout()
    #plt.show()
    plt.figure(figsize=(12, 6))  # Größe des Plots (optional)
    plt.plot(time_col, df[str(value_col)], label= str(title), color='blue')
    #test

    # Achsen beschriften
    plt.xlabel('Zeit')
    plt.ylabel('Verbrauch (MW)')
    plt.title('Stromverbrauch über die Zeit')
    plt.legend()

    # Schönes Layout
    plt.grid(True)
    plt.tight_layout()

    # Plot anzeigen
    plt.show()