# Telco Churn Classification Project

## Project Description
 - machine learning project with the telco dataset

## Data dictionary
Target  | Description   | Data Type
--|--|--
less_than_a_year    | indicates if the customer has a tenure less than 12 months and has churned. Engineered from the original churn and tenure columns | int64



Categorical Features   | Description |	Data Type
--|--|--
senior_citizen|	indicates if the customer is a senior citizen	|int64
dependents|	    indicates if the customer has dependents	|int64
phone_service|	indicates if the customer has phone service with Telco	| int64
multiple_lines |	indicates if the customer with phone service has multiple lines	| int64
online_security|	indicates if the customer has online security services |	int 64
online_backup|	indicates if the customer has online backup services |	int64
device_protection	| indicates if the customer has device protection services |	int64
tech_support |  indicates if the customer has tech support services |	int64
streaming_tv |	indicates if the customer has tv streaming services |	int64
streaming_movies |	indicates if the customer has movie streaming services |	int64
payment_type    | indicates the type of payment method a customer is using | int64
internet_service_type |	indicates which internet service (if any) the customer has |	int64
gender	|   indicates the the customers' gender identity |	uint8
contract_type | 	indicates the type of contract the customer has with Telco |	int64
auto_bill_pay |	indicates if the customer is enrolled in auto bill pay or not |	int64

Continuous Features | Description | Data Type
--|--|--
monthly_charges | how much a customer pays per month in dollars| float64
total_charges   | how much a customer has paid over the course of their tenure | float64
tenure          | how many months the customer has been with the company| int64

Other   | Description   | Data Type
--|--|--
churn   | indicates whether or not a customer churned | int64
customer_id | customer id number                       | object

## Ideas and Hypotheses

## How to recreatae this Project
You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

1. Read the README.md
2. Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
3. Add your own env file to your directory. (user, password, host)
4. Run the final_telco_report.ipynb notebook

### Other Related Resourses
- [First telco churn project](https://public.tableau.com/profile/heather.mcmillan#!/vizhome/StorytellingProject-TelcoChurn/RetentionPresentation) on Tableau
- My [Trello Board](https://trello.com/b/5lC2YbuY/classification-project) for this project

### Deliverables 
- Jupyter Final Report Notebook (add link)
    - code is commented in notebook adequately
    - supporting markdown text guides the reader through thought process and takeaways
    - functions in acquire and prepare modules include docstrings

- README.md file containing the following:
    - project description and goals (add link)
    - data dictionary (add link)
    - project planning (add link)
    - Initial ideas/hypotheses stated (add link)
    - instructions for recreating project/running repo (add link)

- CSV file with customer_id, probability of churn, predictions (add link)

- Modules to recreate project present (See Module Breakdown)
    - acquire.py (add link)
    - prepare.py (add link)
    - 
- Notebook walkthrough presentation (See Presentation Best Practices)