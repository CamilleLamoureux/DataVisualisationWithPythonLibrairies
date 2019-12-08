# LAMOUREUX Camille - 291756
# 2DTTL - Final Project

import initialisation as i

# Selecting data
nationalities = ['France','Italy','Spain','Brazil','Argentina','Germany','England']
data_reduce = i.data.loc[i.data['Nationality'].isin(nationalities)]

# Create diagram
i.sns.scatterplot(data=data_reduce, x='Potential', y='Nationality')

# Display
i.plt.show()

'''
NOTES :
    Plupart des valeurs => entre  60 et 90
    Angleterre a le plus de joueur en dessous de cette tranche
    L'Espagne a des joueurs globalement plus fort.
    La France et l'Argentine ont les joueurs les plus forts.
'''
