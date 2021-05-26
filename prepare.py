import pandas as pd
import numpy as np
import acquire
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer 


###################################### Test Train Split ######################################

def test_train_split(df):
    '''
    args: df
    This function take in the telco_churn data data acquired by aquire.py, get_telco_data(),
    performs a split, stratifies by churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=713,
                                        stratify = df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=713,
                                   stratify= train_validate.churn)
    return train, validate, test

###################################### Prep Telco ######################################

def prep_telco(df):
    """
    This functions takes in the telco churn dataframe and retuns the cleaned and prepped dataset
    """

    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    train, validate, test = test_train_split(df)

    return train, validate, test
