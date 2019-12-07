# LAMOUREUX Camille - 291756
# 2DTTL - Final Project

import initialisation as i

more_players_country = i.data['Nationality'].value_counts().idxmax()

print(more_players_country,'got the biggest number of players.')

# Exemple de count plots
#i.sns.countplot(data=i.data,x='Overall')

# Exemple de distplot
#i.sns.distplot(i.data['Overall'])

# Display
i.plt.xticks(rotation=90)
i.plt.show()

'''
NOTES :
    COUNT PLOTS = échelle représentant les effectifs
    DISTPLOTS = échelle entre 0 et 1 (fréquence)
    
    USED WHEN : le distplot permet d'estimer la distribution des données
    le count plots montre le nombre d'éléments dans chaque catégories sous forme de barres (ex : histogramme)
'''