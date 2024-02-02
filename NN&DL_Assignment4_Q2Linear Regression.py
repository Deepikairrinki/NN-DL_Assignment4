#2 QUESTION. Linear Regression

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# a) Importing the Salarydatasets

salaryData = pd.read_csv('Salary_Data.csv')

#excluding last column
X = salaryData.iloc[:, :-1].values
#salary
Y = salaryData.iloc[:, 1].values
salaryData.info()
salaryData.head()


#b) Splitting the dataset into the Training set and Test set

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3, random_state=0)

print("Below is the Split Data:")
print("Train features:")
print(pd.DataFrame(X_train).head())
print("Train targets:")
print(pd.DataFrame(Y_train).head())
print("Test features:")
print(pd.DataFrame(X_test).head())
print("Test targets:")
print(pd.DataFrame(Y_test).head())



# c) Train and predict the model

model = LinearRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print("Predicted values:", Y_pred)



#d) Calculate the mean_squared error

mse = mean_squared_error(Y_test, Y_pred)
print("Mean Squared Error:", mse)



#e) Visualize both train and test data using scatter plot.
#The scatter function is used to plot the training data, and the plot function is used to plot the predicted values


# Training Data
plt.scatter(X_train, Y_train)
plt.plot(X_train, model.predict(X_train), color='red')
plt.title('Training Set')
plt.show()

# Testing Data
plt.scatter(X_test, Y_test)
plt.plot(X_test, model.predict(X_test), color='red')
plt.title('Testing Set')
plt.show()