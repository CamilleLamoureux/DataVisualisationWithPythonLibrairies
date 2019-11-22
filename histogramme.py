# LAMOUREUX Camille - 291756
# 2DTTL - Final Project

import initialisation as i

i.sns.distplot(i.data['Overall'])
#i.sns.distplot(i.data['Overall'],hist=False)
#i.sns.distplot(i.data['Overall'],kde=False)
#i.sns.distplot(i.data['Overall'],bins=3)


# Display
i.plt.show()

# Statistic calculations
modal_value = i.data['Overall'].mode()
mean = i.data['Overall'].mean()
median= i.data['Overall'].median()
standard_deviation = i.data['Overall'].std()
minimum = i.data['Overall'].min()
maximum = i.data['Overall'].max()
data_range = maximum - minimum
print(
    'Modal value : ',modal_value,'\n',
    'Mean : ',mean,'\n',
    'Median : ',median,'\n',
    'Standard deviation : ',standard_deviation,'\n',
    'Range : ',data_range,'\n'
)


"""
NOTES SUR LA FONCTION DISPLOT :
    bins = nombre de rectangles
    kde = courbe => si on met False, on a plus la courbe qui s'affiche (default = True)
    hist = histogramme => si on met False, on a plus l'histogramme qui s'affiche (default = True)
    
EXEMPLES DE VARIABLES :
    2 variables quantitatives : Overall & Potential => des variables qui sont des quantités
    2 variables catégorielles : Club & Preferred Foot => des variables qui sont parmi une liste de catégories possibles
    
NOTES SUR L'HISTOGRAMME :
    Valeur approximative du modal :
    Valeurs abhérentes : Non, nous observons une courbe en cloche qui semble logique
    Autres : aucun 70 ?
"""
