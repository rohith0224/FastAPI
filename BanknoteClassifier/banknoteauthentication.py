
import pandas as pd
import numpy as np

df=pd.read_csv("BankNote_Authentication.csv")



X=df.iloc[:,:-1]
Y=df.iloc[:,-1]



from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

from sklearn.ensemble import RandomForestClassifier

model=RandomForestClassifier()
model.fit(X_train,Y_train)

model.predict(X_test)

model.score(X_test,Y_test)

import pickle

pickle.dump(model,open("model.pkl",'wb'))

