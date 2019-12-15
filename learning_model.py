# LAMOUREUX Camille - 291756
# 2DTTL - Final Project

# Importations
import initialisation as i
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pandas as pd

# Functions definitions
def price_formating(price):
    price = price.replace('€','')
    price = price.replace('.','')
    price = price.replace('K','000')
    price = price.replace('M','000000')

    return float(price)


def weight_formating(df):
    weight_cleaned = df['Weight'].str.extract('(\d+)', expand=False)
    df['Weight'] = pd.to_numeric(weight_cleaned)

    return df


def data_frame_cleaner(df):
    # Identifying columns
    useless_columns = ['Name','Photo','Flag','Club Logo','Contract Valid Until','Release Clause']
    not_numbers_columns = ['Nationality','Club','Preferred Foot','Work Rate','Body Type','Real Face','Position','Joined','Loaned From']
    unknown_columns = ['LS','ST','RS','LW','LF','CF','RF','RW','LAM','CAM','RAM','LM','LCM','CM','RCM','RM','LWB','LDM','CDM','RDM','RWB','LB','LCB','CB','RCB','RB']
    to_drop = useless_columns + unknown_columns

    # Droping columns
    cleaned_df = df.drop(columns=to_drop)

    # Formating columns
    cleaned_df = weight_formating(cleaned_df)
    cleaned_df['Value'] = cleaned_df['Value'].apply(price_formating)
    cleaned_df['Wage'] = cleaned_df['Wage'].apply(price_formating)
    for col in not_numbers_columns :
        pd.get_dummies(cleaned_df[col])

    return cleaned_df



# MAIN
cleaned_data_frame = data_frame_cleaner(i.data)

'''
# FORMATAGE DES DONNEES
data_matrix = data.as_matrix()
x = data_matrix[:,54:59]
y = data_matrix[:,11]

# SUBDIVISION DES DONNEES
x_app,x_test,y_app,y_test = model_selection.train_test_split(x,y,
                                                             test_size=300,
                                                             random_state=0)

# REGRESSION LOGIQUE
regression = LogisticRegression()
modele = regression.fit(x_app,y_app)
print(modele.coef_, modele.intercept_)

# PREDICTION
y_prediction = modele.predict(x_test)



print(x)
'''


