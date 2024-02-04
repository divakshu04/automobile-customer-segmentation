import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
import warnings
warnings.filterwarnings('ignore')

class segmentation_model():
    def __init__(self, model_file, scaler_file):
        with open('model', 'rb') as model_file, open('scaler', 'rb') as scaler_file:
            self.model = pickle.load(model_file)
            self.scaler = pickle.load(scaler_file)
            self.data = None
    
    def load_and_clean_data(self, data_file):
        df = pd.read_csv(data_file, delimiter=',')
        self.df_with_predictions = df.copy()

        df['Gender'] = df['Gender'].fillna('Male')

        df['Ever_Married'] = df['Ever_Married'].fillna('Yes')

        df['Graduated'] = df['Graduated'].fillna('Yes')
        
        df['Profession'] = df['Profession'].fillna('Artist')

        df['Work_Experience'] = df['Work_Experience'].fillna(1.0)

        df['Family_Size'] = df['Family_Size'].fillna(1.0)

        df['Var_1'] = df['Var_1'].fillna('Cat_6')

        df['Spending_Score'] = df['Spending_Score'].fillna('Low')

        self.cleaned_data = df.copy()

        df = df.drop(['ID','Gender'],axis=1)

        df['Ever_Married'] = df['Ever_Married'].map({'Yes':1, 'No':0})

        df['Graduated'] = df['Graduated'].map({'Yes':1, 'No':0})

        age_upgrade = pd.get_dummies(df['Age'], drop_first=True).astype(int)

        freshers = age_upgrade.loc[:, 19:23].max(axis=1)
        youngsters = age_upgrade.loc[:, 25:33].max(axis=1)
        youngsters_with_experience = age_upgrade.loc[:,35:43].max(axis=1)
        experienced = age_upgrade.loc[:, 45:63].max(axis=1)
        very_experienced = age_upgrade.loc[:, 65:79].max(axis=1)
        professionals = age_upgrade.loc[:,80:89].max(axis=1)

        df = pd.concat([df, freshers, youngsters, youngsters_with_experience, experienced, very_experienced, professionals], axis=1)

        profession = pd.get_dummies(df['Profession'], drop_first=True).astype(int)
        spending_score = pd.get_dummies(df['Spending_Score'], drop_first=True).astype(int)

        var_1 = pd.get_dummies(df['Var_1'], drop_first=True).astype(int)

        cat_1_3_7 = var_1.loc[:,['Cat_3','Cat_7']].max(axis=1)
        cat_2_5 = var_1.loc[:,['Cat_2','Cat_5']].max(axis=1)
        cat_6 = var_1.loc[:,['Cat_6']].max(axis=1)

        df = pd.concat([df, profession, spending_score, cat_1_3_7, cat_2_5, cat_6], axis=1)
        df = df.drop(['Profession', 'Spending_Score', 'Var_1','Age'], axis=1)

        column_name = ['Ever_Married', 'Graduated','Work_Experience',
       'Family_Size', 'freshers', 'youngsters', 'youngsters_with_experience', 'experienced', 'very_experienced', 'professionals',
       'Doctor',
       'Engineer', 'Entertainment', 'Executive', 'Healthcare',
       'Homemaker', 'Lawyer', 'Marketing', 'High', 'Low', 'Cat_1_3_7', 'Cat_2_5',
       'Cat_6']
        df.columns = column_name
        columns = ['Ever_Married', 'freshers', 'youngsters', 'youngsters_with_experience', 'experienced', 'very_experienced', 'professionals',
           'Graduated', 'Work_Experience', 'Doctor', 'Engineer',
       'Entertainment', 'Executive', 'Healthcare', 'Homemaker', 'Lawyer',
       'Marketing',
       'High', 'Low',
       'Family_Size', 'Cat_1_3_7','Cat_2_5',
       'Cat_6']
        df = df[columns]

        self.preprocessed_data = df.copy()

        scaler = StandardScaler()
        self.data = scaler.fit_transform(df)
    
    def predict_output(self):
        if (self.data is not None):
                predictions = self.model.predict(self.data)
                predicted_class_indices = np.argmax(predictions, axis=1)
                label_mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
                predicted_labels = [label_mapping[index] for index in predicted_class_indices]
                self.cleaned_data['Prediction'] = predicted_labels
                return self.cleaned_data

