import pandas as pd
import acquire

def prep_iris(df):
    '''
    
    '''
    df = df.drop(columns =['species_id', 'measurement_id']) 
    df = df.rename(columns ={'species_name': 'species'})
    dummy_df = pd.get_dummies(df['species'], dummy_na = False, drop_first =[True])
    df = pd.concat([df, dummy_df], axis = 1)
    return df

def prep_titanic(df):
    '''
    
    '''  
    df.drop_duplicates(inplace =True )
    columns_to_drop = ['deck', 'age', 'embarked', 'class', 'passenger_id']
    df = df.drop(columns = columns_to_drop)
    df['embark_town'] = df.embark_town.fillna('Southampton')
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']], dummy_na=False, drop_first = [True, True])
    df = pd.concat([df, dummy_df], axis =1)
    return df

def prep_telco(df):
    ''' 
    
    '''  
    df = df.drop_duplicates()  
    drop_columns = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']
    df = df.drop(columns = drop_columns)
    dummy_df = pd.get_dummies(df[['payment_type', 'internet_service_type', 'contract_type']], dummy_na = False, drop_first = [True, True, True])
    df = pd.concat([df, dummy_df], axis = 1)
    return df