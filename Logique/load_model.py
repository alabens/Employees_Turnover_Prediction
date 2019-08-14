from keras.models import load_model
from sklearn.preprocessing import StandardScaler,LabelEncoder
import pandas as pd
import sqlite3
import numpy as np
import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

from datetime import date

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam,SGD,Adagrad,Adadelta,RMSprop
from keras.utils import to_categorical

from sklearn.model_selection import train_test_split
df=pd.read_csv('IBM.csv')
df.drop(['DailyRate','EmployeeCount','EmployeeNumber','HourlyRate','MonthlyRate'
          ,'Over18','StandardHours', 'StockOptionLevel','TrainingTimesLastYear','EducationField','EnvironmentSatisfaction',
         'JobInvolvement','JobRole','JobSatisfaction','PercentSalaryHike','PerformanceRating','RelationshipSatisfaction'
         ,'YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager','WorkLifeBalance'],axis=1,inplace=True)

le = LabelEncoder()

def transform(feature):
    df[feature]=le.fit_transform(df[feature])
    #print(df[feature])
    #print(le.classes_)
cat_df=df.select_dtypes(include='object')
for col in cat_df.columns:
    transform(col)
scaler=StandardScaler()
scaled_df=scaler.fit_transform(df.drop('Attrition',axis=1))
X=scaled_df
Y=df['Attrition'].as_matrix()
Y=to_categorical(Y)
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=42)

model = load_model('final_model.h5')


def TraveltoInt(travel):
    switcher = {
        "Non-Travel": 0,
        "Travel_Frequently": 1,
        "Travel_Rarely": 2,
    }
    return switcher.get(travel, "3")


def DepttoInt( Dept):
    switcher = {
        "Human Resources": 0,
        "Research & Development": 1,
        "Sales": 2,
    }
    return switcher.get(Dept, "3")


def SextoInt( Sex):
    switcher = {
        "Female": 0,
        "Male": 1,
    }
    return switcher.get(Sex, "2")


def StatustoInt(Status):
    switcher = {
        "Divorced": 0,
        "Married": 1,
        "Single": 2,
    }
    return switcher.get(Status, "3")


def OverTimetoInt(time):
    switcher = {
        "No": 0,
        "Yes": 1,
    }
    return switcher.get(time, "")


def predictEmp(employé):
    # employé = le.fit_transform(employé)
    # print(employé)
    # print(scaler.transform([employé]))
    res = model.predict_classes(scaler.transform([employé]))
    ch = ""
    if (str(res) == "[0]"):
        ch = "NO"
    else:
        ch = "Yes"

    return (ch)




