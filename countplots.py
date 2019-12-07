# LAMOUREUX Camille - 291756
# 2DTTL - Final Project

import initialisation as i

# Selecting data to show
countries = ['France','Italy','Spain','Brazil','Argentina','Germany','England']
data_reduce = i.data.loc[i.data['Nationality'].isin(countries)]

# Creating bar plot
i.sns.barplot(y='Potential', x='Nationality', data=data_reduce)

# Display
i.plt.show()