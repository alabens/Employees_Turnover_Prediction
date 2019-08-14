# Ignore  the warnings
import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

# data visualisation and manipulation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
import missingno as msno
from keras.models import model_from_json

#configure
# sets matplotlib to inline and displays graphs below the corressponding cell.

style.use('fivethirtyeight')
sns.set(style='whitegrid',color_codes=True)

#import the necessary modelling algos.
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB

#model selection
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,roc_curve,roc_auc_score
from sklearn.model_selection import GridSearchCV

from imblearn.over_sampling import SMOTE

#preprocess.
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer,LabelEncoder,OneHotEncoder
from sklearn import preprocessing

# ann and dl libraraies
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam,SGD,Adagrad,Adadelta,RMSprop
from keras.utils import to_categorical

import tensorflow as tf
import random as rn

df=pd.read_csv('IBM.csv')
sns.factorplot(data=df,kind='box',size=10,aspect=3)

warnings.filterwarnings('always')
warnings.filterwarnings('ignore')


def plot_cat(attr, labels=None):
    if (attr == 'JobRole'):
        sns.factorplot(data=df, kind='count', size=5, aspect=3, x=attr)
        return

    sns.factorplot(data=df,kind='count',size=5,aspect=1.5,x=attr)

#plot_cat('Attrition')
#corelation matrix.
cor_mat= df.corr()
mask = np.array(cor_mat)
mask[np.tril_indices_from(mask)] = False
fig=plt.gcf()
fig.set_size_inches(30,12)
sns.heatmap(data=cor_mat,mask=mask,square=True,annot=True,cbar=True)
#df.drop(['BusinessTravel','DailyRate','EmployeeCount','EmployeeNumber','HourlyRate','MonthlyRate','NumCompaniesWorked','Over18','StandardHours', 'StockOptionLevel','TrainingTimesLastYear',],axis=1,inplace=True)

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

#for col in df.columns:
    #print(col)

scaler=StandardScaler()
scaled_df=scaler.fit_transform(df.drop('Attrition',axis=1))
X=scaled_df
Y=df['Attrition'].as_matrix()
Y=to_categorical(Y)
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=42)
#print('x_test=',x_test.shape)


np.random.seed(31)
rn.seed(31)
tf.set_random_seed(31)

model=Sequential()
model.add(Dense(input_dim=13,units=50,activation='relu'))
model.add(Dense(units=16,activation='relu'))
model.add(Dense(units=2,activation='sigmoid'))

model.compile(optimizer=Adam(lr=0.01),loss='binary_crossentropy',metrics=['accuracy'])


History=model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=10,verbose=1)
predicted=model.predict_classes(x_test)
scores = model.evaluate(X, Y, verbose=0)

print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

#print (predicted)
#model.save('final_model.h5')

##### SAVING MODEL ######

#model_json = model.to_json()
#with open("model_final.json", "w") as json_file:
    #json_file.write(model_json)
## serialize weights to HDF5
#model.save_weights("model_final.h5")
#print("Saved model to disk")

def resultat(employé):
    employé=employé.reshape(1,13)
    res=model.predict_classes(employé)
    if (str(res)=="[0]") :
        return("NO")
    else :
        return("YES")
    return (res)

def TraveltoInt(travel):
    switcher = {
        "Non-Travel":0,
        "Travel_Frequently" :1,
        "Travel_Rarely":2,
    }
    return switcher.get(travel, "3")

def DepttoInt(Dept):
    switcher = {
        "Human Resources" :0,
        "Research & Development": 1,
        "Sales":2,
    }
    return switcher.get(Dept, "3")

def SextoInt(Sex):
    switcher = {
        "Female" :0,
        "Male": 1,
    }
    return switcher.get(Sex, "2")

def StatustoInt(Status):
    switcher = {
        "Divorced" :0,
        "Married": 1,
        "Single":2,
    }
    return switcher.get(Status, "3")

def OverTimetoInt(time):
    switcher = {
        "No" :0,
        "Yes": 1,
    }
    return switcher.get(time, "")




def predictEmp(employé):

    #employé = le.fit_transform(employé)
    #print(employé)
    #print(scaler.transform([employé]))
    res = model.predict_classes(scaler.transform([employé]))

    if (str(res)=="[0]") :
        return("NO")
    else :
        return("YES")

b = np.array([41,TraveltoInt('Travel_Rarely'),DepttoInt('Sales'),0,2,SextoInt("Female"),2,StatustoInt("Single"),5993,8,OverTimetoInt("Yes"),8,6])

#b = np.array(['Age', 'Travel','Departement', 'distance from home, 'education','sexe','JobLevel' , "marritalStatus", 'salary', 'NumberCompaniesWorked', "overtime", 'totalWorkingyears,'yearsAtCompany'])
print(predictEmp(b))

    #for i in range (30):
    #a = X[i]
    #print(a.shape)
    # print (X.shape)
    #print(X[0])
    #print(resultat(X[0]))

    # print(type(X))

#print(type(b))
#print(b.shape)



