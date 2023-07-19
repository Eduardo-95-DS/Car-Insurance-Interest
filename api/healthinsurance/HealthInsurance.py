import pickle
import numpy  as np
import pandas as pd

class HealthInsurance(object):
    
    def __init__(self):        
        self.home_path=''
        self.annual_premium_scaler =            pickle.load(open(self.home_path + 'parameters/annual_premium_scaler.pkl','rb'))
        self.age_scaler =                       pickle.load(open(self.home_path + 'parameters/age_scaler.pkl','rb'))
        self.vintage_scaler =                   pickle.load(open(self.home_path + 'parameters/vintage_scaler.pkl','rb'))
#         self.target_encode_gender_scaler =      pickle.load(open(self.home_path + ''))
        self.target_encode_region_code_scaler = pickle.load(open(self.home_path + 'parameters/target_encode_region_code_scaler.pkl','rb')) 
        self.fe_policy_sales_channel_scaler =   pickle.load(open(self.home_path + 'parameters/fe_policy_sales_channel_scaler.pkl','rb'))
        
        
    def data_cleaning(self, df1):
        # 1.1. Rename Columns
        #cols_new = ['id', 'gender', 'age', 'driving_license', 'region_code', 'previously_insured', 'vehicle_age', 
        #            'vehicle_damage', 'annual_premium', 'policy_sales_channel', 'vintage', 'response']

        # rename 
        #df1.columns = cols_new
        
        return df1 


    def feature_engineering(self, df2):  
        
#         df2['vehicle_damage']=df2['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        
        df2['previously_insured']=df2['previously_insured'].apply(lambda x: 'Yes' if x == 1 else 'No')

        df2['driving_license']=df2['driving_license'].apply(lambda x: 'Yes' if x == 1 else 'No')
#         
        df2['vehicle_age']=df2['vehicle_age'].apply(lambda x: 'over_2_years' if x == '> 2 Years' 
                                            else 'between_1_2_years' if x == '1-2 Year'
                                            else 'below_1_year')
                                            
        return df2
    
    
    def data_preparation(self, df5):       
#         annual_premium - standardscaler
        df5['annual_premium']=self.annual_premium_scaler.transform(df5[['annual_premium']].values)
    
#         age - minmaxScaler
        df5['age']=self.age_scaler.transform(df5[['age']].values)
    
#         vintage - minmaxscaler
        #df5['vintage']=self.vintage_scaler.transform(df5[['vintage']].values)
        
#         gender 
#         df5['gender']=df5['gender'].map(self.target_encode_gender_scaler)
        df5=pd.get_dummies(df5,prefix='gender',columns=['gender'])

#         region_code 
        df5['region_code']=df5['region_code'].map(self.target_encode_region_code_scaler)
    
#         vehicle_age 
        df5=pd.get_dummies(df5,prefix='vehicle_age',columns=['vehicle_age'])
    
#         policy_sales_channel 
        df5['policy_sales_channel']=df5['policy_sales_channel'].map(self.fe_policy_sales_channel_scaler)
        
#         previously insured
        df5['previously_insured']=df5['previously_insured'].apply(lambda x: 1 if x == 'Yes' else 0)
        
#         driving license
        df5['driving_license']=df5['driving_license'].apply(lambda x: 1 if x == 'Yes' else 0)
        
#         vehicle damage
        df5['vehicle_damage']=df5['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
    
#         feature selection
        cols_selected=['annual_premium','age','vintage','region_code','vehicle_damage','previously_insured',
                      'policy_sales_channel']
    
        return df5[cols_selected]
    
    
    def get_prediction(self, model, original_data, test_data):
        # model prediction
        pred = model.predict_proba(test_data)

        # join prediction into original data
        original_data['score'] = pred[:, 1].tolist()
        
        return original_data.to_json(orient='records', date_format='iso')
