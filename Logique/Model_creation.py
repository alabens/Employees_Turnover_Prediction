#import DeepLearning
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
from keras.layers import Embedding

from keras import layers
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


df.drop(['DailyRate','EmployeeCount','EmployeeNumber','HourlyRate','MonthlyRate'
          ,'Over18','StandardHours', 'StockOptionLevel','TrainingTimesLastYear','EducationField','EnvironmentSatisfaction',
         'JobInvolvement','JobRole','JobSatisfaction','PercentSalaryHike','PerformanceRating','RelationshipSatisfaction'
         ,'YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager','WorkLifeBalance'],axis=1,inplace=True)


le = LabelEncoder()

def transform(feature):
    df[feature]=le.fit_transform(df[feature])
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




np.random.seed(91)
rn.seed(91)
tf.set_random_seed(91)
HIDDEN_SIZE=50

model = Sequential()

model.add(Dense(input_dim=13,units=50,activation='relu'))
model.add(Dense(units=30,activation='relu'))
model.add(Dense(units=30,activation='tanh'))
model.add(Dense(units=16,activation='tanh'))
model.add(Dense(units=2,activation='sigmoid'))

model.compile(optimizer=Adam(lr=0.01),loss='binary_crossentropy',metrics=['accuracy'])

History=model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=80,verbose=1)

predicted=model.predict_classes(x_test)
scores = model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


#model.save('my_model.h5')
