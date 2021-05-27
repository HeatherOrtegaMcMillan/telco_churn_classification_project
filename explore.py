import pandas as pd
import numpy as np
import seaborn as sns


################################### telco_churn Exploring Functions ###############################

# function to plot counts all the object columns 
def plot_counts(df):
    '''
    This function takes in the dataframe and plots the counts of all the objects in the dataframe
    '''
    for col in df.columns:
        # skip over customer ID
        if col == 'customer_id':
            continue
        if df[col].dtype == 'object':
            # use seaborn countplot 
            sns.countplot(df[col])
            plt.title(f'{col} counts')
            plt.show()