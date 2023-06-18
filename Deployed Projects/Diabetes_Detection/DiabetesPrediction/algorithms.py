import joblib
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn import svm
import pickle


dataset = pd.read_csv('DiabetesPrediction\dataset.csv')
print(dataset.head())

print(dataset.shape)

x=dataset.drop(columns='Outcome',axis=1)
y=dataset['Outcome']

sc = StandardScaler()
sc.fit(x)
s_data = sc.transform(x)
print(s_data)

x = s_data
y=dataset['Outcome']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)

model = svm.SVC(kernel='linear')

model.fit(x_train,y_train)
print(model.score(x_test,y_test))

input = (12,100,84,33,105,30,0.488,46)
input1 = np.asarray(input)
input2 = input1.reshape(1,-1)
std_data = sc.transform(input2)
ans=model.predict(std_data)

if(ans[0]==1):
   print("person have diabetes.")
else:
   print("person does not have diabetes.")

filename= 'diabetes_model.sav'
saved_model=joblib.dump(model,filename)
