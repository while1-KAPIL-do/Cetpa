#------------------------------------ OOPS ------------------------------------

class employee:
     def __init__(self,first,last,pay):
          self.first = first
          self.last = last
          self.email = first+"."+last+"@koozoo.com"
          self.pay = pay
     
     def fullname(self):
          return '{} {}'.format(self.first,self.last)
     def applyraise(self):
          self.pay = int(self.pay*10.4) # 4% increase
          return self.pay
          
'''
emp_1 = employee()
emp_2 = employee()
print(emp_1)
print(emp_2)

emp_1.firstName = "Kapil"
emp_1.lastName = "Agrawal"
emp_1.email = "kk@gmail.com"
emp_1.pay = "680000"

print("Name\t",emp_1.firstName,emp_1.lastName)
print("Email\t",emp_1.email)
print("pay\t",emp_1.pay)
'''

# Constractor
emp2 = employee('Ayushi','Singhal',76000)
print(emp2.fullname())
print(emp2.applyraise())

# ---------------------------- ML --------------------------------------------

import numpy as np
import pandas as pd
# import matplotlib as pl
# import matplotlib.pyplot as plt

df = {"dbc":[5,7,8,7,8,8,5,8,9],
      "dbm":[16,17,16,28,30,34,48,54,52],
      "speed":[1200,1500,1800,1200,1500,1800,1200,1500,1800],
      "DEFECT":[0,0,0,1,1,1,1.5,1.5,1.5]}

data = pd.DataFrame(df)
data

x = data.drop(['DEFECT'], axis = 1)
y = data.DEFECT
print(x)
print(y)


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
lr = LinearRegression().fit(x,y)
y_train_pred = lr.predict(x)
y_train_pred

# testing
df = {"dbc":[6.,8,9],
      "dbm":[60,62,59],
      "speed":[1200,1500,1800]}

x_test = pd.DataFrame(df)
x_test

y_test_pred = lr.predict(x_test)
y_test_pred

Size_comparison = {"Data_size":[2,2,2],
                   "Size_test_ML":[1.97316117, 2.07083559,1.84664684]}
final_data_size = pd.DataFrame(Size_comparison)
final_data_size






df = {"dbc":[5,6,6,6,6,6,7,9,8],
      "dbm":[14,16,17,22,24,25,34,36,38],
      "speed":[1200,1500,1800,1200,1500,1800,1200,1500,1800],
      "DEFECT":[0,0,0,1,1,1,1.5,1.5,1.5]}

data = pd.DataFrame(df)
data

x = data.drop(['DEFECT'], axis = 1)
y = data.DEFECT
print(x)
print(y)


lr = LinearRegression().fit(x,y)
y_train_pred = lr.predict(x)
y_train_pred

# testing
df = {"dbc":[8,10,10],
      "dbm":[40,42,43],
      "speed":[1200,1500,1800]}

x_test = pd.DataFrame(df)
x_test

y_test_pred = lr.predict(x_test)
y_test_pred

Size_comparison = {"Data_size":[2,2,2],
                   "Size_test_ML":[2.04347237, 1.76083424, 1.76137595]}
final_data_size = pd.DataFrame(Size_comparison)
final_data_size










