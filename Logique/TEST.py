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

# ann and dl libraraies
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam,SGD,Adagrad,Adadelta,RMSprop
from keras.utils import to_categorical

import tensorflow as tf
import random as rn
df=pd.read_csv('IBM.csv')
le = LabelEncoder()

def transform(feature):
    df[feature]=le.fit_transform(df[feature])
    #print(df[feature])
    #print(le.classes_)
cat_df=df.select_dtypes(include='object')

for col in cat_df.columns:
    transform(col)
df.drop(['DailyRate','EmployeeCount','EmployeeNumber','HourlyRate','MonthlyRate'
          ,'Over18','StandardHours', 'StockOptionLevel',
         'JobInvolvement','JobRole','JobSatisfaction','PercentSalaryHike','PerformanceRating','RelationshipSatisfaction'
         ,'YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager','WorkLifeBalance'],axis=1,inplace=True)
print(df.columns)

cor_mat= df.corr()
mask = np.array(cor_mat)
mask[np.tril_indices_from(mask)] = False
fig=plt.gcf()
fig.set_size_inches(100,70)
sns.heatmap(data=cor_mat,mask=mask,square=True,annot=True,cbar=True)
plt.show()