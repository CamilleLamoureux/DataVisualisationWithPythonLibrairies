# LAMOUREUX Camille - 291756
# 2DTTL - Final Project

# Importations
import initialisation as i
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split

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

def unvalid_lines_cleaner(df):
    df = df.head(400)

    return df


def data_frame_cleaner(df):
    # Identifying columns
    useless_columns = ['Name','Photo','Flag','Club Logo','Contract Valid Until','Release Clause']
    not_numbers_columns = ['Nationality','Club','Preferred Foot','Work Rate','Body Type','Real Face','Position','Joined','Loaned From']
    unknown_columns = ['LS','ST','RS','LW','LF','CF','RF','RW','LAM','CAM','RAM','LM','LCM','CM','RCM','RM','LWB','LDM','CDM','RDM','RWB','LB','LCB','CB','RCB','RB']
    to_drop = useless_columns + unknown_columns + not_numbers_columns

    # Droping columns
    cleaned_df = df.drop(columns=to_drop)

    # Droping lines
    cleaned_df = unvalid_lines_cleaner(df)


    # Formating columns
    cleaned_df = weight_formating(cleaned_df)
    cleaned_df['Value'] = cleaned_df['Value'].apply(price_formating)
    cleaned_df['Wage'] = cleaned_df['Wage'].apply(price_formating)

    #for col in not_numbers_columns :
    #   pd.get_dummies(cleaned_df[col])


    return cleaned_df


# DATA CLEAN
cleaned_df = data_frame_cleaner(i.data)

# INITIALISATION
X = cleaned_df['Age','Overall','Potential','Height','Weight'].values
y = cleaned_df['Value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=50)

# PREDICTION
linear_regression = linear_model.LinearRegression().fit(X,y)