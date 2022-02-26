#%%
import env
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import os

url_titanic = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/titanic_db'
url_iris = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/iris_db'
url_telco = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/telco_churn'

#%%

def get_titanic_data(use_cache =True):
    filename = 'titanic.csv'
    
    if os.path.exists(filename) and use_cache:
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    url = url_titanic
    query = '''
    SELECT *
        FROM passengers
    '''

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df
# %%
get_titanic_data()
# %%
def get_iris_data(use_cache = True):
    filename = 'iris.csv'
    
    if os.path.exists(filename) and use_cache:
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    url = url_iris
    query = '''
    SELECT *
        FROM species
    '''

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df
# %%
get_iris_data()
# %%
def get_telco_data(use_cache = True):
    filename = 'telco.csv'
    
    if os.path.exists(filename) and use_cache:
        print('Reading from csv file...')
        return pd.read_csv(filename)
    
    url = url_telco
    query = '''
    SELECT *
        FROM customers
        JOIN contract_types USING (contract_type_id)
        JOIN internet_service_types USING (internet_service_type_id)
        JOIN payment_types USING (payment_type_id)
    '''

    print('Getting a fresh copy from SQL database...')
    df = pd.read_sql(query, url)
    print('Saving to csv...')
    df.to_csv(filename, index=False)
    return df


# customers, contract_types, internet_service_types, and payment_types
#  4 tables together, contains all the contract, payment, and internet service option

get_telco_data()


# %%
