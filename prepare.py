import pandas as pd
import numpy as np
import acquire
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import sklearn.feature_selection as feat_select
import scipy.stats as stats
from sklearn.preprocessing import LabelEncoder



###################################### Test Train Split ######################################

def test_train_split(df, stratify_val = 'churn'):
    '''
    args: df
    This function take in the telco_churn data data acquired by aquire.py, get_telco_data(),
    performs a split, stratifies by churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=713,
                                        stratify = df[stratify_val])
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=713,
                                   stratify= train_validate[stratify_val])
    return train, validate, test

def all_aboard_the_X_train(X_cols, y_col, train, validate, test):
    '''
    X_cols = list of column names you want as your features
    y_col = string that is the name of your target column
    train = the name of your train dataframe
    validate = the name of your validate dataframe
    test = the name of your test dataframe
    outputs X_train and y_train, X_validate and y_validate, and X_test and y_test
    6 variables come out! So have that ready
    '''
    
    # do the capital X lowercase y thing for train test and split
    # X is the data frame of the features, y is a series of the target
    X_train, y_train = train[X_cols], train[y_col]
    X_validate, y_validate = validate[X_cols], validate[y_col]
    X_test, y_test = test[X_cols], test[y_col]
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test

###################################### Prep Telco ######################################

def prep_telco(df):
    """
    This functions takes in the telco churn dataframe and retuns the cleaned and prepped dataset
    Use this function for exploring
    """

    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    train, validate, test = test_train_split(df)

    return train, validate, test

def prep_telco_hypothesis(df):
    """
    This functions takes in the telco churn dataframe and retuns the cleaned and prepped dataset
    Use this function for exploring
    """

    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    df['less_than_a_year'] = (((df['tenure'] < 12) == True) & ((df['churn'] == 'Yes') == True)).astype(int)
    train, validate, test = test_train_split(df)

    return train, validate, test

def prep_telco_model(df):
    '''
    This function takes in a dataframe and returns the cleaned, encoded and split data.
    Use this function before modeling.
    Stratified on churned. Adds column churned in under a year. 
    returns train, validate, test
    DOESN'T DO THIS YET: Also splits into X and y sections. Function returns X_train, y_train, X_validate, y_validate, X_test, y_test
    

    '''
    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    
    # list of columns to drop
    cols_to_drop = ['payment_type_id', 'internet_service_type_id','contract_type_id']

    # drop superfulous columns
    df = df.drop(columns=cols_to_drop)

    # get list of columns that need to be encoded
    cols = [col for col in list(df.columns) if df[col].dtype == 'object']
    
    # turn all text (object) columns to numbers using LabelEncoder()
    label_encoder = LabelEncoder()
    for col in cols:
        df[col] = label_encoder.fit_transform(df[col])

    # adds column for less than a year, If their tenure is less than a year and they have churned it's a 1
    df['less_than_a_year'] = (((df['tenure'] < 12) == True) & ((df['churn'] == 1) == True)).astype(int)

    # split into train validate and test 
    # Maybe try stratifying on new column less_than_a_year, similar to churn
    train, validate, test = test_train_split(df)

    return train, validate, test

def prep_full_telco(df):
    '''
    Does the same thing as prep_telco_model except no split. For creating CSV
    '''

    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    
    # list of columns to drop
    cols_to_drop = ['payment_type_id', 'internet_service_type_id','contract_type_id']

    # drop superfulous columns
    df = df.drop(columns=cols_to_drop)

    # get list of columns that need to be encoded
    cols = [col for col in list(df.columns) if df[col].dtype == 'object']

    # turn all text (object) columns to numbers using LabelEncoder()
    label_encoder = LabelEncoder()
    for col in cols:
        if col != 'customer_id':
            df[col] = label_encoder.fit_transform(df[col])

    # adds column for less than a year, If their tenure is less than a year and they have churned it's a 1
    df['less_than_a_year'] = (((df['tenure'] < 12) == True) & ((df['churn'] == 1) == True)).astype(int)

    return df
