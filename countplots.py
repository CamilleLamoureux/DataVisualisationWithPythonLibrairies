# LAMOUREUX Camille - 291756
# 2DTTL - Final Project

import initialisation as i

# Selecting data to show
nationalities = ['France','Italy','Spain','Brazil','Argentina','Germany','England']
data_reduce = i.data.loc[i.data['Nationality'].isin(nationalities)]

# Creating bar plot
i.sns.barplot(data=data_reduce, y='Nationality',x='Potential')

# Display
i.plt.show()

'''
NOTES :
    Pays avec le plus haut potentiel est l'Espagne.
    NB : On sait que dans le foot, les joueurs peuvent aller jouer dans d'autres pays que celui dont ils ont la nationalité, 
    mais il est impossible avec les données présentes de trier par autre chose que la nationalité.
    On utilise donc les valeurs "Potential" et "Nationality".
'''