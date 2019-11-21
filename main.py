# Initialisation
import seaborn as sns
import pandas as pd
import numpy as np
import webbrowser
import matplotlib.pyplot as plt


# Reading the csv file into a DF
data = pd.read_csv('data.csv')


# Data visualization with html
url = pd.DataFrame.to_html(data)
print(url)
webbrowser.open_new_tab(url)

# Type and attributes of "data"
print(type(data))

# Histogramme
#sns.distplot(bins=None,hist=True,kde=True)





