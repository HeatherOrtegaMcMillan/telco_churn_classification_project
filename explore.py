import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import scipy.stats as stats


################################### telco_churn Exploring Functions ###############################

###### function to plot counts all the object columns 
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


###### RUN METRICS FUNCTION 
def run_metrics(X, y, model, data_set = 'This'):
    """
    This function takes in a sklearn model and a data set name and prints out metrics for that model. 
    X = X_train, X_validate, or X_test
    y = y_train, y_validate, or y_test
    model = name of model 
    data_set = 'train', 'validate', or 'test' (AS A STRING)
    Can only be used after data is split, and X_ and y_ variables have been set, and after the sklearn model has been created
    Will output the Precision Score, the classification report, the confusion matrix, True Positive, False Positive, True Negative, and False Negative rates
    It is advisable to print the name of the model you're working with before hand for clarity
    i.e. print('Metrics for Model 1 with Train data\n')
    USE EXAMPLE: run_metrics(X_train, y_train, model1, data_set = 'Train')
    """
    score = model.score(X, y)
    matrix = confusion_matrix(y, model.predict(X))
    tpr = matrix[1,1] / (matrix[1,1] + matrix[1,0])
    fpr = matrix[0,1] / (matrix[0,1] + matrix[0,0])
    tnr = matrix[0,0] / (matrix[0,0] + matrix[0,1])
    fnr = matrix[1,0] / (matrix[1,1] + matrix[1,0])
    print(f'{data_set} data set accuracy score: {score:.2%}')
    class_report = classification_report(y, model.predict(X), zero_division=True)
    print('-------------------------------')
    print(f'classification report')
    print(class_report)
    print ('-------------------------------')
    print('')
    print('confusion matrix')
    print(matrix)
    print(' ')
    print(f'{data_set} data set model metrics')
    print('---------------------------------')
    print(f'True positive rate for the model is {tpr:.2%}')
    print(f'False positive rate for the model is  {fpr:.2%}')
    print(f'True negative rate for the model is {tnr:.2%}')
    print(f'False negative rate for the model is {fnr:.2%}')
    prc = matrix[1,1] / (matrix[1,1] + matrix[0,1])
    print('---------------------------------')
    print(f'{data_set} data set accuracy score: {score:.2%}')
    print(f'{data_set} data set precision score {prc:.2%}')
    print(f'{data_set} data set recall score: {tpr:.2%}')

######### Contingency metrics, hypothesis testing function
def contingency_metrics(crosstab, alpha = 0.05):
    '''
    This function takes in a crosstab, and outputs the observed, expected values, chi2 and p statistics.
    Alpha is automatically set to 0.05. Will say if null hypothesis can be rejected or not.
    '''
    chi2, p, degf, expected = stats.chi2_contingency(crosstab)

    crosstab.rename(index={0: 'Stayed', 1: 'Churned'}, inplace=True)
    
    print('~~ Observed ~~\n')
    display(crosstab)
    print('\n~~ Expected ~~\n')
    display(pd.DataFrame(expected.round(), index=crosstab.index, columns=crosstab.columns))
    print('\n~~ Statistics ~~\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')
    if p < alpha:
        print(f'\n~~~~ We can reject the null hypothesis. Yay! ~~~~')
    else:
        print(f'\n~~~~ We cannot reject the null hypothesis ~~~~ ')
              

